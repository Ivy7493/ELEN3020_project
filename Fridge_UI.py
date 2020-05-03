import SetupAPI
import sqlite3
import tkinter as tk
from tkinter.font import Font
import DataAPI
import Main_UI
import DisplayFridges
from tkinter import messagebox

def MessagePopup(messageText, messageTitle):
    message_window = tk.Tk()
    message_window.title(messageTitle)

    text = tk.Text(message_window)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    message_window["bg"] = 'cadet blue'
    message = tk.Label(message_window, text = messageText, font = myFont, bg = 'cadet blue')
    message.grid(row = 0, column = 0)

    def CloseMessage():
        message_window.destroy()

    backButton = tk.Button(message_window, text = 'Close', command = CloseMessage, font = myFont).grid(row=1) 


##########---------->START: WINDOW FOR ADDING FRIDGES<----------##########
def AddFridge_Window(conn):
    def CreateFridge():
        _fridgeID = fridgeID.get()
        _temperature = temp.get()
        _numShelves = numShelves.get()
        _widthShelves = widthShelves.get()
        _rate = rate.get()
        try:
            _temperature = int(_temperature)
            _numShelves = int(_numShelves)
            _widthShelves = int(_widthShelves)
            _rate = float(_rate)
            intCheck = "TRUE"
        except:
            intCheck = "FALSE"
        if any([_fridgeID == "", _temperature == "", _numShelves == "", _widthShelves == "", _rate == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        elif intCheck == "FALSE":
            MessagePopup("One or more fields are wrong data type", "ERROR")
        else:
            try:
                messageText = DataAPI.AddFridge(conn, _fridgeID, _temperature, _numShelves, _widthShelves, _rate)
                MessagePopup(messageText, "Add Fridge")
            except:
                MessagePopup("ERROR: Invalid data entered", "Add Fridge")

    def Open_MainFridge_Window():
        window_AddFridge.destroy()
        MainFridge_Window(conn)

    window_AddFridge = tk.Tk()
    window_AddFridge.title("ADD FRIDGE")
    window_AddFridge["bg"] = 'cadet blue'
    
    text = tk.Text(window_AddFridge)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_AddFridge, text="Fridge ID", bg = 'cadet blue', font=myFont, anchor = 'w').grid(row=1, column = 1, sticky = "ew")
    fridgeID = tk.Entry(window_AddFridge)
    fridgeID.grid(row=1, column=2, sticky="ew")

    tk.Label(window_AddFridge, text="Temperature", bg = 'cadet blue', font=myFont, anchor = 'w').grid(row=2, column = 1, sticky = "ew")
    temp = tk.Entry(window_AddFridge)
    temp.grid(row=2, column=2, sticky="ew")

    tk.Label(window_AddFridge, text="Number of Shelves", bg = 'cadet blue', font=myFont, anchor = 'w').grid(row=3, column = 1, sticky = "ew")
    numShelves = tk.Entry(window_AddFridge)
    numShelves.grid(row=3, column=2, sticky="ew")

    tk.Label(window_AddFridge, text="Number of Boxes", bg = 'cadet blue', font=myFont, anchor = 'w').grid(row=4, column = 1, sticky = "ew")
    widthShelves = tk.Entry(window_AddFridge)
    widthShelves.grid(row=4, column=2, sticky="ew")

    tk.Label(window_AddFridge, text="Monthly Rate (R)", bg = 'cadet blue', font=myFont, anchor = 'w').grid(row=5, column = 1, sticky = "ew")
    rate = tk.Entry(window_AddFridge)
    rate.grid(row=5, column=2, sticky="ew")

    tk.Button(window_AddFridge, text='Add Fridge', command=CreateFridge, font=myFont).grid(row=6, column=2, sticky="ew")
    tk.Button(window_AddFridge, text='Back to Fridge Menu', command=Open_MainFridge_Window, font=myFont).grid(row=8, column=2, sticky="ew")

    tk.Label(window_AddFridge, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_AddFridge, height = 1, width = 2, bg="cadet blue").grid(row =7, column =0)
    tk.Label(window_AddFridge, height = 1, width = 2, bg="cadet blue").grid(row =9, column =3)

    window_AddFridge.mainloop()
##########---------->END: MAIN WINDOW FOR ADDING FRIDGES<----------##########


##########---------->START: WINDOW FOR DELETING FRIDGES<----------##########
def DeleteFridge_Window(conn):
    def DeleteFridge():
        _fridgeID = fridgeID.get()
        messageText = DataAPI.DeleteFridge(conn, _fridgeID)
        MessagePopup(messageText, "Delete Fridge")

    def Open_MainFridge_Window():
        window_DeleteFridge.destroy()
        MainFridge_Window(conn)

    window_DeleteFridge = tk.Tk()
    window_DeleteFridge.title("DELETE FRIDGE")
    window_DeleteFridge["bg"] = 'cadet blue'
    
    text = tk.Text(window_DeleteFridge)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_DeleteFridge, text="Delete fridge with FridgeID: ", font=myFont, bg = 'cadet blue', anchor = "w").grid(row=1, column = 1, sticky = "ew")
    fridgeID = tk.Entry(window_DeleteFridge)
    fridgeID.grid(row=1, column=2, sticky = "ew")

    tk.Button(window_DeleteFridge, text='Delete Fridge', command=DeleteFridge, font=myFont).grid(row=2, column=2, sticky = "ew")
    tk.Button(window_DeleteFridge, text='Back to Fridge Menu', command=Open_MainFridge_Window, font=myFont).grid(row=4, column=2, sticky="ew")

    tk.Label(window_DeleteFridge, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_DeleteFridge, height = 1, width = 2, bg="cadet blue").grid(row =3, column =0)
    tk.Label(window_DeleteFridge, height = 1, width = 2, bg="cadet blue").grid(row =5, column =3)

    window_DeleteFridge.mainloop()
