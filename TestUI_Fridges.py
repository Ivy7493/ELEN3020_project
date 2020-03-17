import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI
import TestUI_MAIN

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

##########---------->START: WINDOW FOR ADDING FRIDGES<----------##########
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

    def Open_MainFridge_Window():
        window_AddFridge.destroy()
        MainFridge_Window()

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
    tk.Button(window_AddFridge, text = 'Back to Fridge Menu', 
                        command = Open_MainFridge_Window).grid(row = 10, column=1)

    window_AddFridge.mainloop()
##########---------->END: MAIN WINDOW FOR ADDING FRIDGES<----------##########


##########---------->START: WINDOW FOR DELETING FRIDGES<----------##########
def DeleteFridge_Window():
    def DeleteFridge():
        try:
            _fridgeID = fridgeID.get()
            print("HAVEN'T MADE DELETE FUNCTION YET")
        except:
            print("ERROR: Invalid data entered")

    def Open_MainFridge_Window():
        window_DeleteFridge.destroy()
        MainFridge_Window()

    window_DeleteFridge = tk.Tk()
    #window_DeleteFridge.geometry("300x300")
    window_DeleteFridge.title("DELETE FRIDGE")

    tk.Label(window_DeleteFridge, text = "Delete fridge with FridgeID: ").grid(row = 0)
    fridgeID = tk.Entry(window_DeleteFridge)
    fridgeID.grid(row = 0, column = 1)

    tk.Label(window_DeleteFridge, text = "From fridge with FridgeID: ").grid(row = 1)
    fridgeID = tk.Entry(window_DeleteFridge)
    fridgeID.grid(row = 1, column = 1)

    tk.Button(window_DeleteFridge, text = 'Delete Fridge', command = DeleteFridge).grid(row = 5, column=1)
    tk.Button(window_DeleteFridge, text = 'Back to Fridge Menu', 
                        command = Open_MainFridge_Window).grid(row = 10, column=1)

    window_DeleteFridge.mainloop()
##########---------->END: WINDOW FOR DELETING FRIDGES<----------##########

##########---------->START: MAIN WINDOW FOR FRIDGES<----------##########
def MainFridge_Window():
    window_MainFridge = tk.Tk()
    window_MainFridge.geometry("300x300")
    window_MainFridge.title("FRIDGE MENU")

    def Open_AddFridge_Window():
        window_MainFridge.destroy()
        AddFridge_Window()

    def Open_DeleteFridge_Window():
        window_MainFridge.destroy()
        DeleteFridge_Window()

    def Open_MainMenu_Window():
        window_MainFridge.destroy()
        TestUI_MAIN.Main_Window()

    tk.Button(window_MainFridge, text = 'Add Fridge', 
                        command = Open_AddFridge_Window).grid(row = 0, column=0)
    tk.Button(window_MainFridge, text = 'Delete Fridge', 
                        command = Open_DeleteFridge_Window).grid(row = 2, column=0)
    tk.Button(window_MainFridge, text = 'Back to Main Menu', 
                        command = Open_MainMenu_Window).grid(row = 3, column=0)

    window_MainFridge.mainloop()
##########---------->END: MAIN WINDOW FOR BOXES<----------##########


#SetupAPI.CreateAllTables(conn)   
#MainFridge_Window()
  





