import customtkinter


class WarningWindow(customtkinter.CTkToplevel):
    def __init__(self, master=None, title=None, message=None):
        super().__init__(master)
        self.title(title)
        self.geometry("800x150")
        self.label = customtkinter.CTkLabel(self, text=message, font=(None, 16))
        self.label.pack(padx=20, pady=20)
        self.ok_button = customtkinter.CTkButton(self, text="OK", command=self.destroy)
        self.ok_button.pack(side="bottom", padx=20, pady=20)
