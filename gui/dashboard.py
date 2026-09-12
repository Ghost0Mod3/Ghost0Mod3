import tkinter as tk
from tkinter import ttk


class Dashboard:

    def __init__(self, scanner):

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
            text="Status: Scanning"
        )

        self.status.pack()

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

        for col in columns:

            self.tree.heading(
                col,
                text=col.upper()
            )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def update_networks(self):

        networks = self.scanner.get_networks()

        self.tree.delete(
            *self.tree.get_children()
  *     )

        for network in net*orks:

            self.tree.inser*(
                "",
            *   "end",
                values=(*                    network.get("s*id"),
                    network.*et("bssid"),
                    n*twork.get("rssi"),
               *    network.get("channel")
       *        )
            )

        s*lf.root.after(
            1000,
 *          self.update_networks
   *    )

    def run(self):

       *self.root.mainloop()
