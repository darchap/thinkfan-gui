import customtkinter


class LeftFrame(customtkinter.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        # Set properties of the left frame
        self.configure(width=10, height=400, corner_radius=0)
        self.grid(row=0, column=0, sticky="w")
        #self.grid_rowconfigure(6, weight=1)

        # Add widgets to the left frame
        self.label = customtkinter.CTkLabel(self, text="Menu", font=(None, 20))
        self.label.grid(row=0, column=0)
        
        # Add stats button
        self.button1 = customtkinter.CTkButton(self, text="Stats")
        self.button1.grid(row=1, column=0)

        # Add appearance mode button
        self.appearance_mode_label = customtkinter.CTkLabel(
            self, text="Appearance Mode:")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(200,0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(0,10))


    def change_appearance_mode_event(self, new_appearance_mode: str):
            customtkinter.set_appearance_mode(new_appearance_mode)