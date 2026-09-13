import tkinter as tk
from tkinter import ttk


class Dashboard:

    def __init__(self, scanner=None):

        self.scanner = scanner

        self.root = tk.Tk()

        self.root.title("Ghost0Mod3 v0.0.1")

        self.root.geometry("1000x600")

        self.build_ui()

        self.update_networks()

    def build_ui(self):

        title = tk.Label(
            self.root,
            text="Ghost0Mod3",
            font=("Arial", 22, "bold")
        )

        title.pack(pady=10)

        self.status = tk.Label(
            self.root,
            text="Status: Ready"
        )

        self.status.pack()

        self.network_count = tk.Label(
            self.root,
            text="Networks: 0"
        )

        self.network_count.pack()

        # Buttons

        button_frame = tk.Frame(self.root)

        button_frame.pack(pady=10)

        self.start_button = tk.Button(
            button_frame,
            text="Start Scan",
            width=15,
            command=self.start_scan
        )

        self.start_button.pack(
            side=tk.LEFT,
            padx=5
        )

        self.stop_button = tk.Button(
            button_frame,
            text="Stop Scan",
            width=15,
            command=self.stop_scan
        )

        self.stop_button.pack(
            side=tk.LEFT,
            padx=5
        )

        # Network Table

        columns = (
            "ssid",
            "bssid",
            "rssi",
            "channel"
        )

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings"
        )

        self.tree.heading(
            "ssid",
            text="SSID"
        )

        self.tree.heading(
            "bssid",
            text="BSSID"
        )

        self.tree.heading(
            "rssi",
            text="RSSI"
        )

        self.tree.heading(
            "channel",
            text="CHANNEL"
        )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def start_scan(self):

        if self.scanner:

            self.scanner.start()

        self.status.config(
            text="Status: Scanning"
        )

    def stop_scan(self):

        if self.scanner:

            self.scanner.stop()

        self.status.config(
            text="Status: Stopped"
        )

    def update_networks(self):

        if self.scanner:

            networks = self.scanner.get_networks()

            self.status.config(
                text=f"Status: {self.scanner.get_status()}"
            )

        else:

            networks = []

            self.status.config(
                text="Status: No Scanner"
            )

        self.tree.delete(
            *self.tree.get_children()
        )

        for network in networks:

            self.tree.insert(
                "",
                "end",
                values=(
                    network.get("ssid"),
                    network.get("bssid"),
                    network.get("rssi"),
                    network.get("channel")
                )
            )

        self.network_count.config(
            text=f"Networks: {len(networks)}"
        )

        self.root.after(
            1000,
            self.update_networks
        )

    def run(self):

        self.root.mainloop()