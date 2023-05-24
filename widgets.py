from tkinter import ttk
import tkinter as tk
from tkinter import messagebox


class Entries(ttk.Frame):
    def __init__(self, parent, label_name):
        super().__init__(master=parent)
        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=3, uniform='a')
        self.rowconfigure(0, weight=1)
        self.entry_text = tk.StringVar()

        ttk.Label(self, text=label_name, font='Helvetica').grid(
            row=0,
            column=0,
            sticky='nsew',
            pady=5,
            padx=5)
        ttk.Entry(self, font=('Helvetica', 22), textvariable=self.entry_text).grid(
            row=0,
            column=1,
            sticky='nsew',
            pady=5,
            padx=5)

        self.pack(expand=True, fill='both')

    def __str__(self):
        return self.entry_text.get()


class AddButton(ttk.Frame):
    def __init__(self, parent, connection, button_name, category, amount, date):
        super().__init__(master=parent)
        self.category = category
        self.amount = amount
        self.date = date
        self.button_name = button_name
        self.conn = connection

        ttk.Button(self, text=self.button_name,
                   command=lambda: self.add_item()).pack(
            fill='both',
            expand=True,
            pady=3,
            padx=3,
            ipady=20)

        self.pack(side='left', expand=True, fill='both')

    def add_item(self):
        sql = '''INSERT INTO expenses VALUES(null, ?, ?, ?)'''
        cursor = self.conn.cursor()
        cursor.execute(sql, (str(self.category), float(str(self.amount)), str(self.date)))
        self.conn.commit()
        messagebox.showinfo(None, 'Item has been added to the database')
