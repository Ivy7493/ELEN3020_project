import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

##########---------->START: MESSAGE POPUP<--------------------##########
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
##########---------->END: MESSAGE POPUP<--------------------##########

##########---------->START: DISPLAY COLLECTIONS<--------------------##########
def OpenAllCollections(conn):
    c = conn.cursor()

    window_Collections = tk.Tk()
    window_Collections.title("COLLECTIONS")

    cols = ('Collection Title', 'Donor ID', 'Client Name', 'Client Phone Number', 'Client Email', 'Client Organization', 'Street Address', 'City', 'Country', 'Postal Code')
    tree = ttk.Treeview(window_Collections, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=9)

    c.execute("SELECT * FROM CollectionTable")

    for row in c.fetchall():
        tree.insert("", "end", values = (row))

    def openCollectionSearchMenu():
        window_Collections.destroy()

    backButton = tk.Button(window_Collections, text = 'Close', command = openCollectionSearchMenu).grid(row=5, column=1)
    
    window_Collections.mainloop()
##########---------->END: DISPLAY COLLECTIONS<--------------------##########
    
##########---------->START: COLLECTION SEARCH<--------------------##########
def OpenCollectionSearch(conn, searchField, searchColumn):
    c = conn.cursor()

    if searchField == "":
        MessagePopup("That is not valid", "ERROR")

    else:
        window_Collections = tk.Tk()
        window_Collections.title("COLLECTIONS")

        cols = ('Collection Title', 'Donor ID', 'Client Name', 'Client Phone Number', 'Client Email', 'Client Organization', 'Street Address', 'City', 'Country', 'Postal Code')
        tree = ttk.Treeview(window_Collections, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
        tree.grid(row=2, column=0, columnspan=9)

        c.execute('''SELECT * FROM CollectionTable WHERE ''' + searchColumn + '''=?''', (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openCollectionSearchMenu():
            window_Collections.destroy()
            

        backButton = tk.Button(window_Collections, text = 'Close', command = openCollectionSearchMenu).grid(row=5, column=1)
        
        window_Collections.mainloop()
##########---------->END: COLLECTION SEARCH<--------------------##########
