import tkinter as tk

from widgets import Entries, Buttons


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

        Buttons(self, self.conn, entry1, entry2, entry3)

        self.mainloop()
