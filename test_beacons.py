from scapy.all import sniff
from scapy.all import Dot11Beacon


def show(pkt):

    if pkt.haslayer(Dot11Beacon):

        print("BEACON:", pkt.addr2)


print("Listening...")

sniff(
    iface="wlan1",
    prn=show,
    store=False
)
