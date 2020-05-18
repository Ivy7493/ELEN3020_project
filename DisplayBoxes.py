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

def OpenAllBoxes(conn):
    c = conn.cursor()
	
    window_Boxes = tk.Tk()
    window_Boxes.title("BOXES")

    text = tk.Text(window_Boxes)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)
	
    cols = ('Box ID', 'Fridge ID', 'Fridge X', 'Fridge Y', 'Box X', 'Box Y', 'Box Z')
    tree = ttk.Treeview(window_Boxes, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=7)

    tree.column("Box ID", minwidth=0, width=65, stretch=tk.NO)
    tree.column("Fridge ID", minwidth=0, width=80, stretch=tk.NO)
    tree.column("Fridge X", minwidth=0, width=75, stretch=tk.NO)
    tree.column("Fridge Y", minwidth=0, width=75, stretch=tk.NO)
    tree.column("Box X", minwidth=0, width=65, stretch=tk.NO)
    tree.column("Box Y", minwidth=0, width=65, stretch=tk.NO)
    tree.column("Box Z", minwidth=0, width=65, stretch=tk.NO)
    
	
    c.execute("SELECT * FROM BoxTable")
	
    for row in c.fetchall():
        tree.insert("", "end", values = (row))
		
    def openBoxSearchMenu():
        window_Boxes.destroy()
		
    backButton = tk.Button(window_Boxes, text = 'Close', command = openBoxSearchMenu, font = myFont).grid(row=5, column=1)
	
    window_Boxes.mainloop()
	
#----------------------------------------------------------------------------------------
def OpenBoxSearch(conn, searchField, searchColumn):
    c = conn.cursor()
    c.execute('''SELECT * FROM BoxTable WHERE ''' + searchColumn + ''' =?''', (str(searchField),))
    result = c.fetchone()

    if searchField == "":
        MessagePopup("Search field is missing data", "ERROR")

    elif result is None:
        MessagePopup("There are no results for that search", "ERROR")

    else:
        window_Boxes = tk.Tk()
        window_Boxes.title("BOXES")

        text = tk.Text(window_Boxes)
        myFont = Font(family="fixedsys", size=12)
        text.configure(font=myFont)

        cols = ('Box ID', 'Fridge ID', 'Fridge X', 'Fridge Y', 'Box X', 'Box Y', 'Box Z')
        tree = ttk.Treeview(window_Boxes, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
        tree.grid(row=2, column=0, columnspan=7)
   
        tree.column("Box ID", minwidth=0, width=65, stretch=tk.NO)
        tree.column("Fridge ID", minwidth=0, width=80, stretch=tk.NO)
        tree.column("Fridge X", minwidth=0, width=75, stretch=tk.NO)
        tree.column("Fridge Y", minwidth=0, width=75, stretch=tk.NO)
        tree.column("Box X", minwidth=0, width=65, stretch=tk.NO)
        tree.column("Box Y", minwidth=0, width=65, stretch=tk.NO)
        tree.column("Box Z", minwidth=0, width=65, stretch=tk.NO)

        c.execute('''SELECT * FROM BoxTable WHERE ''' + searchColumn + ''' =?''', (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openBoxSearchMenu():
            window_Boxes.destroy()

        backButton = tk.Button(window_Boxes, text = 'Close', command = openBoxSearchMenu, font = myFont).grid(row=5, column=1)
        
        window_Boxes.mainloop()
#----------------------------------------------------------------------------------------

