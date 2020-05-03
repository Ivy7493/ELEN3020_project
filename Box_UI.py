from tkinter.font import Font
import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import DisplayBoxes
from tkinter import messagebox


##########---------->START: WINDOW FOR ADDING BOXES<----------##########


def AddBox_Window(conn):
    def CreateBox():
        try:
            _boxID = boxID.get()
            _fridgeID = fridgeID.get()
            _fridgeX = int(fridgeX.get())
            _fridgeY = int(fridgeY.get())
            _boxX = int(boxX.get())
            _boxY = int(boxY.get())
            _boxZ = int(boxZ.get())
            messagebox.showinfo("Add Box", DataAPI.AddBox(
                conn, _boxID, _fridgeID, _fridgeX, _fridgeY, _boxX, _boxY, _boxZ))
        except:
            messagebox.showinfo("Add Box", "ERROR: Invalid data entered")

    def console_PrintBox():
        print("Box ID: %s\nFridge ID: %s\nFridge X: %s\nFridgeY: %s\nBox X: %s\nBox Y: %s\nBox Z: %s" %
              (boxID.get(), fridgeID.get(), fridgeX.get(), fridgeY.get(), boxX.get(), boxY.get(), boxZ.get()))

    def Open_MainBox_Window():
        window_AddBox.destroy()
        MainBox_Window(conn)

    def SuggestFridge():
        messagebox.showinfo("Suggest Fridge", DataAPI.FindEmptyFridge(conn))

    window_AddBox = tk.Tk()
    # window_AddBox.geometry("300x300")
    window_AddBox.title("ADD BOX")
    window_AddBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_AddBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_AddBox, text="Box ID", font = myFont, bg = 'cadet blue').grid(row=0)
    boxID = tk.Entry(window_AddBox)
    boxID.grid(row=0, column=1)

    tk.Label(window_AddBox, text="Fridge ID", font = myFont, bg = 'cadet blue').grid(row=1)
    fridgeID = tk.Entry(window_AddBox)
    fridgeID.grid(row=1, column=1)

    tk.Label(window_AddBox, text="Fridge X Position", font = myFont, bg = 'cadet blue').grid(row=2)
    fridgeX = tk.Entry(window_AddBox)
    fridgeX.grid(row=2, column=1)

    tk.Label(window_AddBox, text="Fridge Y Position", font = myFont, bg = 'cadet blue').grid(row=3)
    fridgeY = tk.Entry(window_AddBox)
    fridgeY.grid(row=3, column=1)

    tk.Label(window_AddBox, text="Box X", font = myFont, bg = 'cadet blue').grid(row=4)
    boxX = tk.Entry(window_AddBox)
    boxX.grid(row=4, column=1)

    tk.Label(window_AddBox, text="Box Y", font = myFont, bg = 'cadet blue').grid(row=5)
    boxY = tk.Entry(window_AddBox)
    boxY.grid(row=5, column=1)

    tk.Label(window_AddBox, text="Box Z", font = myFont, bg = 'cadet blue').grid(row=6)
    boxZ = tk.Entry(window_AddBox)
    boxZ.grid(row=6, column=1)

    #tk.Button(window_AddBox, text='Print Box to Console', command=console_PrintBox, font = myFont).grid(row=7, column=1)
    tk.Button(window_AddBox, text='Add Box', command=CreateBox, font = myFont).grid(row=8, column=1, sticky = "ew")

    tk.Button(window_AddBox, text='Suggest Fridge', command=SuggestFridge, font = myFont).grid(row=1, column=3)

    tk.Button(window_AddBox, text='Back to Box Menu', command=Open_MainBox_Window, font = myFont).grid(row=10, column=1, sticky = "ew")

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
            messagebox.showinfo("Move Box", DataAPI.MoveBox(
                conn, _boxID, _fridgeID, _fridgeX, _fridgeY))
        except:
            messagebox.showinfo("Move Box", "ERROR: Invalid data entered")

    def Open_MainBox_Window():
        window_MoveBox.destroy()
        MainBox_Window(conn)

    def SuggestFridge():
        messagebox.showinfo("Suggest Fridge", DataAPI.FindEmptyFridge(conn))

    window_MoveBox = tk.Tk()
    # window_MoveBox.geometry("300x300")
    window_MoveBox.title("MOVE BOX")
    window_MoveBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_MoveBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_MoveBox, text="Move box with BoxID:", font = myFont, bg = 'cadet blue').grid(row=0)
    boxID = tk.Entry(window_MoveBox)
    boxID.grid(row=0, column=1)

    tk.Label(window_MoveBox, text="To fridge with FridgeID:", font = myFont, bg = 'cadet blue').grid(row=1)
    fridgeID = tk.Entry(window_MoveBox)
    fridgeID.grid(row=1, column=1)

    tk.Label(window_MoveBox, text="Fridge X Position:", font = myFont, bg = 'cadet blue').grid(row=2)
    fridgeX = tk.Entry(window_MoveBox)
    fridgeX.grid(row=2, column=1)

    tk.Label(window_MoveBox, text="Fridge Y Position:", font = myFont, bg = 'cadet blue').grid(row=3)
    fridgeY = tk.Entry(window_MoveBox)
    fridgeY.grid(row=3, column=1)

    tk.Button(window_MoveBox, text='Move Box', command=MoveBox, font = myFont).grid(row=5, column=1, sticky = "ew")
    tk.Button(window_MoveBox, text='Back to Box Menu', command=Open_MainBox_Window, font = myFont).grid(row=10, column=1, sticky = "ew")
    tk.Button(window_MoveBox, text='Suggest Fridge', command=SuggestFridge, font = myFont).grid(row=1, column=3)

    window_MoveBox.mainloop()
