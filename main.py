from core.scanner import Scanner
from gui.dashboard import Dashboard


def main():

    scanner = Scanner("wlan1")

    scanner.start()

    dashboard = Dashboard(scanner)

    try:

        dashboard.run()

    finally:

        scanner.stop()


if __name__ == "__main__":
    main()
