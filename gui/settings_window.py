import tkinter as tk
from tkinter import ttk

from gui.scrollable_frame import ScrollableFrame


class SettingsWindow:

    def __init__(self, parent):

        self.window = tk.Toplevel(parent)

        self.window.title(
            "Ghost0Mod3 Settings"
        )

        screen_width = (
            self.window.winfo_screenwidth()
        )

        screen_height = (
            self.window.winfo_screenheight()
        )

        self.window.geometry(
            f"{screen_width}x{screen_height}"
        )

        self.scroll = ScrollableFrame(
            self.window
        )

        self.scroll.pack(
            fill="both",
            expand=True
        )

        self.content = (
            self.scroll.scrollable_frame
        )

        self.build_ui()

    def build_ui(self):

        title = tk.Label(
            self.content,
            text="Ghost0Mod3 Settings",
            font=("Arial", 18, "bold")
        )

        title.pack(
            pady=10
        )

        # ----------------------------------
        # Scanner
        # ----------------------------------

        scanner_frame = ttk.LabelFrame(
            self.content,
            text="Scanner"
        )

        scanner_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.auto_scan = tk.BooleanVar(
            value=True
        )

        self.channel_hopping = tk.BooleanVar(
            value=True
        )

        self.scan_24 = tk.BooleanVar(
            value=True
        )

        self.scan_5 = tk.BooleanVar(
            value=True
        )

        ttk.Checkbutton(
            scanner_frame,
            text="Auto Start Scan",
            variable=self.auto_scan
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        ttk.Checkbutton(
            scanner_frame,
            text="Channel Hopping",
            variable=self.channel_hopping
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        ttk.Checkbutton(
            scanner_frame,
            text="Scan 2.4 GHz",
            variable=self.scan_24
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        ttk.Checkbutton(
            scanner_frame,
            text="Scan 5 GHz",
            variable=self.scan_5
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        # ----------------------------------
        # Audio
        # ----------------------------------

        audio_frame = ttk.LabelFrame(
            self.content,
            text="Audio"
        )

        audio_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.radar_sound = tk.BooleanVar(
            value=True
        )

        self.target_sound = tk.BooleanVar(
            value=True
        )

        ttk.Checkbutton(
            audio_frame,
            text="Radar Sounds",
            variable=self.radar_sound
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        ttk.Checkbutton(
            audio_frame,
            text="Target Lock Sounds",
            variable=self.target_sound
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        # ----------------------------------
        # Display
        # ----------------------------------

        display_frame = ttk.LabelFrame(
            self.content,
            text="Display"
        )

        display_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        self.auto_display = tk.BooleanVar(
            value=True
        )

        self.fullscreen = tk.BooleanVar(
            value=False
        )

        self.vehicle_mode = tk.BooleanVar(
            value=False
        )

        ttk.Checkbutton(
            display_frame,
            text="Auto Detect Display",
            variable=self.auto_display
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        ttk.Checkbutton(
            display_frame,
            text="Fullscreen",
            variable=self.fullscreen
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        ttk.Checkbutton(
            display_frame,
            text="Vehicle Mode",
            variable=self.vehicle_mode
        ).pack(
            anchor="w",
            padx=10,
            pady=2
        )

        # ----------------------------------
        # Target Tracking
      
