import DatabasesAPI
import sqlite3
from tkinter import *

#This is for testing the back end. DO NOT EDIT OR REMOVE
conn = DatabasesAPI.ConnectDatabase()
print(DatabasesAPI.CheckFridgeID(conn, "ABC"))
print(DatabasesAPI.ReturnNumberOfFridges(conn))
win = Tk()
MainTitle = Label(win,text="Back end testing UI!")
MainTitle.grid(row=0,column=1)
Connect = Button(win,text="Connect to Database",command=DatabasesAPI.ConnectDatabase)
Connect.grid(row=1,column=1)


win.mainloop()
