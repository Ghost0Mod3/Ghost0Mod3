# core/scanner.py

import threading
import time

from scapy.all import (
    AsyncSniffer,
    Dot11,
    Dot11Beacon,
    Dot11ProbeResp,
    Dot11Elt,
)


class Scanner:

    def __init__(self, iface="wlan1"):

        self.iface = iface

        self.sniffer = None

        self.running = False

        self.lock = threading.RLock()

        self.networks = {}

    def get_ssid(self, packet):

        try:

            elt = packet.getlayer(Dot11Elt)

            while elt:

                if getattr(elt, "ID", None) == 0:

                    raw = elt.info

                    decoded = raw.decode(
                        "utf-8",
                        errors="replace"
                    ).strip()

                    return decoded or "Hidden SSID"

                elt = elt.payload.getlayer(Dot11Elt)

        except Exception:
            pass

        return "Hidden SSID"

    def get_channel(self, packet):

        try:

            stats = packet[Dot11Beacon].network_stats()

            return int(stats.get("channel", -1))

        except Exception:

            return -1

    def handle_packet(self, packet):

        if not (
            packet.haslayer(Dot11Beacon)
            or packet.haslayer(Dot11ProbeResp)
        ):
            return

        bssid = packet[Dot11].addr2

        if not bssid:
            return

        rssi = int(
            getattr(
                packet,
                "dBm_AntSignal",
                -100,
            )
        )

        ssid = self.get_ssid(packet)

        channel = self.get_channel(packet)

        with self.lock:

            self.networks[bssid] = {

                "ssid": ssid,

                "bssid": bssid,

                "rssi": rssi,

                "channel": channel,

                "last_seen": time.time(),
            }

    def start(self):

        if self.running:
            return

        self.sniffer = AsyncSniffer(
            iface=self.iface,
            prn=self.handle_packet,
            store=False,
        )

        self.sniffer.start()

        self.running = True

    def stop(self):

        if self.sniffer:

            self.sniffer.stop()

        self.running = False

    def get_networks(self):

        with self.lock:

            return sorted(
                self.networks.values(),
                key=lambda network: network["rssi"],
                reverse=True
            )
