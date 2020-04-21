import sqlite3
import tkinter as tk
from tkinter import ttk

def OpenAllBoxes(conn):
	c = conn.cursor()
	
	window_Boxes = tk.Tk()
	window_Boxes.title("BOXES")
	
	cols = ('Box ID', 'Fridge ID', 'Fridge X', 'Fridge Y', 'Box X', 'Box Y', 'Box Z')
	tree = ttk.Treeview(window_Boxes, columns=cols, show='headings')
	for col in cols:
		tree.heading(col, text=col)
	tree.grid(row=2, column=0, columnspan=7)
	
	c.execute("SELECT * FROM BoxTable")
	
	for row in c.fetchall():
		tree.insert("", "end", values = (row))
		
	def openBoxSearchMenu():
		window_Boxes.destroy()
		
	backButton = tk.Button(window_Boxes, text = 'Close', command = openBoxSearchMenu).grid(row=5, column=1)
	
	window_Boxes.mainloop()
	
#----------------------------------------------------------------------------------------
def OpenBoxIDSearch(conn, searchField):
    c = conn.cursor()

    if searchField == "":
        message_window = tk.Tk()
        message_window.title("ERROR")
        message = tk.Label(message_window, text = "That is not a valid Box ID")
        message.grid(row = 0, column = 0)

        def openBoxSearchMenu():
            message_window.destroy()

        backButton = tk.Button(message_window, text = 'Close', command = openBoxSearchMenu).grid(row=1)

    else:
        window_Boxes = tk.Tk()
        window_Boxes.title("BOXES")

        cols = ('Box ID', 'Fridge ID', 'Fridge X', 'Fridge Y', 'Box X', 'Box Y', 'Box Z')
        tree = ttk.Treeview(window_Boxes, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
        tree.grid(row=2, column=0, columnspan=7)

        c.execute("SELECT * FROM BoxTable WHERE BoxID=?", (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openBoxSearchMenu():
            window_Boxes.destroy()

        backButton = tk.Button(window_Boxes, text = 'Close', command = openBoxSearchMenu).grid(row=5, column=1)
        
        window_Boxes.mainloop()
#----------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------
def OpenFridgeIDSearch(conn, searchField):
    c = conn.cursor()

    if searchField == "":
        message_window = tk.Tk()
        message_window.title("ERROR")
        message = tk.Label(message_window, text = "That is not a valid Fridge ID")
        message.grid(row = 0, column = 0)

        def openBoxSearchMenu():
            message_window.destroy()

        backButton = tk.Button(message_window, text = 'Close', command = openBoxSearchMenu).grid(row=1)

    else:
        window_Boxes = tk.Tk()
        window_Boxes.title("BOXES")

        cols = ('Box ID', 'Fridge ID', 'Fridge X', 'Fridge Y', 'Box X', 'Box Y', 'Box Z')
        tree = ttk.Treeview(window_Boxes, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
        tree.grid(row=2, column=0, columnspan=7)

        c.execute("SELECT * FROM BoxTable WHERE FridgeID=?", (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openBoxSearchMenu():
            window_Boxes.destroy()

        backButton = tk.Button(window_Boxes, text = 'Close', command = openBoxSearchMenu).grid(row=5, column=1)
        
        window_Boxes.mainloop()
#----------------------------------------------------------------------------------------

