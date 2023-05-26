from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt


class Buttons(ttk.Frame):
    def __init__(self, parent, connection, category, amount, date):
        super().__init__(master=parent)
        self.conn = connection
        self.category = category
        self.amount = amount
        self.date = date

        self.columnconfigure(0, weight=1, uniform='a')
        self.columnconfigure(1, weight=1, uniform='a')
        self.columnconfigure(2, weight=1, uniform='a')
        self.rowconfigure(0, weight=1)

        ttk.Button(self, text='Add item', command=lambda: self.add_item()).grid(
            row=0,
            column=0,
            sticky='snew',
            pady=3,
            padx=3,
            ipady=20)

        ttk.Button(self, text='List items', command=lambda: self.list_items()).grid(
            row=0,
            column=1,
            sticky='snew',
            pady=3,
            padx=3,
            ipady=20)

        ttk.Button(self, text='Display chart', command=lambda: self.create_plot()).grid(
            row=0,
            column=2,
            sticky='snew',
            pady=3,
            padx=3,
            ipady=20)

        self.pack(expand=True, fill='both')

    def add_item(self):
        sql = '''INSERT INTO expenses VALUES(null, ?, ?, ?)'''
        cursor = self.conn.cursor()
        cursor.execute(sql, (str(self.category), float(str(self.amount)), str(self.date)))
        self.conn.commit()
        messagebox.showinfo(None, 'Item has been added to the database')

    def create_plot(self):
        plot_dict = {}
        sql = '''SELECT category, amount FROM expenses'''
        cursor = self.conn.cursor()
        for record in cursor.execute(sql):
            plot_dict[record[0]] = plot_dict.get(record[0], 0) + record[1]

        plt.bar(plot_dict.keys(), plot_dict.values())
        plt.show()

    def list_items(self):
        sql = '''SELECT * FROM expenses'''
        cursor = self.conn.cursor()
        for record in cursor.execute(sql):
            print(record)
