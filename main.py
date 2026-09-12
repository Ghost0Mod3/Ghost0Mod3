from core.scanner import Scanner
import time

def main():

    scanner = Scanner("wlan1")

    scanner.start()

    try:

        while True:

            networks = scanner.get_networks()

            print(f"Networks: {len(networks)}")

            time.sleep(1)

    except KeyboardInterrupt:

        scanner.stop()

if __name__ == "__main__":
    main()
