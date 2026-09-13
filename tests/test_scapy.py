from scapy.all import sniff

print("Waiting for packets...")

sniff(
    iface="wlan1",
    prn=lambda pkt: print("PACKET"),
    store=False
)
