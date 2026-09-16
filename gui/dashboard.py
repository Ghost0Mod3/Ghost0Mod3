import tkinter as tk
from tkinter import ttk

from core.target_manager import TargetManager

try:
    from gui.track_window import TrackWindow
except Exception:
    TrackWindow = None


class Dashboard:

    def __init__(self, scanner=None):

        self.scanner = scanner

        self.target_manager = TargetManager()

        self.current_target = (
            self.target_manager.load_target()
        )

        self.root = tk.Tk()

        self.root.title("Ghost0Mod3")

        self.root.geometry("1000x700")

        self.build_ui()

        self.refresh_target_panel()

        self.update_networks()

    def build_ui(self):

        title = tk.Label(
            self.root,
            text="Ghost0Mod3",
            font=("Arial", 24, "bold")
        )

        title.pack(
            pady=10
        )

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

        button_frame = tk.Frame(
            self.root
        )

        button_frame.pack(
            pady=10
        )

        self.start_button = tk.Button(
            button_frame,
            text="Start",
            width=10,
            command=self.start_scan
        )

        self.start_button.pack(
            side=tk.LEFT,
            padx=5
        )

        self.stop_button = tk.Button(
            button_frame,
            text="Stop",
            width=10,
            command=self.stop_scan
        )

        self.stop_button.pack(
            side=tk.LEFT,
            padx=5
        )

        self.track_button = tk.Button(
            button_frame,
            text="Track",
            width=10,
            command=self.track_selected
        )

        self.track_button.pack(
            side=tk.LEFT,
            padx=5
        )

        self.clear_button = tk.Button(
            button_frame,
            text="Clear",
            width=10,
            command=self.clear_target
        )

        self.clear_button.pack(
            side=tk.LEFT,
            padx=5
        )

        self.refresh_button = tk.Button(
            button_frame,
            text="Refresh",
            width=10,
            command=self.manual_refresh
        )

        self.refresh_button.pack(
            side=tk.LEFT,
            padx=5
        )

        self.settings_button = tk.Button(
            button_frame,
            text="Settings",
            width=10,
            command=self.open_settings
        )

        self.settings_button.pack(
            side=tk.LEFT,
            padx=5
        )

        columns = (
            "ssid",
            "bssid",
            "rssi",
            "channel"
        )

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=10
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
            text="CH"
        )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        target_frame = ttk.LabelFrame(
            self.root,
            text="TARGET WIFI"
        )

        target_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.target_ssid = tk.Label(
            target_frame,
            text="SSID: None",
            anchor="w"
        )

        self.target_ssid.pack(
            fill="x"
        )

        self.target_bssid = tk.Label(
            target_frame,
            text="BSSID: None",
            anchor="w"
        )

        self.target_bssid.pack(
            fill="x"
        )

        self.target_rssi = tk.Label(
            target_frame,
            text="RSSI: None",
            anchor="w"
        )

        self.target_rssi.pack(
            fill="x"
        )

        self.target_channel = tk.Label(
            target_frame,
            text="CH: None",
            anchor="w"
        )

        self.target_channel.pack(
            fill="x"
        )

        self.target_status = tk.Label(
            target_frame,
            text="STATUS: NONE",
            anchor="w"
        )

        self.target_status.pack(
            fill="x"
        )

    def open_settings(self):

        self.status.config(
            text="Status: Settings Coming Soon"
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

    def track_selected(self):

        selected = self.tree.focus()

        if not selected:

            self.status.config(
                text="Status: No Network Selected"
            )

            return

        values = self.tree.item(
            selected
        )["values"]

        self.current_target = {

            "ssid": values[0],
            "bssid": values[1],
            "rssi": values[2],
            "channel": values[3]

        }

        self.target_manager.save_target(
            self.current_target
        )

        self.refresh_target_panel()

        self.status.config(
            text="Status: Tracking Target"
        )

        if TrackWindow:

            try:

                TrackWindow(
                    self.root
                )

            except Exception as error:

                print(error)

    def clear_target(self):

        self.current_target = None

        self.target_manager.clear_target()

        self.refresh_target_panel()

        self.status.config(
            text="Status: Target Cleared"
        )

    def refresh_target_panel(self):

        if not self.current_target:

            self.target_ssid.config(
                text="SSID: None"
            )

            self.target_bssid.config(
                text="BSSID: None"
            )

            self.target_rssi.config(
                text="RSSI: None"
            )

            self.target_channel.config(
                text="CH: None"
            )

            self.target_status.config(
                text="STATUS: NONE"
            )

            return

        self.target_ssid.config(
            text=f"SSID: {self.current_target.get('ssid')}"
        )

        self.target_bssid.config(
            text=f"BSSID: {self.current_target.get('bssid')}"
        )

        self.target_rssi.config(
            text=f"RSSI: {self.current_target.get('rssi')}"
        )

        self.target_channel.config(
            text=f"CH: {self.current_target.get('channel')}"
        )

        self.target_status.config(
            text="STATUS: TRACKING ACTIVE"
        )

    def manual_refresh(self):

        self.current_target = (
            self.target_manager.load_target()
        )

        self.refresh_target_panel()

        self.status.config(
            text="Status: Refreshed"
        )

    def update_networks(self):

        if self.scanner:

            networks = self.scanner.get_networks()

            self.status.config(
                text=f"Status: {self.scanner.get_status()}"
            )

        else:

            networks = []

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
