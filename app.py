import tkinter as tk

from widgets import Entries, AddButton


class App(tk.Tk):
    def __init__(self, connection):
        super().__init__()
        self.conn = connection
        self.title('Home budget')
        self.geometry('500x300')
        self.minsize(500, 300)
        self.resizable(False, False)

        entry1 = Entries(self, 'Category:')
        entry2 = Entries(self, 'Amount:')
        entry3 = Entries(self, 'Date:')

        AddButton(self,
                  self.conn,
                  'Button 1',
                  entry1,
                  entry2,
                  entry3)
        # Buttons(self, 'Button 2')
        # Buttons(self, 'Button 3')

        self.mainloop()
