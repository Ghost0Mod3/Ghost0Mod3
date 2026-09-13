import threading
import subprocess
import time


class ChannelHopper:

    def __init__(self, iface="wlan1"):

        self.iface = iface

        self.running = False

        self.thread = None

        self.channels = [
            1, 6, 11,
            36, 40, 44, 48
        ]

    def start(self):

        if self.running:
            return

        self.running = True

        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )

        self.thread.start()

    def stop(self):

        self.running = False

    def run(self):

        while self.running:

            for channel in self.channels:

                if not self.running:
                    break

                try:

                    subprocess.run(
                        [
                            "iw",
                            "dev",
                            self.iface,
                            "set",
                            "channel",
                            str(channel)
                        ],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )

                except Exception:

                    pass

                time.sleep(0.5)