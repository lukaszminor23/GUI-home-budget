import matplotlib.pyplot as plt
from tkinter import messagebox


def add_item(self):
    sql = '''INSERT INTO expenses VALUES(null, ?, ?, ?)'''
    cursor = self.conn.cursor()
    cursor.execute(sql, (str(self.category), float(str(self.amount)), str(self.date)))
    self.conn.commit()
    messagebox.showinfo(None, 'Item has been added to the database')


def list_items(connection):
    sql = '''SELECT * FROM expenses'''
    cursor = connection.cursor()
    for record in cursor.execute(sql):
        print(record)


def create_plot(connection):
    plot_dict = {}
    sql = '''SELECT category, amount FROM expenses'''
    cursor = connection.cursor()
    for record in cursor.execute(sql):
        plot_dict[record[0]] = plot_dict.get(record[0], 0) + record[1]

    plt.bar(plot_dict.keys(), plot_dict.values())
    plt.show()
