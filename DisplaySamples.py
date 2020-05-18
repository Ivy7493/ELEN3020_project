import sqlite3
import textwrap
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
import DataAPI

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


def OpenAllSamples(conn):
    c = conn.cursor()

    window_Samples = tk.Tk()
    window_Samples.title("SAMPLES")

    text = tk.Text(window_Samples)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    cols = ('ID', 'Box ID', 'X', 'Y' , 'Z', 'Type', 'Origin Country', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
    tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text = col)
    tree.grid(row=0, column=0, columnspan=16)

    tree.column("ID", minwidth=0, width=40, stretch=tk.NO)
    tree.column("Box ID", minwidth=0, width=65, stretch=tk.NO)
    tree.column("X", minwidth=0, width=30, stretch=tk.NO)
    tree.column("Y", minwidth=0, width=30, stretch=tk.NO)
    tree.column("Z", minwidth=0, width=30, stretch=tk.NO)
    tree.column("Type", minwidth=0, width=50, stretch=tk.NO)
    tree.column("Origin Country", minwidth=0, width=120, stretch=tk.NO)
    tree.column("Collection Date", minwidth=0, width=128, stretch=tk.NO)
    tree.column("Entry Date", minwidth=0, width=85, stretch=tk.NO)
    tree.column("Subject Age", minwidth=0, width=100, stretch=tk.NO)
    tree.column("Tube Rating", minwidth=0, width=100, stretch=tk.NO)
    tree.column("Collection Title", minwidth=0, width=130, stretch=tk.NO)
    tree.column("Return Type", minwidth=0, width=100, stretch=tk.NO)
    tree.column("Return Date", minwidth=0, width=100, stretch=tk.NO)
    tree.column("Phenotype Value", minwidth=0, width=130, stretch=tk.NO)
    tree.column("Disease State", minwidth=0, width=105, stretch=tk.NO)

    c.execute("SELECT * FROM SampleTable")

    for row in c.fetchall():
        tree.insert("", "end", values = (row))

    def openSampleSearchMenu():
        window_Samples.destroy()

    backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu, font = myFont).grid(row=5, column=1)

    window_Samples.mainloop()



def OpenSampleSearch(conn, searchField, searchColumn):
    c = conn.cursor()
    c.execute('''SELECT * FROM SampleTable WHERE ''' + searchColumn + ''' =?''', (str(searchField),))
    result = c.fetchone()

    if searchField == "":
        MessagePopup("Search field is missing data", "ERROR")

    elif result is None:
        MessagePopup("There are no results for that search", "ERROR")

    else:
        window_Samples = tk.Tk()
        window_Samples.title("SAMPLES")

        text = tk.Text(window_Samples)
        myFont = Font(family="fixedsys", size=12)
        text.configure(font=myFont)

        cols = ('ID', 'Box ID', 'X', 'Y' , 'Z', 'Type', 'Origin Country', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
        tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text = col)
        tree.grid(row=0, column = 0, columnspan=16)

        tree.column("ID", minwidth=0, width=40, stretch=tk.NO)
        tree.column("Box ID", minwidth=0, width=65, stretch=tk.NO)
        tree.column("X", minwidth=0, width=30, stretch=tk.NO)
        tree.column("Y", minwidth=0, width=30, stretch=tk.NO)
        tree.column("Z", minwidth=0, width=30, stretch=tk.NO)
        tree.column("Type", minwidth=0, width=50, stretch=tk.NO)
        tree.column("Origin Country", minwidth=0, width=120, stretch=tk.NO)
        tree.column("Collection Date", minwidth=0, width=128, stretch=tk.NO)
        tree.column("Entry Date", minwidth=0, width=85, stretch=tk.NO)
        tree.column("Subject Age", minwidth=0, width=100, stretch=tk.NO)
        tree.column("Tube Rating", minwidth=0, width=100, stretch=tk.NO)
        tree.column("Collection Title", minwidth=0, width=130, stretch=tk.NO)
        tree.column("Return Type", minwidth=0, width=100, stretch=tk.NO)
        tree.column("Return Date", minwidth=0, width=100, stretch=tk.NO)
        tree.column("Phenotype Value", minwidth=0, width=130, stretch=tk.NO)
        tree.column("Disease State", minwidth=0, width=105, stretch=tk.NO)

        c.execute('''SELECT * FROM SampleTable WHERE ''' + searchColumn + ''' =?''', (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openSampleSearchMenu():
            window_Samples.destroy()

        backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu, font = myFont).grid(row=5, column=1)

        window_Samples.mainloop() 


def OpenSampleFridgeSearch(conn, fridgeID):
    c = conn.cursor()
    result = DataAPI.IsFridgeEmpty(conn, fridgeID)

    if fridgeID == "":
        MessagePopup("Search field is missing data", "ERROR")

    elif result == "FALSE":
        messageText = "Fridge " + fridgeID + " is empty"
        MessagePopup(messageText , "ERROR")

    else:
        window_Samples = tk.Tk()
        window_Samples.title("SAMPLES")

        text = tk.Text(window_Samples)
        myFont = Font(family="fixedsys", size=12)
        text.configure(font=myFont)

        cols = ('ID', 'Box ID', 'X', 'Y' , 'Z', 'Type', 'Origin Country', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
        tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text = col)
        tree.grid(row=0, column = 0, columnspan=16)

        tree.column("ID", minwidth=0, width=40, stretch=tk.NO)
        tree.column("Box ID", minwidth=0, width=65, stretch=tk.NO)
        tree.column("X", minwidth=0, width=30, stretch=tk.NO)
        tree.column("Y", minwidth=0, width=30, stretch=tk.NO)
        tree.column("Z", minwidth=0, width=30, stretch=tk.NO)
        tree.column("Type", minwidth=0, width=50, stretch=tk.NO)
        tree.column("Origin Country", minwidth=0, width=120, stretch=tk.NO)
        tree.column("Collection Date", minwidth=0, width=128, stretch=tk.NO)
        tree.column("Entry Date", minwidth=0, width=85, stretch=tk.NO)
        tree.column("Subject Age", minwidth=0, width=100, stretch=tk.NO)
        tree.column("Tube Rating", minwidth=0, width=100, stretch=tk.NO)
        tree.column("Collection Title", minwidth=0, width=130, stretch=tk.NO)
        tree.column("Return Type", minwidth=0, width=100, stretch=tk.NO)
        tree.column("Return Date", minwidth=0, width=100, stretch=tk.NO)
        tree.column("Phenotype Value", minwidth=0, width=130, stretch=tk.NO)
        tree.column("Disease State", minwidth=0, width=105, stretch=tk.NO)

        c.execute("SELECT * FROM SampleTable")
        for result in c.fetchall():
            if DataAPI.ReturnFridgeSampleIn(conn, result[0]) == fridgeID:
                tree.insert("", "end", values = (result))

        def openSampleSearchMenu():
            window_Samples.destroy()

        backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu, font = myFont).grid(row=5, column=1)

        window_Samples.mainloop() 


