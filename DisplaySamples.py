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


def OpenAllSamples(conn):
	c = conn.cursor()

	window_Samples = tk.Tk()
	window_Samples.title("SAMPLES")

	cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
	tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
	for col in cols:
		tree.heading(col, text = col)
	tree.grid(row=2, column = 0, columnspan=7)

	c.execute("SELECT * FROM SampleTable")

	for row in c.fetchall():
		tree.insert("", "end", values = (row))

	def openSampleSearchMenu():
		window_Samples.destroy()

	backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

	window_Samples.mainloop()



def OpenSampleSearch(conn, searchField, searchColumn):
    c = conn.cursor()

    if searchField == "":
        MessagePopup("That is not valid", "ERROR")

    else:
        window_Samples = tk.Tk()
        window_Samples.title("SAMPLES")

        cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
        tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
        for col in cols:
            tree.heading(col, text = col)
        tree.grid(row=2, column = 0, columnspan=7)

        c.execute('''SELECT * FROM SampleTable WHERE ''' + searchColumn + ''' =?''', (str(searchField),))

        for row in c.fetchall():
            tree.insert("", "end", values = (row))

        def openSampleSearchMenu():
            window_Samples.destroy()

        backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

        window_Samples.mainloop() 


