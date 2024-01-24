import logging
import subprocess

import customtkinter

from dialogs import WarningWindow
from permissions import update_fan_value
from sensors import get_info


class InfoFrame(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.PROC_PATH = "/proc/acpi/ibm/fan"

        # Set properties of the frame
        self.configure(width=300, corner_radius=0)
        self.grid(row=0, column=1)

        # Create and add widgets
        self._create_info_frame()
        self._create_slider()
        self._create_slider_label()
        self._create_buttons()

        # Update labels
        self.update_info()

    def _create_info_frame(self):
        self.info_frame = customtkinter.CTkFrame(self)
        self.info_frame.grid(row=0, column=0, sticky="nsew")
        self.info_label = customtkinter.CTkLabel(self.info_frame, text="")
        self.info_label.grid(row=0, column=0, sticky="nsew")

    def _create_slider(self):
        self.slider = customtkinter.CTkSlider(self, from_=0, to=7, number_of_steps=7, command=self.update_slider_label)
        self.slider.grid(row=1, column=2)

    def _create_slider_label(self):
        self.slider_label = customtkinter.CTkLabel(
            self,
            text=f"Set fan level: {int(self.slider.get())}",
            font=(None, 16),
        )
        self.slider_label.grid(row=0, column=2, sticky="nsew")

    def _create_buttons(self):
        self.slider_button = customtkinter.CTkButton(
            self,
            text="Set",
            command=lambda: self.button_event(f"level {self.slider.get()}"),
        )
        self.slider_button.grid(row=1, column=3, padx=20, pady=5, sticky="nsew")

        self.auto_button = customtkinter.CTkButton(
            self,
            text="Auto",
            command=lambda: self.button_event("level auto"),
        )
        self.auto_button.grid(row=2, column=2, padx=(10, 5), pady=5, sticky="nsew")

        self.disengaged_button = customtkinter.CTkButton(
            self,
            text="Disengaged",
            command=lambda: self.button_event("level disengaged"),
        )
        self.disengaged_button.grid(row=2, column=3, padx=(5, 10), pady=5, sticky="nsew")

    def update_info(self):
        self.info_label.configure(text="\n{}".format("\n".join(get_info())), font=(None, 16))
        self.after(1000, self.update_info)

    def update_slider_label(self, _):
        fan_level = int(self.slider.get())
        self.slider_label.configure(text=(f"Set fan level: {fan_level}"))

    def show_warning_message(self, title, message):
        self.warning_window = WarningWindow(self, title, message)

    def button_event(self, command):
        try:
            update_fan_value(self.PROC_PATH, command)

        except PermissionError as e:
            self.show_warning_message(
                "Error",
                "Please check the file permissions",
            )
            logging.error(e)

        except FileNotFoundError as e:
            self.show_warning_message("Error", f"{self.PROC_PATH} does not exist!")
            logging.error(e)

        except OSError as e:
            self.show_warning_message(
                "Error",
                "Check that /etc/modprobe.d/thinkpad_acpi.conf contains 'options thinkpad_acpi fan_control=1'",
            )
            logging.error(e)

        except subprocess.CalledProcessError:
            logging.error("Failed to execute the command. Please check the command.")


class AboutFrame(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.PROC_PATH = "/proc/acpi/ibm/fan"

        # Set properties of the frame
        self.configure(width=300, corner_radius=0)
        self.grid(row=0, column=1)

        self._create_slider_label()

        def _create_slider_label(self):
            self.slider_label = customtkinter.CTkLabel(
                self,
                text=f"Set fan level: {int(self.slider.get())}",
                font=(None, 16),
            )
            self.slider_label.grid(row=0, column=2, sticky="nsew")
