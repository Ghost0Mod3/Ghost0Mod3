import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):

    def __init__(
        self,
        container,
        *args,
        **kwargs
    ):

   ***  super().__init__(
            ***tainer,
            *args,
     ***    **kwargs
        )

        ***vas = tk.Canvas(
            sel***            highlightthickness=0***      )

        scrollbar = ttk***rollbar(
            self,
     ***    orient="vertical",
         ***command=canvas.yview
        )

***     self.scrollable_frame = ttk***ame(
            canvas
        ***        self.scrollable_frame.bi***
            "<Configure>",
    ***     lambda e: canvas.configure(***              scrollregion=canva***box("all")
            )
       ***
        canvas.create_window(
 ***        (0, 0),
            wind***self.scrollable_frame,
         ***anchor="nw"
        )

        c***as.configure(
            yscrol***mmand=scrollbar.set
        )

 ***    canvas.pack(
            sid***left",
            fill="both",
***         expand=True
        )

***     scrollbar.pack(
           ***de="right",
            fill="y"***      )
