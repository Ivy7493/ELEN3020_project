import DatabasesAPI
import sqlite3
from tkinter import *

def GetFridgeInfo():
    _FridgeID = FridgeIDUI.get()
    _MaxBoxes = MaxBoxesUI.get()
    _Temperature = TemperatureUI.get()
    DatabasesAPI.AddFridge(conn,_FridgeID,_MaxBoxes,_Temperature)

#This is for testing the back end. DO NOT EDIT OR REMOVE
conn = DatabasesAPI.ConnectDatabase()
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")
#DatabasesAPI.CreateFridgeTable(conn)
#DatabasesAPI.CreateBoxTable(conn)
DatabasesAPI.AddBox(conn, "DXD", "ADC", 10)
DatabasesAPI.IsFridgeFull(conn, 'ABC')
DatabasesAPI.PrintBoxTable(conn)
print(DatabasesAPI.ReturnNumberOfFridges(conn))
DatabasesAPI.PrintFridgeTable(conn)
win = Tk()
MainTitle = Label(win,text="Back end testing UI!")
MainTitle.grid(row=0,column=1)
Connect = Button(win,text="Connect to Database",command=DatabasesAPI.ConnectDatabase)
Connect.grid(row=1,column=1)
FridgeIDUI = Entry(win)
MaxBoxesUI = Entry(win)
TemperatureUI = Entry(win)
FridgeIDUI.grid(row=3,column=0)
MaxBoxesUI.grid(row=3,column=1)
TemperatureUI.grid(row=3,column=2)
FridgeIDLabel = Label(win,text="Enter Fridge ID")
MaxBoxesLabel = Label(win,text="Enter max boxes")
TemperatureLabel = Label(win,text="Enter Fridge Temp")
FridgeIDLabel.grid(row=2,column=0)
MaxBoxesLabel.grid(row=2,column=1)
TemperatureLabel.grid(row=2,column=2)
SubmitFridge = Button(win,text="Add Fridge",command=GetFridgeInfo)
SubmitFridge.grid(row=4,column=1)



win.mainloop()
