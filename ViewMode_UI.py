import sqlite3
import tkinter as tk
import textwrap
import math
from tkinter import * 
from tkinter import ttk
from tkinter.font import Font
import Main_UI
import DisplayTestResults

def ViewSamples(conn, _boxID, _fridgeID, _collectionTitle):
    c = conn.cursor()
    window_ViewSamples = Tk()
    window_ViewSamples.title("VIEW SAMPLES")
    
    text = tk.Text(window_ViewSamples)
    myFont = Font(family="fixedsys",size= 12)
    text.configure(font=myFont)

    cols = ('ID', 'Box ID', 'X', 'Y' , 'Z', 'Type', 'Origin Country', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
    tree = ttk.Treeview(window_ViewSamples, columns=cols, show='headings')
    for col in cols:
        tree.heading(col, text=col)
    tree.grid(row=0, column=0, columnspan=16)#, rowspan = 2)

    tree.column("Sample ID", minwidth=0, width=80, stretch=NO)
    tree.column("Box ID", minwidth=0, width=65, stretch=NO)
    tree.column("X", minwidth=0, width=30, stretch=NO)
    tree.column("Y", minwidth=0, width=30, stretch=NO)
    tree.column("Z", minwidth=0, width=30, stretch=NO)
    tree.column("Sample Type", minwidth=0, width=75, stretch=NO)
    tree.column("Origin Country", minwidth=0, width=100, stretch=NO)
    tree.column("Collection Date", minwidth=0, width=100, stretch=NO)
    tree.column("Entry Date", minwidth=0, width=100, stretch=NO)
    tree.column("Subject Age", minwidth=0, width=100, stretch=NO)
    tree.column("Tube Rating", minwidth=0, width=75, stretch=NO)
    tree.column("Collection Title", minwidth=0, width=100, stretch=NO)
    tree.column("Return Type", minwidth=0, width=75, stretch=NO)
    tree.column("Return Date", minwidth=0, width=100, stretch=NO)
    tree.column("Phenotype Value", minwidth=0, width=100, stretch=NO)
    tree.column("Disease State", minwidth=0, width=100, stretch=NO)

    if _collectionTitle == "FALSE":
        c.execute("SELECT * FROM SampleTable WHERE boxID=?", (str(_boxID),))
        results = c.fetchall()
    else:
        c.execute("SELECT * FROM SampleTable WHERE boxID=? AND collectionTitle = ?", (str(_boxID), str(_collectionTitle),))
        results = c.fetchall()
    
    sampleList = []
    count = 0

    for result in results:
        tree.insert("", "end", values = result)
        sampleList.append(result)
        count = count + 1

    def SampleTestClick(s):
        DisplayTestResults.OpenTestResultSearch(conn, s[0], "sampleID")

    if count!=0:
        count2 = 0
        sampleTestLabel = Label(text = "TEST RESULTS:").grid(column = count2, row = count)
        for indx, s in enumerate(sampleList):
            cmd = lambda _s=s: SampleTestClick(_s)
            c.execute("SELECT * FROM SampleTestTable WHERE sampleID = ?", (s[0],))
            result = c.fetchone()
            if result is None:
                pass
            else:    
                count2 = count2 + 1 
                sampleTestButton = Button(text=s[0], command=cmd, height = 1, font=myFont)
                sampleTestButton.grid(column = count2, row = count, sticky = tk.N)

    def OpenViewBoxes():
        window_ViewSamples.destroy()
        ViewBoxes(conn, _fridgeID, _collectionTitle)

    backButton = Button(window_ViewSamples, text="Return", command=OpenViewBoxes, font = myFont).grid(column=0)
    window_ViewSamples.mainloop()


def ViewBoxes(conn, _fridgeID, _collectionTitle):
    c = conn.cursor()

    window_ViewBoxes = tk.Tk()
    window_ViewBoxes.title("VIEW BOXES")
    window_ViewBoxes["bg"]='cadet blue'

    text = tk.Text(window_ViewBoxes)
    myFont = Font(family="fixedsys",size= 12)
    text.configure(font=myFont)

    fridgeID = "Fridge ID: " + str(_fridgeID)
    fridgeLabel = Label(text = fridgeID, bg = 'cadet blue', font = myFont, anchor = "w")
    fridgeLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "ew")

    c.execute("SELECT temperature FROM FridgeTable where fridgeID = ?", (_fridgeID,))
    fridgeTemp = "Temperature: " + str(c.fetchone()[0])
    fridgeLabel2 = Label(text = fridgeTemp, bg = 'cadet blue', font = myFont, anchor = "w")
    fridgeLabel2.grid(row = 1, column = 0, columnspan = 2, sticky = "ew")


    c.execute("SELECT * FROM BoxTable WHERE fridgeID = ?", (_fridgeID,))
    boxResults = c.fetchall()
    count = 0
    
    boxList = []

    def sampleLoop(boxID):
        c.execute("SELECT * FROM SampleTable WHERE boxID = ? AND collectionTitle = ?", (box[0], _collectionTitle,))
        
        sampleResults = c.fetchall()
        if sampleResults is None:
            pass
        else:
            return "TRUE"

    for box in boxResults:
        if _collectionTitle != "FALSE":
            if sampleLoop(box[0]) == "TRUE":
                count = count + 1
                boxList.append(box)
        else:
            count = count + 1
            boxList.append(box)

    rowCol = math.sqrt(count)
    myRow = 2
    myCol = 0

    def BoxClick(b):
        window_ViewBoxes.destroy()
        ViewSamples(conn, b[0], _fridgeID, _collectionTitle)

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
        ViewFridges(conn, _collectionTitle)

    tk.Label(window_ViewBoxes, height = 1, width = 2, bg="cadet blue").grid(column =0)
    backButton = Button(window_ViewBoxes, text="Return", command=OpenViewFridges, font = myFont).grid(columnspan = 3)
    tk.Label(window_ViewBoxes, height = 1, width = 2, bg="cadet blue").grid(column =2)
    window_ViewBoxes.mainloop()

