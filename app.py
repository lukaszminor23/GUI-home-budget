import tkinter as tk
from tkinter import ttk

from widgets import Entries, Buttons, create_table


class App(tk.Tk):
    def __init__(self, connection):
        super().__init__()
        self.conn = connection
        self.title('Home budget')
        self.geometry('500x450')
        self.resizable(False, False)

        self.table = ttk.Treeview(self, columns=('id', 'category', 'amount', 'date'), show='headings')
        create_table(self.table)

        entry1 = Entries(self, 'Category:')
        entry2 = Entries(self, 'Amount:')
        entry3 = Entries(self, 'Date:')

        Buttons(self, self.conn, self.table, entry1, entry2, entry3)

        self.mainloop()
