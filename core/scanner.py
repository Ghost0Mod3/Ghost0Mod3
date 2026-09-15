# core/scanner.py

import threading
import subprocess

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

    def setup_monitor_mode(self):

        print(
            f"Configuring {self.iface} for monitor mode..."
        )

        try:

            subprocess.run(
                [
                    "ip",
                    "link",
                    "set",
                    self.iface,
                    "down"
                ],
                check=True
            )

            subprocess.run(
                [
                    "iw",
                    "dev",
                    self.iface,
                    "set",
                    "type",
                    "monitor"
                ],
                check=True
            )

            subprocess.run(
                [
                    "ip",
                    "link",
                    "set",
                    self.iface,
                    "up"
                ],
                check=True
            )

            print(
                f"{self.iface} now in monitor mode."
            )

        except Exception as error:

            print(
                f"Monitor mode setup failed: {error}"
            )

    def verify_monitor_mode(self):

        try:

            result = subprocess.run(
                [
                    "iw",
                    "dev",
                    self.iface,
                    "info"
                ],
                capture_output=True,
                text=True
            )

            if "type monitor" in result.stdout:

                print(
                    f"{self.iface} monitor mode verified."
                )

                return True

            print(
                f"{self.iface} is not in monitor mode."
            )

            return False

        except Exception as error:

            print(
                f"Monitor mode verification failed: {error}"
            )

            return False

    def start(self):

        if self.running:
            return

        if not SCAPY_AVAILABLE:

            print(
                "Scapy not available"
            )

            return

        self.setup_monitor_mode()

        if not self.verify_monitor_mode():

            print(
                "Scanner startup aborted."
            )

            return

        print(
            f"Starting scanner on {self.iface}"
        )

        self.sniffer = AsyncSniffer(
            iface=self.iface,
            prn=self.handle_packet,
            store=False
        )

        self.sniffer.start()

        self.channel_hopper.start()

        self.running = True

    def stop(self):

        print(
            "Stopping scanner"
        )

        self.channel_hopper.stop()

        if self.sniffer and self.running:

            try:

                self.sniffer.stop()

            except Exception as error:

                print(error)

        self.running = False

    def get_status(self):

        if self.running:
            return "Scanning"

        return "Stopped"

    def handle
