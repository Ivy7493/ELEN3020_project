import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

def AddFridge_Window():
    def CreateFridge():
        try:
            _fridgeID = fridgeID.get()
            _temperature = int(temp.get())
            _numShelves = int(numShelves.get())
            _widthShelves = int(widthShelves.get())
            print(DataAPI.AddFridge(conn, _fridgeID, _temperature, _numShelves, _widthShelves))
        except:
            print("ERROR: Invalid data entered")

    def console_PrintFridge():
        print("Fridge ID: %s\nTemperature: %s\nNumShelves: %s\nNumBoxes: %s" % (fridgeID.get(), temp.get(), numShelves.get(), widthShelves.get()))

    window_AddFridge = tk.Tk()
    window_AddFridge.geometry("300x300")
    window_AddFridge.title("ADD FRIDGE")

    tk.Label(window_AddFridge, text = "Fridge ID").grid(row = 0)
    fridgeID = tk.Entry(window_AddFridge)
    fridgeID.grid(row = 0, column = 1)

    tk.Label(window_AddFridge, text = "Temperature").grid(row = 1)
    temp = tk.Entry(window_AddFridge)
    temp.grid(row = 1, column = 1)

    tk.Label(window_AddFridge, text = "Number of Shelves").grid(row = 2)
    numShelves = tk.Entry(window_AddFridge)
    numShelves.grid(row = 2, column = 1)

    tk.Label(window_AddFridge, text = "Number of Boxes").grid(row = 3)
    widthShelves = tk.Entry(window_AddFridge)
    widthShelves.grid(row = 3, column = 1)

    tk.Button(window_AddFridge, text = 'Print to Console', command = console_PrintFridge).grid(row = 7, column=1)
    tk.Button(window_AddFridge, text = 'Add Fridge', command = CreateFridge).grid(row = 8, column=1)

    window_AddFridge.mainloop()

def MainFridge_Window():
    MainFridge_Window = tk.Tk()
    MainFridge_Window.geometry("300x300")
    MainFridge_Window.title("FRIDGE MENU")

    tk.Button(MainFridge_Window, text = 'Add Fridge', command = AddFridge_Window).grid(row = 0, column=0)
    #tk.Button(MainFridge_Window, text = 'Move Box', command = MoveBox_Window).grid(row = 1, column=0)
    #tk.Button(MainFridge_Window, text = 'Delete Box', command = DeleteBox_Window).grid(row = 2, column=0)

    MainFridge_Window.mainloop()


SetupAPI.CreateAllTables(conn)   
MainFridge_Window()


  





