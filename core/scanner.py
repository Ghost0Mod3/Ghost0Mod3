# core/scanner.py

import threading

try:

    from scapy.all import (
        sniff,
        Dot11Beacon,
        Dot11ProbeResp,
    )

    SCAPY_AVAILABLE = True

except ImportError:

    SCAPY_AVAILABLE = False

from core.packet_parser import PacketParser
from core.channel_hopper import ChannelHopper
from core.classifier import Classifier


class Scanner:

    def __init__(self, iface="wlan1"):

        self.iface = iface

        self.running = False

        self.lock = threading.RLock()

        self.networks = {}

        self.sniffer_thread = None

        self.channel_hopper = ChannelHopper(
            self.iface
        )

    def sniff_loop(self):

        print(f"Sniffing on {self.iface}")

        sniff(
            iface=self.iface,
            prn=self.handle_packet,
            store=False
        )

    def start(self):

        if self.running:
            return

        if not SCAPY_AVAILABLE:

            print("Scapy unavailable")

            return

        print(f"Starting scanner on {self.iface}")

        self.running = True

        self.channel_hopper.start()

        self.sniffer_thread = threading.Thread(
            target=self.sniff_loop,
            daemon=True
        )

        self.sniffer_thread.start()

    def stop(self):

        print("Stopping scanner")

        self.running = False

        self.channel_hopper.stop()

    def get_status(self):

        if self.running:
            return "Scanning"

        return "Stopped"

    def handle_packet(self, packet):

        if not self.running:
            return

        if not (
            packet.haslayer(Dot11Beacon)
            or packet.haslayer(Dot11ProbeResp)
        ):
            return

        network = PacketParser.parse(packet)

        bssid = network.get("bssid")

        if not bssid:
            return

        classification = Classifier.classify(
            network.get("ssid", "Unknown"),
            network.get("crypto", "UNKNOWN")
        )

        network["risk"] = classification["risk"]

        network["category"] = classification["category"]

        with self.lock:

            self.networks[bssid] = network

        print(
            f"{network.get('ssid')} "
            f"{network.get('rssi')} dBm"
        )

    def get_networks(self):

        with self.lock:

            return sorted(
                self.networks.values(),
                key=lambda network: network.get(
                    "rssi",
                    -100
                ),
                reverse=True
            )

    def get_network_count(self):

        with self.lock:

            return len(
                self.networks
            )
