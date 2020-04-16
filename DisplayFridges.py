import sqlite3
import tkinter as tk
from tkinter import ttk

def OpenAllFridges():
    conn = sqlite3.connect('Test.db')
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    window_Fridges = tk.Tk()
    window_Fridges.title("FRIDGES")

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'NumBoxes', 'BoxWidth', 'BoxLength', 'BoxHeight')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=7)

    c.execute("SELECT * FROM fridgeTable ")

    for row in c.fetchall():
        tree.insert("", "end", values = (row))
        print(row)


    window_Fridges.mainloop()
    c.close()
    conn.close()
#----------------------------------------------------------------------------------------
    

#----------------------------------------------------------------------------------------
def OpenFridgeSearch(searchField):
    conn = sqlite3.connect('Test.db')
    c = conn.cursor()

    window_Fridges = tk.Tk()
    window_Fridges.title("FRIDGES")

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'NumBoxes', 'BoxWidth', 'BoxLength', 'BoxHeight')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=7)

    c.execute("SELECT * FROM fridgeTable WHERE fridgeID=?", (str(searchField),))

    for row in c.fetchall():
        tree.insert("", "end", values = (row))
        print(row)


    window_Fridges.mainloop()
    c.close()
    conn.close()
#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------
def OpenTemperatureSearch(searchField):
    conn = sqlite3.connect('Test.db')
    c = conn.cursor()

    window_Fridges = tk.Tk()
    window_Fridges.title("FRIDGES")

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'NumBoxes', 'BoxWidth', 'BoxLength', 'BoxHeight')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=7)

    c.execute("SELECT * FROM fridgeTable WHERE temperature=?", (int(searchField),))

    for row in c.fetchall():
        tree.insert("", "end", values = (row))
        print(row)


    window_Fridges.mainloop()
    c.close()
    conn.close()
#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------
def OpenNumShelvesSearch(searchField):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    window_Fridges = tk.Tk()
    window_Fridges.title("FRIDGES")

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'NumBoxes', 'BoxWidth', 'BoxLength', 'BoxHeight')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=7)

    c.execute("SELECT * FROM fridgeTable WHERE numShelves=?", (int(searchField),))

    for row in c.fetchall():
        tree.insert("", "end", values = (row))
        print(row)


    window_Fridges.mainloop()
    c.close()
    conn.close()
#----------------------------------------------------------------------------------------

