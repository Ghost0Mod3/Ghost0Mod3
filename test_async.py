from scapy.all import AsyncSniffer
import time

print("Starting AsyncSniffer")

sniffer = AsyncSniffer(
    iface="wlan1",
    prn=lambda p: print("PACKET"),
    store=False
)

sniffer.start()

time.sleep(10)

sniffer.stop()

print("Done")
