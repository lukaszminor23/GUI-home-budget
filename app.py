import tkinter as tk
from widgets import Entries, Buttons


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Home budget')
        self.geometry('500x300')
        self.minsize(500, 300)

        Entries(self, 'Category:')
        Entries(self, 'Amount:')
        Entries(self, 'Date:')

        Buttons(self, 'Button 1')
        Buttons(self, 'Button 2')
        Buttons(self, 'Button 3')

        self.mainloop()


App()
