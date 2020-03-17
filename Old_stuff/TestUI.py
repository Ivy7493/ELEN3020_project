import DatabasesAPI
import sqlite3
from tkinter import *

def GetFridgeInfo():
    _FridgeID = FridgeIDUI.get()
    _MaxBoxes = MaxBoxesUI.get()
    _ShelfWidth = ShelfWidthUI.get()
    _Temperature = TemperatureUI.get()
    DatabasesAPI.AddFridge(conn,_FridgeID,_MaxBoxes,_ShelfWidth,_Temperature)

def GetBoxInfo():
    _FridgeID = FridgeIDBox.get()
    _BoxID = BoxIDUI.get()
    _MS = MS.get()
    DatabasesAPI.AddBox(conn, _BoxID, _FridgeID, _MS)

def PrintBoxTable():
    print("------------Box Table Entries-------------")
    print("Box Code | Fridge code | Max Samples")
    DatabasesAPI.PrintBoxTable(conn)

def PrintFridgeTable():
    print("-----------Fridge Table Entries-----------")
    print("Fridge Code | Max Boxes | Shelf Width| Temparture")
    DatabasesAPI.PrintFridgeTable(conn)

def MoveBox():
    _BoxID = MoveBoxID.get()
    _FridgeID = MoveBoxFridgeID.get()
    DatabasesAPI.MoveBox(conn, _BoxID, _FridgeID)

def CreateTables():
    DatabasesAPI.CreateBoxTable(conn)
    DatabasesAPI.CreateFridgeTable(conn)
    

#This is for testing the back end. DO NOT EDIT OR REMOVE
conn = DatabasesAPI.ConnectDatabase()
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")

#------------------UI SECTION----------------------#
win = Tk()
MainTitle = Label(win,text="Back end testing UI!")
MainTitle.grid(row=0,column=1)
Connect = Button(win,text="Click To make Database",command=CreateTables)
Connect.grid(row=1,column=1)
FridgeIDUI = Entry(win)
MaxBoxesUI = Entry(win)
ShelfWidthUI = Entry(win)
TemperatureUI = Entry(win)
FridgeIDUI.grid(row=3,column=0)
MaxBoxesUI.grid(row=3,column=1)
ShelfWidthUI.grid(row=3,column=2)
TemperatureUI.grid(row=3,column=3)
FridgeIDLabel = Label(win,text="Enter Fridge ID")
MaxBoxesLabel = Label(win,text="Enter max boxes")
ShelfWidthLabel = Label(win,text="Enter Shelf Width")
TemperatureLabel = Label(win,text="Enter Fridge Temp")
FridgeIDLabel.grid(row=2,column=0)
MaxBoxesLabel.grid(row=2,column=1)
ShelfWidthLabel.grid(row=2,column=2)
TemperatureLabel.grid(row=2,column=3)
SubmitFridge = Button(win,text="Add Fridge",command=GetFridgeInfo)
SubmitFridge.grid(row=4,column=1)
BoxIDUI = Entry(win)
BoxIDLabel = Label(win, text="Enter BoxID")
BoxIDUI.grid(row=6,column=0)
BoxIDLabel.grid(row=5,column=0)
FridgeIDBox = Entry(win)
FridgeIDLabelBox = Label(win,text="Enter FridgeID")
FridgeIDBox.grid(row=6,column=1)
FridgeIDLabelBox.grid(row=5,column=1)
MS = Entry(win)
MSLabel = Label(win,text="Max Samples")
MS.grid(row=6,column=2)
MSLabel.grid(row=5,column=2)
SubmitBox = Button(win,text="Create Box",command = GetBoxInfo)
SubmitBox.grid(row=7,column=1)
PrintBoxTableUI = Button(win,text="Print Box UI",command=PrintBoxTable)
PrintFridgeTableUI = Button(win,text="Print Fridge Table",command=PrintFridgeTable)
PrintBoxTableUI.grid(row=0,column=0)
PrintFridgeTableUI.grid(row=0,column=2)
MoveBoxID = Entry(win)
MoveBoxLabel = Label(win, text="Enter Box ID")
MoveBoxFridgeID = Entry(win)
MoveBoxFridgeLabel = Label(win,text="Destination Fridge ID")
SubmitMoveBox = Button(win,text="Move Box",command=MoveBox)
MoveBoxID.grid(row=9,column = 0)
MoveBoxLabel.grid(row=8,column=0)
MoveBoxFridgeID.grid(row=9, column=1)
MoveBoxFridgeLabel.grid(row=8, column=1)
SubmitMoveBox.grid(row=10, column=1)



win.mainloop()
