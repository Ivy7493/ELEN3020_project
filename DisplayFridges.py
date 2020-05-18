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

    text = tk.Text(window_Fridges)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    cols = ('Fridge ID', 'Temperature', 'NumShelves', 'WidthShelves', 'Rate')
    tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=0, column=0, columnspan=5)

    tree.column("Frdige ID", minwidth=0, width=100, strecth=tk.NO )
    tree.column("Temperature", minwidth=0, width=100, strecth=tk.NO )
    tree.column("NumShelves", minwidth=0, width=100, strecth=tk.NO)
    tree.column("WidthShelves", minwidth=0, width=100, strecth=tk.NO)
    tree.column("Rate", minwidth=0, width=100, strecth=tk.NO)

    c.execute("SELECT * FROM FridgeTable")

    for row in c.fetchall():
        tree.insert("", "end", values = (row))

    def openFridgeSearchMenu():
        window_Fridges.destroy()

    backButton = tk.Button(window_Fridges, text = 'Close', command = openFridgeSearchMenu, font = myFont).grid(row=5, column=1)
    
    window_Fridges.mainloop()
#----------------------------------------------------------------------------------------
    

#----------------------------------------------------------------------------------------
def OpenFridgeSearch(conn, searchField, searchColumn):
    c = conn.cursor()

    c.execute('''SELECT * FROM FridgeTable WHERE ''' + searchColumn + '''=?''', (str(searchField),))
    result = c.fetchone()

    if searchField == "":
        MessagePopup("Search field is missing data", "ERROR")

    elif result is None:
        MessagePopup("There are no results for that search", "ERROR")

    else:
        window_Fridges = tk.Tk()
        window_Fridges.title("FRIDGES")

        text = tk.Text(window_Fridges)
        myFont = Font(family="fixedsys", size=12)
        text.configure(font=myFont)

        cols = ('Fridge ID', 'Temperature', 'NumShelves', 'WidthShelves', 'Rate')
        tree = ttk.Treeview(window_Fridges, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
        tree.grid(row=0, column=0, columnspan=5)

        tree.column("Frdige ID", minwidth=0, width=110, strecth=tk.NO )
        tree.column("Temperature", minwidth=0, width=110, strecth=tk.NO )
        tree.column("NumShelves", minwidth=0, width=110, strecth=tk.NO)
        tree.column("WidthShelves", minwidth=0, width=110, strecth=tk.NO)
        tree.column("Rate", minwidth=0, width=110, strecth=tk.NO)

        c.execute('''SELECT * FROM FridgeTable WHERE ''' + searchColumn + '''=?''', (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openFridgeSearchMenu():
            window_Fridges.destroy()
            

        backButton = tk.Button(window_Fridges, text = 'Close', command = openFridgeSearchMenu, font = myFont).grid(row=5, column=1)
        
        window_Fridges.mainloop()
#----------------------------------------------------------------------------------------
