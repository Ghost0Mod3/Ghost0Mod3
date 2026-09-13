# core/scanner.py

import threading

try:

    from scapy.all import (
        AsyncSniffer,
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

        self.sniffer = None

        self.lock = threading.RLock()

        self.networks = {}

        self.channel_hopper = ChannelHopper(
            self.iface
        )

    def start(self):

        if self.running:
            return

        if not SCAPY_AVAILABLE:

            self.running = True
            return

        self.sniffer = AsyncSniffer(
            iface=self.iface,
            prn=self.handle_packet,
            store=False
        )

        self.sniffer.start()

        self.channel_hopper.start()

        self.running = True

    def stop(self):

        self.channel_hopper.stop()

        if self.sniffer and self.running:

            try:

                self.sniffer.stop()

            except Exception:

                pass

        self.running = False

    def get_status(self):

        if self.running:

            return "Scanning"

        return "Stopped"

    def handle_packet(self, packet):

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
            network.get(
                "ssid",
                "Unknown"
            ),
            network.get(
                "crypto",
                "UNKNOWN"
            )
        )

        network["risk"] = classification[
            "risk"
        ]

        network["category"] = classification[
            "category"
        ]

        with self.lock:

            self.networks[bssid] = network

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