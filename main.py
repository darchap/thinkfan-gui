import logging
import sys

import customtkinter

from left_frame import LeftFrame
from right_frame import InfoFrame


class App:
    APPEARANCE_MODE = "dark"
    COLOR_THEME = "green"
    WINDOW_TITLE = "ThinkFan GUI"
    WINDOW_SIZE = "800x350"

    def __init__(self):
        customtkinter.set_appearance_mode(self.APPEARANCE_MODE)
        customtkinter.set_default_color_theme(self.COLOR_THEME)

        self.root = customtkinter.CTk()
        self.root.title(self.WINDOW_TITLE)
        self.root.geometry(self.WINDOW_SIZE)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        LeftFrame(self.root)
        InfoFrame(self.root)

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    app = App()
    app.start()