##########---------->END: WINDOW FOR DELETING FRIDGES<----------##########

##########---------->START: WINDOW FOR SEARCHING FRIDGES<-------##########
def SearchFridge_Window(conn):
    window_SearchFridge = tk.Tk()
    window_SearchFridge.title("SEARCH FRIDGE WINDOW")
    window_SearchFridge["bg"] = 'cadet blue'
    
    text = tk.Text(window_SearchFridge)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    #--------------------
    def OpenAllFridges():
        DisplayFridges.OpenAllFridges(conn)

    searchButton = tk.Button(window_SearchFridge, text='Display All Fridges', command=OpenAllFridges, font=myFont)
    searchButton.grid(row=1, column=2, sticky = "ew")
    #--------------------
    searchLabel1 = tk.Label(window_SearchFridge, text = 'Fridge ID:', anchor = "w", font=myFont, bg = 'cadet blue')
    searchLabel1.grid(row=3, column = 1, sticky = "ew")
    searchField1 = tk.Entry(window_SearchFridge)
    searchField1.grid(row=3, column=2, sticky = "ew")

    def runDisplayFridges():
        DisplayFridges.OpenFridgeSearch(conn, searchField1.get())

    searchButton1 = tk.Button(window_SearchFridge, text='Search', command=runDisplayFridges, font=myFont)
    searchButton1.grid(row=3, column=3, sticky = "ew")
    #--------------------
    searchLabel2 = tk.Label(window_SearchFridge, text = 'Fridge Temperature:', anchor = "w", font=myFont, bg = 'cadet blue')
    searchLabel2.grid(row=4, column = 1, sticky = "ew")
    searchField2 = tk.Entry(window_SearchFridge)
    searchField2.grid(row=4, column=2, sticky = "ew")

    def runDisplayTemperatures():
        DisplayFridges.OpenTemperatureSearch(conn, searchField2.get())

    searchButton2 = tk.Button(window_SearchFridge, text='Search', command=runDisplayTemperatures, font=myFont)
    searchButton2.grid(row=4, column=3, sticky = "ew")
    #--------------------
    searchLabel3 = tk.Label(window_SearchFridge, text = 'Number of Shelves:', font=myFont, bg = 'cadet blue', anchor = "w")
    searchLabel3.grid(row=5, column = 1, sticky = "ew")
    searchField3 = tk.Entry(window_SearchFridge)
    searchField3.grid(row=5, column=2, sticky = "ew")

    def runDisplayShelves():
        DisplayFridges.OpenNumShelvesSearch(conn, searchField3.get())

    searchButton3 = tk.Button(window_SearchFridge, text='Search', command=runDisplayShelves, font=myFont)
    searchButton3.grid(row=5, column=3, sticky = "ew")
    #--------------------
    def Open_MainMenu_Window():
        window_SearchFridge.destroy()
        MainFridge_Window(conn)

    returnButton = tk.Button(window_SearchFridge, text='Back to Fridge Menu', command=Open_MainMenu_Window, font=myFont)
    returnButton.grid(row=7, column=2, sticky = "ew")
    #--------------------

    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =6, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =8, column =4)

    window_SearchFridge.mainloop()
##########---------->END: WINDOW FOR SEARCHING FRIDGES<-------##########

##########---------->START: MAIN WINDOW FOR FRIDGES<----------##########
def MainFridge_Window(conn):
    window_MainFridge = tk.Tk()
    #window_MainFridge.geometry("300x225")
    window_MainFridge.title("FRIDGE MENU")
    window_MainFridge["bg"]='cadet blue'
    
    text = tk.Text(window_MainFridge)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)


    def Open_SearchFridge_Window():
        window_MainFridge.destroy()
        SearchFridge_Window(conn)

    def Open_AddFridge_Window():
        window_MainFridge.destroy()
        AddFridge_Window(conn)

    def Open_DeleteFridge_Window():
        window_MainFridge.destroy()
        DeleteFridge_Window(conn)

    def Open_MainMenu_Window():
        window_MainFridge.destroy()
        Main_UI.Edit_Window(conn)

    tk.Button(window_MainFridge, text='Add Fridge', command=Open_AddFridge_Window, font=myFont).grid(row=1, column=1, sticky="ew")
    tk.Button(window_MainFridge, text='Delete Fridge', command=Open_DeleteFridge_Window, font=myFont).grid(row=3, column=1, sticky="ew")
    tk.Button(window_MainFridge, text='Search Fridge', command=Open_SearchFridge_Window, font=myFont).grid(row=5, column=1, sticky="ew")
    tk.Button(window_MainFridge, text='Back to Edit Menu', command=Open_MainMenu_Window, font=myFont).grid(row=7, column=1, sticky="ew")

    tk.Label(window_MainFridge, height = 1, width = 6, bg="cadet blue").grid(row =0, column =2)
    tk.Label(window_MainFridge, height = 1, width = 6, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_MainFridge, height = 1, width = 6, bg="cadet blue").grid(row =4, column =0)
    tk.Label(window_MainFridge, height = 1, width = 6, bg="cadet blue").grid(row =6, column =0) 
    tk.Label(window_MainFridge, height = 1, width = 6, bg="cadet blue").grid(row =8, column =0) 

    window_MainFridge.mainloop()
##########---------->END: MAIN WINDOW FOR FRIDGES<----------##########

