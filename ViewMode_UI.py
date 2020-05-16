import sqlite3
import tkinter as tk
import textwrap
import math
from tkinter import * 
from tkinter import ttk
from tkinter.font import Font
import Main_UI

def ViewSamples(conn, _boxID, _fridgeID):
    c = conn.cursor()
    window_ViewSamples = Tk()
    window_ViewSamples.title("VIEW SAMPLES")
    
    cols = ('Sample ID', 'Box ID', 'X', 'Y' , 'Z', 'Sample Type', 'Origin Country', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
    tree = ttk.Treeview(window_ViewSamples, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=2, column=0, columnspan=16, rowspan = 2)

    tree.column("Sample ID", minwidth=0, width=90, stretch=NO)
    tree.column("Box ID", minwidth=0, width=65, stretch=NO)
    tree.column("X", minwidth=0, width=30, stretch=NO)
    tree.column("Y", minwidth=0, width=30, stretch=NO)
    tree.column("Z", minwidth=0, width=30, stretch=NO)
    tree.column("Sample Type", minwidth=0, width=105, stretch=NO)
    tree.column("Origin Country", minwidth=0, width=118, stretch=NO)
    tree.column("Collection Date", minwidth=0, width=130, stretch=NO)
    tree.column("Entry Date", minwidth=0, width=95, stretch=NO)
    tree.column("Subject Age", minwidth=0, width=100, stretch=NO)
    tree.column("Tube Rating", minwidth=0, width=105, stretch=NO)
    tree.column("Collection Title", minwidth=0, width=127, stretch=NO)
    tree.column("Return Type", minwidth=0, width=98, stretch=NO)
    tree.column("Return Date", minwidth=0, width=100, stretch=NO)
    tree.column("Phenotype Value", minwidth=0, width=132, stretch=NO)
    tree.column("Disease State", minwidth=0, width=110, stretch=NO)

    c.execute("SELECT * FROM SampleTable WHERE boxID=?", (str(_boxID),))

    for row in c.fetchall():
        tree.insert("", "end", values = row)

    def OpenViewBoxes():
        window_ViewSamples.destroy()
        ViewBoxes(conn, _fridgeID)

    backButton = Button(window_ViewSamples, text="Return", command=OpenViewBoxes).grid(column=0)
    window_ViewSamples.mainloop()


def ViewBoxes(conn, _fridgeID):
    c = conn.cursor()

    window_ViewBoxes = tk.Tk()
    window_ViewBoxes.title("VIEW BOXES")
    window_ViewBoxes["bg"]='cadet blue'

    text = tk.Text(window_ViewBoxes)
    myFont = Font(family="fixedsys",size= 12)
    text.configure(font=myFont)

    c.execute("SELECT * FROM BoxTable WHERE fridgeID = ?", (_fridgeID,))
    results = c.fetchall()
    count = 0
    
    boxList = []

    for result in results:
        count = count + 1
        boxList.append(result)
    
    rowCol = math.sqrt(count)
    
    myRow = 0
    myCol = 0

    def BoxClick(b):
        window_ViewBoxes.destroy()
        ViewSamples(conn, b[0], _fridgeID)
    

    for indx, b in enumerate(boxList):
        cmd = lambda _b=b: BoxClick(_b)
        boxButton = Button(text=b[0], command=cmd, font=myFont)

        if myCol < rowCol:
            boxButton.grid(row = myRow, column = myCol, sticky=NS, padx=10, pady=10)
            myCol = myCol + 1
        else:
            myRow = myRow + 1
            myCol = 0
            boxButton.grid(row = myRow, column = myCol, sticky=NS, padx=10, pady=10)
            myCol = myCol + 1

    def OpenViewFridges():
        window_ViewBoxes.destroy()
        ViewFridges(conn)

    backButton = Button(window_ViewBoxes, text="Return", command=OpenViewFridges).grid(column=0)
    window_ViewBoxes.mainloop()

def ViewFridges(conn):
    c = conn.cursor()

    window_ViewFridges = tk.Tk()
    window_ViewFridges.title("VIEW FRIDGES")
    window_ViewFridges["bg"]='cadet blue'

    text = tk.Text(window_ViewFridges)
    myFont = Font(family="fixedsys",size= 12)
    text.configure(font=myFont)

    c.execute("SELECT * FROM FridgeTable")
    results = c.fetchall()
    count = 0
    
    fridgeList = []

    for result in results:
        count = count + 1
        fridgeList.append(result)
    
    rowCol = math.sqrt(count)
    
    myRow = 0
    myCol = 0


    def FridgeClick(option):
        window_ViewFridges.destroy()
        ViewBoxes(conn, option[0])

    for indx, f in enumerate(fridgeList):
        cmd = lambda _f=f: FridgeClick(_f)
        fridgeButton = Button(text=f[0], command=cmd, font=myFont)
        #fridgeLabel = tk.Label(window_ViewFridges, text = "", width=1, height=1, bg='pink')
        #fridgeLabel2 = tk.Label(window_ViewFridges, text = "", width =1, height =1, bg='blue').grid(row = 0, column = 0)
        
        #if myCol!=0 and myRow!=0:
        if myCol < rowCol:
            fridgeButton.grid(row = myRow, column = myCol, sticky=NSEW, padx=10, pady=10)
            #fridgeLabel.grid(row=myRow, column=myCol)

            myCol = myCol + 1
        else:
            myRow = myRow + 1
            myCol = 0
            fridgeButton.grid(row = myRow, column = myCol,sticky=NSEW, padx=10, pady=10)
            #fridgeLabel.grid(row=myRow, column=myCol)
            myCol = myCol + 1

    def Return():
        window_ViewFridges.destroy()
        Main_UI.Main_Window(conn)

    backButton = Button(window_ViewFridges, text="Return", command=Return).grid(column=0)
    
    window_ViewFridges.mainloop()


