import tkinter as tk
from tkinter import ttk


class Dashboard:

    def __init__(self, scanner):

        self.scanner = scanner

        self.root = tk.Tk()

        self.root.title("Ghost0Mod3 v0.0.1")

        self.root.geometry("1000x600")

        self.root.configure(bg="#111111")

        self.build_ui()

        self.update_networks()

    def build_ui(self):

        title = tk.Label(
            self.root,
            text="Ghost0Mod3",
            font=("Arial", 24, "bold"),
            fg="#00ffcc",
            bg="#111111"
        )

        title.pack(pady=10)

        self.status_label = tk.Label(
            self.root,
            text="Status: Scanning",
            fg="lime",
            bg="#111111",
            font=("Arial", 12)
        )

        self.status_label.pack()

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

        self.tree.heading("ssid", text="SSID")
        self.tree.heading("bssid", text="BSSID")
        self.tree.heading("rssi", text="RSSI")
        self.tree.heading("channel", text="Channel")

        self.tree.column("ssid", width=250)
        self.tree.column("bssid", width=200)
        self.tree.column("rssi", width=80)
        self.tree.column("channel", width=80)

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def update_networks(self):

        networks = self.scanner.get_networks()

        self.tree.delete(*self.tree.get_children())

        for network in networks:

            self.tree.insert(
                "",
                "end",
                values=(
                    network.get("ssid"),
                    network.get("bssid"),
                    network.get("rssi"),
                    network.get("channel"),
                )
            )

        self.root.after(
            1000,
            self.update_networks
        )

    def run(self):

        self.root.mainloop()
