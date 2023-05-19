from tkinter import ttk


class Entries(ttk.Frame):
    def __init__(self, parent, label_name):
        super().__init__(master=parent)
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure(0, weight=1)

        ttk.Label(self, text=label_name, font='Helvetica').grid(
            row=0,
            column=0,
            sticky='nsew',
            pady=5,
            padx=5)
        ttk.Entry(self, font=('Helvetica', 22)).grid(
            row=0,
            column=1,
            sticky='nsew',
            pady=5,
            padx=5)

        self.pack(expand=True, fill='both')


class Buttons(ttk.Frame):
    def __init__(self, parent, button_name):
        super().__init__(master=parent)

        ttk.Button(self, text=button_name).pack(
            fill='both',
            expand=True,
            pady=3,
            padx=3,
            ipady=20
        )

        self.pack(side='left', expand=True, fill='both')