def ViewFridges(conn, collectionTitle):
    c = conn.cursor()

    window_ViewFridges = tk.Tk()
    window_ViewFridges.title("VIEW FRIDGES")
    window_ViewFridges["bg"]='cadet blue'

    text = tk.Text(window_ViewFridges)
    myFont = Font(family="fixedsys",size= 12)
    text.configure(font=myFont)

    c.execute("SELECT * FROM FridgeTable")
    fridgeResults = c.fetchall()
    count = 0
    
    fridgeList = []

    def fridgeLoop(fridgeID):
        c.execute("SELECT * FROM BoxTable WHERE fridgeID = ?", (str(fridgeID),))
        boxResults = c.fetchall()
        for box in boxResults:
            c.execute("SELECT * FROM SampleTable WHERE boxID = ? AND collectionTitle = ?", (box[0], collectionTitle,))
            sampleResults = c.fetchall()
            if sampleResults is None:
                pass
            else:
                return "TRUE"
    
    for fridge in fridgeResults:
        if collectionTitle != "FALSE":
            if fridgeLoop(fridge[0]) == "TRUE":
                count = count + 1
                fridgeList.append(fridge)
        else:
            count = count + 1
            fridgeList.append(fridge)
    
    rowCol = math.sqrt(count)
    myRow = 0
    myCol = 0


    def FridgeClick(option):
        window_ViewFridges.destroy()
        ViewBoxes(conn, option[0], collectionTitle)

    for indx, f in enumerate(fridgeList):
        cmd = lambda _f=f: FridgeClick(_f)
        fridgeButton = Button(text=f[0], command=cmd, font=myFont)
        
        if myCol < rowCol:
            fridgeButton.grid(row = myRow, column = myCol, sticky=NSEW, padx=10, pady=10)
            myCol = myCol + 1
        else:
            myRow = myRow + 1
            myCol = 0
            fridgeButton.grid(row = myRow, column = myCol,sticky=NSEW, padx=10, pady=10)
            myCol = myCol + 1

    def Return():
        window_ViewFridges.destroy()
        Main_UI.Main_Window(conn)

    tk.Label(window_ViewFridges, height = 1, width = 2, bg="cadet blue").grid(column =0)
    backButton = Button(window_ViewFridges, text="Return", command=Return, font = myFont).grid(columnspan=3)
    tk.Label(window_ViewFridges, height = 1, width = 2, bg="cadet blue").grid(column =2)
    
    window_ViewFridges.mainloop()


