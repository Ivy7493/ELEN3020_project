import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import DisplayFridges
from tkinter import messagebox

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
            messagebox.showinfo("Add Fridge", DataAPI.AddFridge(
                conn, _fridgeID, _temperature, _numShelves, _widthShelves))
        except:
            messagebox.showinfo("Add Fridge", "ERROR: Invalid data entered")

    def console_PrintFridge():
        print("Fridge ID: %s\nTemperature: %s\nNumShelves: %s\nNumBoxes: %s" % (
            fridgeID.get(), temp.get(), numShelves.get(), widthShelves.get()))

    def Open_MainFridge_Window():
        window_AddFridge.destroy()
        MainFridge_Window()

    window_AddFridge = tk.Tk()
    window_AddFridge.geometry("300x300")
    window_AddFridge.title("ADD FRIDGE")

    tk.Label(window_AddFridge, text="Fridge ID").grid(row=0)
    fridgeID = tk.Entry(window_AddFridge)
    fridgeID.grid(row=0, column=1)

    tk.Label(window_AddFridge, text="Temperature").grid(row=1)
    temp = tk.Entry(window_AddFridge)
    temp.grid(row=1, column=1)

    tk.Label(window_AddFridge, text="Number of Shelves").grid(row=2)
    numShelves = tk.Entry(window_AddFridge)
    numShelves.grid(row=2, column=1)

    tk.Label(window_AddFridge, text="Number of Boxes").grid(row=3)
    widthShelves = tk.Entry(window_AddFridge)
    widthShelves.grid(row=3, column=1)

    tk.Button(window_AddFridge, text='Print to Console',
              command=console_PrintFridge).grid(row=7, column=1)
    tk.Button(window_AddFridge, text='Add Fridge',
              command=CreateFridge).grid(row=8, column=1)
    tk.Button(window_AddFridge, text='Back to Fridge Menu',
              command=Open_MainFridge_Window).grid(row=10, column=1)

    window_AddFridge.mainloop()
##########---------->END: MAIN WINDOW FOR ADDING FRIDGES<----------##########


##########---------->START: WINDOW FOR DELETING FRIDGES<----------##########
def DeleteFridge_Window():
    def DeleteFridge():
        _fridgeID = fridgeID.get()
        messagebox.showinfo(
            "Delete Fridge", DataAPI.DeleteFridge(conn, _fridgeID))

    def Open_MainFridge_Window():
        window_DeleteFridge.destroy()
        MainFridge_Window()

    window_DeleteFridge = tk.Tk()
    # window_DeleteFridge.geometry("300x300")
    window_DeleteFridge.title("DELETE FRIDGE")

    tk.Label(window_DeleteFridge,
             text="Delete fridge with FridgeID: ").grid(row=0)
    fridgeID = tk.Entry(window_DeleteFridge)
    fridgeID.grid(row=0, column=1)

    tk.Button(window_DeleteFridge, text='Delete Fridge',
              command=DeleteFridge).grid(row=5, column=1)
    tk.Button(window_DeleteFridge, text='Back to Fridge Menu',
              command=Open_MainFridge_Window).grid(row=10, column=1)

    window_DeleteFridge.mainloop()
##########---------->END: WINDOW FOR DELETING FRIDGES<----------##########

##########---------->START: WINDOW FOR SEARCHING FRIDGES<-------##########


def SearchFridge_Window():

    window_SearchFridge = tk.Tk()
    window_SearchFridge.title("SEARCH FRIDGE WINDOW")
    window_SearchFridge.geometry("300x300")
    window_SearchFridge["bg"] = 'pink'

    searchButton = tk.Button(window_SearchFridge, text='Display All Fridges',
                             command=DisplayFridges.OpenAllFridges).grid(row=1, column=2)

    searchField1 = tk.Entry(window_SearchFridge)
    searchField1.grid(row=2, column=1)

    def runDisplayFridges():
        DisplayFridges.OpenFridgeSearch(searchField1.get())
        print(searchField1.get())

    searchButton1 = tk.Button(window_SearchFridge, text='Search for FridgeID',
                              command=runDisplayFridges).grid(row=2, column=2)
    #---------------------------------------------------------------------------------

    searchField2 = tk.Entry(window_SearchFridge)
    searchField2.grid(row=3, column=1)

    def runDisplayTemperatures():
        DisplayFridges.OpenTemperatureSearch(searchField2.get())
        print(searchField2.get())

    searchButton2 = tk.Button(window_SearchFridge, text='Search for fridge temperature',
                              command=runDisplayTemperatures).grid(row=3, column=2)
    #---------------------------------------------------------------------------------

    searchField3 = tk.Entry(window_SearchFridge)
    searchField3.grid(row=4, column=1)

    def runDisplayShelves():
        DisplayFridges.OpenNumShelvesSearch(searchField3.get())
        print(searchField3.get())

    searchButton3 = tk.Button(window_SearchFridge, text='Search for number of shelves',
                              command=runDisplayShelves).grid(row=4, column=2)
    #---------------------------------------------------------------------------------

    window_SearchFridge.mainloop()
##########---------->END: WINDOW FOR SEARCHING FRIDGES<-------##########

##########---------->START: MAIN WINDOW FOR FRIDGES<----------##########


def MainFridge_Window():
    window_MainFridge = tk.Tk()
    window_MainFridge.geometry("300x300")
    window_MainFridge.title("FRIDGE MENU")

    def Open_SearchFridge_Window():
        window_MainFridge.destroy()
        SearchFridge_Window()

    def Open_AddFridge_Window():
        window_MainFridge.destroy()
        AddFridge_Window()

    def Open_DeleteFridge_Window():
        window_MainFridge.destroy()
        DeleteFridge_Window()

    def Open_MainMenu_Window():
        window_MainFridge.destroy()
        Main_UI.Main_Window()

    tk.Button(window_MainFridge, text='Add Fridge',
              command=Open_AddFridge_Window).grid(row=0, column=0)
    tk.Button(window_MainFridge, text='Delete Fridge',
              command=Open_DeleteFridge_Window).grid(row=2, column=0)
    tk.Button(window_MainFridge, text='Search Fridge',
              command=Open_SearchFridge_Window).grid(row=3, column=0)

    tk.Button(window_MainFridge, text='Back to Main Menu',
                  command=Open_MainMenu_Window).grid(row=4, column=0)

    window_MainFridge.mainloop()
##########---------->END: MAIN WINDOW FOR FRIDGES<----------##########


# SetupAPI.CreateAllTables(conn)
# MainFridge_Window()
