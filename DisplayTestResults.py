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

def OpenAllTestResults(conn):
    c = conn.cursor()

    window_TestResults = tk.Tk()
    window_TestResults.title("TEST RESULTS")

    text = tk.Text(window_TestResults)
    myFont = Font(family="fixedsys",size= 12)
    text.configure(font=myFont)

    cols = ('Sample ID', 'Test Type', 'Test Result')
    tree = ttk.Treeview(window_TestResults, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=3)

    c.execute("SELECT * FROM SampleTestTable")

    for row in c.fetchall():
        tree.insert("", "end", values = (row))

    def openTestResultSearchMenu():
        window_TestResults.destroy()

    backButton = tk.Button(window_TestResults, text = 'Close', command = openTestResultSearchMenu, font = myFont).grid(row=5, column=1)
    
    window_TestResults.mainloop()
#----------------------------------------------------------------------------------------
    

#----------------------------------------------------------------------------------------
def OpenTestResultSearch(conn, searchField, searchColumn):
    c = conn.cursor()

    if searchField == "":
        MessagePopup("That is not valid", "ERROR")

    else:
        window_TestResults = tk.Tk()
        window_TestResults.title("TEST RESULTS")

        text = tk.Text(window_TestResults)
        myFont = Font(family="fixedsys",size= 12)
        text.configure(font=myFont)

        cols = ('Sample ID', 'Test Type', 'Test Result')
        tree = ttk.Treeview(window_TestResults, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text=col)
        tree.grid(row=2, column=0, columnspan=3)

        c.execute('''SELECT * FROM SampleTestTable WHERE ''' + searchColumn + '''=?''', (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openTestResultSearchMenu():
            window_TestResults.destroy()
            

        backButton = tk.Button(window_TestResults, text = 'Close', command = openTestResultSearchMenu, font = myFont).grid(row=5, column=1)
        
        window_TestResults.mainloop()
#----------------------------------------------------------------------------------------
