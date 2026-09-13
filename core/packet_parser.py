# core/packet_parser.py

from scapy.all import (
    Dot11Elt,
    Dot11Beacon,
    Dot11ProbeResp,
)


class PacketParser:

    @staticmethod
    def get_ssid(packet):

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

    @staticmethod
    def get_bssid(packet):

        try:

            return packet.addr2

        except Exception:

            return None

    @staticmethod
    def get_rssi(packet):

        try:

            return int(
                getattr(
                    packet,
                    "dBm_AntSignal",
                    -100
                )
            )

        except Exception:

            return -100

    @staticmethod
    def get_channel(packet):

        try:

            if packet.haslayer(Dot11Beacon):

                stats = packet[
                    Dot11Beacon
                ].network_stats()

            elif packet.haslayer(
                Dot11ProbeResp
            ):

                stats = packet[
                    Dot11ProbeResp
                ].network_stats()

            else:

                return -1

            return int(
                stats.get(
                    "channel",
                    -1
                )
            )

        except Exception:

            return -1

    @staticmethod
    def get_crypto(packet):

        try:

            if packet.haslayer(Dot11Beacon):

                stats = packet[
                    Dot11Beacon
                ].network_stats()

            elif packet.haslayer(
                Dot11ProbeResp
            ):

                stats = packet[
                    Dot11ProbeResp
                ].network_stats()

            else:

                return "UNKNOWN"

            crypto = stats.get(
                "crypto",
                []
            )

            if not crypto:

                return "OPEN"

            return ",".join(
                sorted(
                    str(item)
                    for item in crypto
                )
            )

        except Exception:

            return "UNKNOWN"

    @staticmethod
    def parse(packet):

        return {

            "ssid":
                PacketParser.get_ssid(
                    packet
                ),

            "bssid":
                PacketParser.get_bssid(
                    packet
                ),

            "rssi":
                PacketParser.get_rssi(
                    packet
                ),

            "channel":
                PacketParser.get_channel(
                    packet
                ),

            "crypto":
                PacketParser.get_crypto(
                    packet
                )
        }