# gui/track_window.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from core.target_manager import TargetManager


class TrackWindow:

    def __init__(self, parent):

        self.target_manager = TargetManager()

        self.window = tk.Toplevel(parent)

        self.window.title(
            "Target Tracking"
        )

        self.window.geometry(
            "600x500"
        )

        self.window.minsize(
            400,
            350
        )

        self.build_ui()

        self.refresh()

    def build_ui(self):

        self.main_frame = ttk.Frame(
            self.window,
            padding=10
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        title = tk.Label(
            self.main_frame,
            text="TRACK TARGET",
            font=("Arial", 18, "bold")
        )

        title.pack(
            pady=(0, 15)
        )

        self.status_label = tk.Label(
            self.main_frame,
            text="No Target Loaded",
            font=("Arial", 12)
        )

        self.status_label.pack(
            pady=(0, 10)
        )

        info_frame = ttk.LabelFrame(
            self.main_frame,
            text="Target Information"
        )

        info_frame.pack(
            fill="x",
            padx=5,
            pady=5
        )

        self.ssid_var = tk.StringVar(
            value="N/A"
        )

        self.bssid_var = tk.StringVar(
            value="N/A"
        )

        self.rssi_var = tk.StringVar(
            value="N/A"
        )

        self.channel_var = tk.StringVar(
            value="N/A"
        )

        self.security_var = tk.StringVar(
            value="N/A"
        )

        self.risk_var = tk.StringVar(
            value="N/A"
        )

        self.category_var = tk.StringVar(
            value="N/A"
        )

        self.add_row(
            info_frame,
            "SSID",
            self.ssid_var,
            0
        )

        self.add_row(
            info_frame,
            "BSSID",
            self.bssid_var,
            1
        )

        self.add_row(
            info_frame,
            "RSSI",
            self.rssi_var,
            2
        )

        self.add_row(
            info_frame,
            "Channel",
            self.channel_var,
            3
        )

        self.add_row(
            info_frame,
            "Security",
            self.security_var,
            4
        )

        self.add_row(
            info_frame,
            "Risk",
            self.risk_var,
            5
        )

        self.add_row(
            info_frame,
            "Category",
            self.category_var,
            6
        )

        button_frame = ttk.Frame(
            self.main_frame
        )

        button_frame.pack(
            fill="x",
            pady=15
        )

        refresh_btn = ttk.Button(
            button_frame,
            text="Refresh",
            command=self.refresh
        )

        refresh_btn.pack(
            side="left",
            padx=5
        )

        clear_btn = ttk.Button(
            button_frame,
            text="Clear Target",
            command=self.clear_target
        )

        clear_btn.pack(
            side="left",
            padx=5
        )

        close_btn = ttk.Button(
            button_frame,
            text="Close",
            command=self.window.destroy
        )

        close_btn.pack(
            side="right",
            padx=5
        )

    def add_row(
        self,
        parent,
        label,
        variable,
        row
    ):

        ttk.Label(
            parent,
            text=f"{label}:"
        ).grid(
            row=row,
            column=0,
            sticky="w",
            padx=10,
            pady=4
        )

        ttk.Label(
            parent,
            textvariable=variable
        ).grid(
            row=row,
            column=1,
            sticky="w",
            padx=10,
            pady=4
        )

    def refresh(self):

        target = self.target_manager.load_target()

        if not target:

            self.status_label.config(
                text="No Active Target"
            )

            self.clear_display()

            return

        self.status_label.config(
            text="TRACKING"
        )

        self.ssid_var.set(
            target.get(
                "ssid",
                "Unknown"
            )
        )

        self.bssid_var.set(
            target.get(
                "bssid",
                "Unknown"
            )
        )

        self.rssi_var.set(
            target.get(
                "rssi",
                "Unknown"
            )
        )

        self.channel_var.set(
            target.get(
                "channel",
                "Unknown"
            )
        )

        self.security_var.set(
            target.get(
                "crypto",
                "Unknown"
            )
        )

        self.risk_var.set(
            target.get(
                "risk",
                "Unknown"
            )
        )

        self.category_var.set(
            target.get(
                "category",
                "Unknown"
            )
        )

    def clear_display(self):

        self.ssid_var.set("N/A")
        self.bssid_var.set("N/A")
        self.rssi_var.set("N/A")
        self.channel_var.set("N/A")
        self.security_var.set("N/A")
        self.risk_var.set("N/A")
        self.category_var.set("N/A")

    def clear_target(self):

        result = messagebox.askyesno(
            "Clear Target",
            "Remove current target?"
        )

        if not result:
            return

        self.target_manager.clear_target()

        self.refresh()
