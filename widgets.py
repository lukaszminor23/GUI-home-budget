from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt
from matplotlib import style


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
        ttk.Entry(self, font=('Helvetica', 15), textvariable=self.entry_text).grid(
            row=0,
            column=1,
            sticky='nsew',
            pady=5,
            padx=5)

        self.pack(expand=True, fill='both')

    def __str__(self):
        return self.entry_text.get()


class Buttons(ttk.Frame):
    def __init__(self, parent, connection, table, category, amount, date):
        super().__init__(master=parent)
        self.conn = connection
        self.category = category
        self.amount = amount
        self.date = date
        self.table = table

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

        ttk.Button(self, text='List items', command=lambda: self.list_items(self.conn, self.table)).grid(
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

        style.use('fivethirtyeight')
        plt.bar(plot_dict.keys(), plot_dict.values())
        plt.title('Amount of money spent by category')
        plt.xlabel('Categories')
        plt.ylabel('Amount')
        plt.show()

    def list_items(self, conn, table):
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM expenses''')
        records = cursor.fetchall()
        for item in table.get_children():
            table.delete(item)

        for record in records:
            id = record[0]
            category = record[1]
            amount = record[2]
            date = record[3]
            data = (id, category, amount, date)
            table.insert(parent='', index=tk.END, values=data)


def create_table(table):
    table.heading('id', text='id')
    table.heading('category', text='Category')
    table.heading('amount', text='Amount')
    table.heading('date', text='Date')
    table.column('id', width=100)
    table.column('category', width=100)
    table.column('amount', width=100)
    table.column('date', width=100)
    table.pack(fill='both')
