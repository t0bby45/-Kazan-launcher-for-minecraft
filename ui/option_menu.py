import customtkinter as ctk

class CustomCTkOptionMenu(ctk.CTkFrame):
    def __init__(self, master, values, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.values = values
        self.command = command
        self.variable = ctk.StringVar()
        self.listbox_visible = False

        self.button = ctk.CTkButton(self, text="", command=self.toggle_listbox)
        self.button.pack(fill="x")

        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        for value in self.values:
            ctk.CTkButton(self.scrollable_frame, text=value, command=lambda v=value: self.select(v)).pack(fill="x")

    def toggle_listbox(self):
        if self.listbox_visible:
            self.scrollable_frame.pack_forget()
        else:
            self.scrollable_frame.pack(fill="x")
        self.listbox_visible = not self.listbox_visible

    def select(self, value):
        self.variable.set(value)
        self.button.configure(text=value)
        self.scrollable_frame.pack_forget()
        self.listbox_visible = False
        if self.command:
            self.command(value)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)
        self.button.configure(text=value)

    def configure_values(self, values):
        self.values = values
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        for value in self.values:
            ctk.CTkButton(self.scrollable_frame, text=value, command=lambda v=value: self.select(v)).pack(fill="x")