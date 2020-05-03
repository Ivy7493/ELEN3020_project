import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

def MessagePopup(messageText, messageTitle):
    message_window = tk.Tk()
    message_window.title(messageTitle)

    text = tk.Text(message_window)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    message_window["bg"] = 'cadet blue'
    message = tk.Label(message_window, text = messageText, font = myFont, bg = 'cadet blue')
    message.grid(row = 0, column = 0)

    def CloseMessage():
        message_window.destroy()

    backButton = tk.Button(message_window, text = 'Close', command = CloseMessage, font = myFont).grid(row=1) 

def OpenAllFridges(conn):
    c = conn.cursor()

    window_Fridges = tk.Tk()
    window_Fridges.title("FRIDGES")

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'WidthShelves', 'Rate')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=8)

    c.execute("SELECT * FROM FridgeTable")

    for row in c.fetchall():
        tree.insert("", "end", values = (row))

    def openFridgeSearchMenu():
        window_Fridges.destroy()

    backButton = tk.Button(window_Fridges, text = 'Close', command = openFridgeSearchMenu).grid(row=5, column=1)
    
    window_Fridges.mainloop()
#----------------------------------------------------------------------------------------
    

#----------------------------------------------------------------------------------------
def OpenFridgeSearch(conn, searchField, searchColumn):
    c = conn.cursor()

    if searchField == "":
        MessagePopup("That is not valid", "ERROR")

    else:
        window_Fridges = tk.Tk()
        window_Fridges.title("FRIDGES")

        cols = ('Fridge ID', 'Temperature', 'NumShelves', 'WidthShelves', 'Rate')
        tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
        tree.grid(row=2, column=0, columnspan=8)

        c.execute('''SELECT * FROM FridgeTable WHERE ''' + searchColumn + '''=?''', (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openFridgeSearchMenu():
            window_Fridges.destroy()
            

        backButton = tk.Button(window_Fridges, text = 'Close', command = openFridgeSearchMenu).grid(row=5, column=1)
        
        window_Fridges.mainloop()
#----------------------------------------------------------------------------------------
