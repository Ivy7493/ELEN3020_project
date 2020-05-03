from tkinter.font import Font
import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import DisplayBoxes
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

##########---------->START: WINDOW FOR ADDING BOXES<----------##########
def AddBox_Window(conn):
    def CreateBox():
        _boxID = boxID.get()
        _fridgeID = fridgeID.get()
        _fridgeX = fridgeX.get()
        _fridgeY = fridgeY.get()
        _boxX = boxX.get()
        _boxY = boxY.get()
        _boxZ = boxZ.get()
        try:
            _fridgeX = int(_fridgeX)
            _fridgeY = int(_fridgeY)
            _boxX = int(_boxX)
            _boxY = int(_boxY)
            _boxZ = int(_boxZ)
            intCheck = "TRUE"
        except:
            intCheck = "FALSE"

        if any( [_boxID == "", _fridgeID == "", _fridgeX == "", _fridgeY == "", _boxX == "", _boxY == "", _boxZ == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        elif intCheck == "FALSE":
            MessagePopup("One or more fields are wrong data type", "ERROR")
        else:
            try:
                messageText = DataAPI.AddBox(conn, _boxID, _fridgeID, _fridgeX, _fridgeY, _boxX, _boxY, _boxZ)
                MessagePopup(messageText, "Add Box")
            except:
                MessagePopup("ERROR: Invalid data entered", "Add Box")

    def Open_MainBox_Window():
        window_AddBox.destroy()
        MainBox_Window(conn)

    def SuggestFridge():
        MessagePopup(DataAPI.FindEmptyFridge(conn),"Suggest Fridge")

    window_AddBox = tk.Tk()
    window_AddBox.title("ADD BOX")
    window_AddBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_AddBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_AddBox, text="Box ID", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=1, column = 1, sticky = "ew")
    boxID = tk.Entry(window_AddBox)
    boxID.grid(row=1, column=2, sticky = "ew")

    tk.Label(window_AddBox, text="Fridge ID", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=2, column = 1, sticky = "ew")
    fridgeID = tk.Entry(window_AddBox)
    fridgeID.grid(row=2, column=2, sticky = "ew")

    tk.Label(window_AddBox, text="Fridge X Position", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=3, column = 1, sticky = "ew")
    fridgeX = tk.Entry(window_AddBox)
    fridgeX.grid(row=3, column=2, sticky = "ew")

    tk.Label(window_AddBox, text="Fridge Y Position", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=4, column = 1, sticky = "ew")
    fridgeY = tk.Entry(window_AddBox)
    fridgeY.grid(row=4, column=2, sticky = "ew")

    tk.Label(window_AddBox, text="Box X", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=5, column = 1, sticky = "ew")
    boxX = tk.Entry(window_AddBox)
    boxX.grid(row=5, column=2, sticky = "ew")

    tk.Label(window_AddBox, text="Box Y", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=6, column = 1, sticky = "ew")
    boxY = tk.Entry(window_AddBox)
    boxY.grid(row=6, column=2, sticky = "ew")

    tk.Label(window_AddBox, text="Box Z", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=7, column = 1, sticky = "ew")
    boxZ = tk.Entry(window_AddBox)
    boxZ.grid(row=7, column=2, sticky = "ew")

    tk.Button(window_AddBox, text='Add Box', command=CreateBox, font = myFont).grid(row=8, column=2, sticky = "ew")
    tk.Button(window_AddBox, text='Suggest Fridge', command=SuggestFridge, font = myFont).grid(row=2, column=3)
    tk.Button(window_AddBox, text='Back to Box Menu', command=Open_MainBox_Window, font = myFont).grid(row=10, column=2, sticky = "ew")

    tk.Label(window_AddBox, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_AddBox, height = 1, width = 2, bg="cadet blue").grid(row =9, column =0)
    tk.Label(window_AddBox, height = 1, width = 2, bg="cadet blue").grid(row =11, column =4)

    window_AddBox.mainloop()
##########---------->END: WINDOW FOR ADDING BOXES<----------##########

##########---------->START: WINDOW FOR MOVING BOXES<----------##########


def MoveBox_Window(conn):
    def MoveBox():
        try:
            _boxID = boxID.get()
            _fridgeID = fridgeID.get()
            _fridgeX = int(fridgeX.get())
            _fridgeY = int(fridgeY.get())
            messageText = DataAPI.MoveBox(conn, _boxID, _fridgeID, _fridgeX, _fridgeY)
            MessagePopup(messageText, "Move Box")
        except:
            MessagePopup("ERROR: Invalid data entered", "Move Box")

    def Open_MainBox_Window():
        window_MoveBox.destroy()
        MainBox_Window(conn)

    def SuggestFridge():  
        MessagePopup(DataAPI.FindEmptyFridge(conn),"Suggest Fridge")

    window_MoveBox = tk.Tk()
    window_MoveBox.title("MOVE BOX")
    window_MoveBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_MoveBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_MoveBox, text="Move box with BoxID:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=1, column = 1, sticky = "ew")
    boxID = tk.Entry(window_MoveBox)
    boxID.grid(row=1, column=2, sticky = "ew")

    tk.Label(window_MoveBox, text="To fridge with FridgeID:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=2, column = 1, sticky = "ew")
    fridgeID = tk.Entry(window_MoveBox)
    fridgeID.grid(row=2, column=2, sticky = "ew")

    tk.Label(window_MoveBox, text="Fridge X Position:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=3, column = 1, sticky = "ew")
    fridgeX = tk.Entry(window_MoveBox)
    fridgeX.grid(row=3, column=2, sticky = "ew")

    tk.Label(window_MoveBox, text="Fridge Y Position:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row=4, column = 1, sticky = "ew")
    fridgeY = tk.Entry(window_MoveBox)
    fridgeY.grid(row=4, column=2, sticky = "ew")

    tk.Button(window_MoveBox, text='Move Box', command=MoveBox, font = myFont).grid(row=5, column=2, sticky = "ew")
    tk.Button(window_MoveBox, text='Back to Box Menu', command=Open_MainBox_Window, font = myFont).grid(row=7, column=2, sticky = "ew")
    tk.Button(window_MoveBox, text='Suggest Fridge', command=SuggestFridge, font = myFont).grid(row=2, column=3)

    tk.Label(window_MoveBox, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_MoveBox, height = 1, width = 2, bg="cadet blue").grid(row =6, column =0)
    tk.Label(window_MoveBox, height = 1, width = 2, bg="cadet blue").grid(row =8, column =4)

    window_MoveBox.mainloop()
##########---------->END: WINDOW FOR MOVING BOXES<----------##########

##########---------->START: WINDOW FOR DELETING BOXES<----------##########
def DeleteBox_Window(conn):
    def DeleteBox():
        _boxID = boxID.get()
        messageText = DataAPI.DeleteBox(conn, _boxID)
        MessagePopup(messageText, "Delete Box")

    def Open_MainBox_Window():
        window_DeleteBox.destroy()
        MainBox_Window(conn)

    window_DeleteBox = tk.Tk()
    window_DeleteBox.title("DELETE BOX")
    window_DeleteBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_DeleteBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_DeleteBox, text="Delete box with BoxID: ", font=myFont, bg = 'cadet blue', anchor = "w").grid(row=1, column = 1, sticky = "ew")
    boxID = tk.Entry(window_DeleteBox)
    boxID.grid(row=1, column=2, sticky = "ew")

    tk.Button(window_DeleteBox, text='Delete Box', command=DeleteBox, font = myFont).grid(row=2, column=2, sticky = "ew")
    tk.Button(window_DeleteBox, text='Back to Box Menu', command=Open_MainBox_Window, font = myFont).grid(row=4, column=2, sticky = "ew")

    tk.Label(window_DeleteBox, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_DeleteBox, height = 1, width = 2, bg="cadet blue").grid(row =3, column =0)
    tk.Label(window_DeleteBox, height = 1, width = 2, bg="cadet blue").grid(row =5, column =3)

    window_DeleteBox.mainloop()
##########---------->END: WINDOW FOR DELETING BOXES<----------##########

##########---------->START: WINDOW FOR SEARCHING BOXES<------##########
def SearchBox_Window(conn):
    window_SearchBox = tk.Tk()
    window_SearchBox.title("SEARCH BOX WINDOW")
    #window_SearchBox.geometry("400x250")
    window_SearchBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_SearchBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    #--------------------
    def Open_AllBoxes():
        DisplayBoxes.OpenAllBoxes(conn)

    displayBoxesButton = tk.Button(window_SearchBox, text='Display All Boxes', command=Open_AllBoxes, font = myFont)
    displayBoxesButton.grid(row=1, column=2, sticky = "ew")
    #--------------------
    searchLabel1 = tk.Label(window_SearchBox, text = 'Box ID:', anchor = "w", font = myFont, bg = 'cadet blue').grid(row=3, column = 1, sticky = "ew")
    searchField1 = tk.Entry(window_SearchBox)
    searchField1.grid(row=3, column=2, sticky = "ew")
    
    def runDisplayBoxes():
        DisplayBoxes.OpenBoxIDSearch(conn, searchField1.get())

    searchButton1 = tk.Button(window_SearchBox, text='Search', command= runDisplayBoxes, font = myFont)
    searchButton1.grid(row=3, column=3, sticky = "ew")
    #--------------------
    searchLabel2 = tk.Label(window_SearchBox, text = 'Fridge ID:', anchor = "w", font = myFont, bg = 'cadet blue').grid(row = 4, column = 1, sticky = "ew")
    searchField2 = tk.Entry(window_SearchBox)
    searchField2.grid(row=4, column=2, sticky = "ew")

    def runDisplayFridgeID():
    	DisplayBoxes.OpenFridgeIDSearch(conn, searchField2.get())

    searchButton2 = tk.Button(window_SearchBox, text = 'Search', command=runDisplayFridgeID, font = myFont)
    searchButton2.grid(row=4, column=3, sticky = "ew")
    #--------------------
    def Open_MainMenu_Window():
        window_SearchBox.destroy()
        MainBox_Window(conn)

    ReturnButton = tk.Button(window_SearchBox, text='Back to Box Menu', command=Open_MainMenu_Window, font = myFont).grid(row=6, column=2)
    #--------------------

    tk.Label(window_SearchBox, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_SearchBox, height = 1, width = 2, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_SearchBox, height = 1, width = 2, bg="cadet blue").grid(row =5, column =0)
    tk.Label(window_SearchBox, height = 1, width = 2, bg="cadet blue").grid(row =7, column = 4)

    window_SearchBox.mainloop()

##########---------->END: WINDOW FOR SEARCHING BOXES<------##########

##########---------->START: MAIN WINDOW FOR BOXES<----------##########
def MainBox_Window(conn):
    window_MainBox = tk.Tk()
    window_MainBox.title("BOX MENU")
    window_MainBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_MainBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def Open_SearchBox_Window():
        window_MainBox.destroy()
        SearchBox_Window(conn)

    def Open_AddBox_Window():
        window_MainBox.destroy()
        AddBox_Window(conn)

    def Open_MoveBox_Window():
        window_MainBox.destroy()
        MoveBox_Window(conn)

    def Open_DeleteBox_Window():
        window_MainBox.destroy()
        DeleteBox_Window(conn)

    def Open_MainMenu_Window():
        window_MainBox.destroy()
        Main_UI.Edit_Window(conn)

    tk.Button(window_MainBox, text='Add Box', command=Open_AddBox_Window, font = myFont).grid(row=1, column=1, sticky = "ew")
    tk.Button(window_MainBox, text='Move Box', command=Open_MoveBox_Window, font = myFont).grid(row=3, column=1, sticky = "ew")
    tk.Button(window_MainBox, text='Delete Box', command=Open_DeleteBox_Window, font = myFont).grid(row=5, column=1, sticky = "ew")
    tk.Button(window_MainBox, text='Search Box', command=Open_SearchBox_Window, font = myFont).grid(row=7, column=1, sticky = "ew")
    tk.Button(window_MainBox, text='Back to Edit Menu', command=Open_MainMenu_Window, font = myFont).grid(row=9, column=1, sticky = "ew")

    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 0, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 2, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 4, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 6, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 8, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 10, column = 2)

    window_MainBox.mainloop()
##########---------->END: MAIN WINDOW FOR BOXES<----------##########