##########---------->END: WINDOW FOR MOVING BOXES<----------##########

##########---------->START: WINDOW FOR DELETING BOXES<----------##########


def DeleteBox_Window(conn):
    def DeleteBox():
        _boxID = boxID.get()
        messagebox.showinfo("Delete Box", (DataAPI.DeleteBox(conn, _boxID)))

    def Open_MainBox_Window():
        window_DeleteBox.destroy()
        MainBox_Window(conn)

    window_DeleteBox = tk.Tk()
    #window_DeleteBox.geometry("300x300")
    window_DeleteBox.title("DELETE BOX")
    window_DeleteBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_DeleteBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_DeleteBox, text="Delete box with BoxID: ", font=myFont, bg = 'cadet blue').grid(row=0)
    boxID = tk.Entry(window_DeleteBox)
    boxID.grid(row=0, column=1)

    tk.Button(window_DeleteBox, text='Delete Box', command=DeleteBox, font = myFont).grid(row=5, column=1, sticky = "ew")
    tk.Button(window_DeleteBox, text='Back to Box Menu', command=Open_MainBox_Window, font = myFont).grid(row=10, column=1, sticky = "ew")

    window_DeleteBox.mainloop()
##########---------->END: WINDOW FOR DELETING BOXES<----------##########



##########---------->START: MAIN WINDOW FOR BOXES<----------##########
def MainBox_Window(conn):
    window_MainBox = tk.Tk()
    window_MainBox.geometry("300x250")
    window_MainBox.title("BOX MENU")
    window_MainBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_MainBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)



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
    tk.Button(window_MainBox, text='Back to Edit Menu', command=Open_MainMenu_Window, font = myFont).grid(row=7, column=1, sticky = "ew")

    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 0, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 2, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 4, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 6, column = 0)
    tk.Label(window_MainBox, height = 1, width = 6, bg ='cadet blue').grid(row = 8, column = 0)

    window_MainBox.mainloop()
##########---------->END: MAIN WINDOW FOR BOXES<----------##########

