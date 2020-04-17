import sqlite3
import tkinter as tk
from tkinter import ttk

def OpenAllFridges():
    conn = sqlite3.connect('Test.db')
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    window_Fridges = tk.Tk()
    window_Fridges.title("FRIDGES")

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'WidthShelves')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=7)

    c.execute("SELECT * FROM FridgeTable")

    for row in c.fetchall():
        tree.insert("", "end", values = (row))
        print(row)

    def openFridgeSearchMenu():
    	window_Fridges.destroy()
    	MainFridge_Window()
    	

    backButton = tk.Button(window_Fridges, text = 'Back to Search Menu', command = openFridgeSearchMenu).grid(row=5, column=1)
    
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

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'WidthShelves')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=7)

    c.execute("SELECT * FROM FridgeTable WHERE fridgeID=?", (str(searchField),))

    for row in c.fetchall():
        tree.insert("", "end", values = (row))
        print(row)

    def openFridgeSearchMenu():
        window_Fridges.destroy()
        MainFridge_Window()

    backButton = tk.Button(window_Fridges, text = 'Back to Search Menu', command = openFridgeSearchMenu).grid(row=5, column=1)
    
    window_Fridges.mainloop()
    c.close()
    conn.close()
#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------
def OpenTemperatureSearch(searchField):
    conn = sqlite3.connect('Test.db')
    c = conn.cursor()

    if searchField == "":
        message_window = tk.Tk()
        message_window.title("ERROR")
        message = tk.Label(message_window, text = "That is not a valid temperature")
        message.grid(row = 0, column = 0)

        def openFridgeSearchMenu():
            message_window.destroy()
            MainFridge_Window()
            
            
        backButton = tk.Button(message_window, text = 'Back to Search Menu', command = openFridgeSearchMenu).grid(row=1)

    else:
        window_Fridges = tk.Tk()
        window_Fridges.title("FRIDGES")

        cols = ('Fridge ID', 'Temperature', 'NumShelves', 'WidthShelves')
        tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
        tree.grid(row=2, column=0, columnspan=7)

        c.execute("SELECT * FROM FridgeTable WHERE temperature=?", (int(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))
            print(row)

        def openFridgeSearchMenu():
            window_Fridges.destroy()
            MainFridge_Window()


        backButton = tk.Button(window_Fridges, text = 'Back to Search Menu', command = openFridgeSearchMenu).grid(column=1)

        window_Fridges.mainloop()
        c.close()
        conn.close()
	
#----------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------
def OpenNumShelvesSearch(searchField):
    conn = sqlite3.connect('Test.db')
    c = conn.cursor()

    window_Fridges = tk.Tk()
    window_Fridges.title("FRIDGES")

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'WidthShelves')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=7)

    c.execute("SELECT * FROM FridgeTable WHERE numShelves=?", (int(searchField),))

    for row in c.fetchall():
        tree.insert("", "end", values = (row))
        print(row)

    def openFridgeSearchMenu():
        window_Fridges.destroy()
        MainFridge_Window()
        

    backButton = tk.Button(window_Fridges, text = 'Back to Search Menu', command = openFridgeSearchMenu).grid(row=5, column=1)

    window_Fridges.mainloop()
    c.close()
    conn.close()

#----------------------------------------------------------------------------------------
