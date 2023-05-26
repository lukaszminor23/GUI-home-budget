import tkinter as tk

from widgets import Entries, AddButton, PlotButton, ListButton
from utils import create_plot, list_items


class App(tk.Tk):
    def __init__(self, connection):
        super().__init__()
        self.conn = connection
        self.title('Home budget')
        self.geometry('450x230')
        self.resizable(False, False)

        entry1 = Entries(self, 'Category:')
        entry2 = Entries(self, 'Amount:')
        entry3 = Entries(self, 'Date:')

        AddButton(self, self.conn, 'Add item', entry1, entry2, entry3)
        ListButton(self, self.conn, 'List items')
        PlotButton(self, self.conn, 'Show chart')

        self.mainloop()
