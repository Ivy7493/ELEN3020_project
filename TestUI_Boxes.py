import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI

def CreateBox():
    try:
        _boxID = boxID.get()
        _fridgeID = fridgeID.get()
        _boxX = int(boxX.get())
        _boxY = int(boxY.get())
        _boxZ = int(boxZ.get())
        print(DataAPI.AddBox(conn, _boxID, _fridgeID, _boxX, _boxY, _boxZ))
    except:
        print("ERROR: Invalid data entered")
 
    

def console_PrintBox():
    print("Box ID: %s\nFridge ID: %s\nBox X: %s\nBox Y: %s\nBox Z: %s" % (boxID.get(), fridgeID.get(), boxX.get(), boxY.get(), boxZ.get()))
  

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

SetupAPI.CreateAllTables(conn)   
print(DataAPI.IsFridgeFull(conn, 'BCD')) 
print(DataAPI.MoveBox(conn, 'B1', 'TITS'))

window_AddBox = tk.Tk()
window_AddBox.geometry("300x300")
window_AddBox.title("ADD BOX")

#SETTING UP NEW FRIDGE FORM----------------------------------------------------------------
tk.Label(window_AddBox, text = "Box ID").grid(row = 0)
boxID = tk.Entry(window_AddBox)
boxID.grid(row = 0, column = 1)

tk.Label(window_AddBox, text = "Fridge ID").grid(row = 1)
fridgeID = tk.Entry(window_AddBox)
fridgeID.grid(row = 1, column = 1)

tk.Label(window_AddBox, text = "Box X").grid(row = 2)
boxX = tk.Entry(window_AddBox)
boxX.grid(row = 2, column = 1)

tk.Label(window_AddBox, text = "Box Y").grid(row = 3)
boxY = tk.Entry(window_AddBox)
boxY.grid(row = 3, column = 1)

tk.Label(window_AddBox, text = "Box Z").grid(row = 4)
boxZ = tk.Entry(window_AddBox)
boxZ.grid(row = 4, column = 1)

tk.Button(window_AddBox, text = 'Console Print', command = console_PrintBox).grid(row = 7, column=1)
tk.Button(window_AddBox, text = 'Populate', command = CreateBox).grid(row = 8, column=1)

window_AddBox.mainloop()



  





