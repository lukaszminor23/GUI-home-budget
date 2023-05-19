import tkinter as tk

from widgets import Entries, Buttons


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Home budget')
    root.geometry('500x300')
    root.minsize(500, 300)

    Entries(root, 'Category:')
    Entries(root, 'Amount:')
    Entries(root, 'Date:')

    Buttons(root, 'Button 1')
    Buttons(root, 'Button 2')
    Buttons(root, 'Button 3')

    root.mainloop()
