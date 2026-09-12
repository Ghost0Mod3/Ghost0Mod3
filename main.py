from core.scanner import Scanner

scanner = Scanner("wlan1")

scanner.start()

try:

    while True:

        networks = scanner.get_networks()

        print(f"Networks: {len(networks)}")

except KeyboardInterrupt:

    scanner.stop()
