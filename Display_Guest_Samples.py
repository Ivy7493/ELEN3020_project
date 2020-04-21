import sqlite3
import tkinter as tk
from tkinter import ttk
import GuestLogin
import Startup

def FetchGuestSamples(conn, searchField):
    c = conn.cursor()

    window_Samples = tk.Tk()
    window_Samples.title("SAMPLES")

    def Log_Out():
        window_Samples.destroy()
        Startup.Start_Window(conn)

    tk.Button(window_Samples, text = 'Log Out', 
                        command = Log_Out).grid(row = 3, column=0)

    cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Origin Country', 'Collection Date', 'Entry Date', 'Sample History', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
    tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=20)
    c.execute("SELECT * FROM SampleTable WHERE collectionTitle=?", (str(searchField),))

    for row in c.fetchall():
        tree.insert("", "end", values = (row))

    window_Samples.mainloop()

