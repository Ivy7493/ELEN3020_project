from tkinter.font import Font
import SetupAPI
import sqlite3
import tkinter as tk
import Box_UI
import Fridge_UI
import Sample_UI
import User_CredentialCheck
import DataAPI
import ViewMode_UI
import Search_UI
import LoggingAPI
import Register_UI
import Billing_UI
import Auto_UI
import StockTake_UI
import datetime
from datetime import date
from datetime import datetime

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

##########---------->START: MAIN WINDOW<--------------------##########
def Main_Window(conn):
    window_Main = tk.Tk()
    window_Main.title("MAIN MENU")
    window_Main["bg"] = 'cadet blue'
    
    text = tk.Text(window_Main)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def Open_Edit_Window():
        temp = LoggingAPI.GetCurrentAccess(conn)
        if temp == 1:
            MessagePopup("INVALID ACCESS LEVEL", "ERROR")

        elif temp == 2:
            window_Main.destroy()
            Edit_Window(conn)

    def Open_View_Window():
        window_Main.destroy()
        ViewMode_UI.ViewFridges(conn, "FALSE")
    
    def Open_Billing_Window():
        window_Main.destroy()
        Billing_UI.MainBilling_Window(conn)
    
    def Open_Search_Window():
        window_Main.destroy()
        Search_UI.MainSearch_Window(conn)

    def Open_StockTake_Window():
        window_Main.destroy()
        StockTake_UI.MainStockTake_Window(conn)

    def Logout():
        window_Main.destroy()
        DataAPI.LogoutAll(conn)
        User_CredentialCheck.Check_Window(conn)

    def Exit():
        window_Main.destroy()

    tk.Button(window_Main, text = 'Edit Mode', font=myFont, command = Open_Edit_Window).grid(row = 1, column=1, sticky = "ew")
    tk.Button(window_Main, text = 'View Mode', font=myFont, command = Open_View_Window).grid(row = 3, column=1, sticky = "ew")
    tk.Button(window_Main, text = 'Invoice Mode', font=myFont, command = Open_Billing_Window).grid(row = 5, column=1, sticky = "ew")
    tk.Button(window_Main, text = 'Search Mode', font=myFont, command = Open_Search_Window).grid(row=7, column=1, sticky = "ew")
    tk.Button(window_Main, text = 'Stock Take Mode', font=myFont, command = Open_StockTake_Window).grid(row=9, column=1, sticky = "ew")
    tk.Button(window_Main, text = 'Log Out', font=myFont, command = Logout).grid(row = 11, column=1, sticky = "ew")
    tk.Button(window_Main, text = 'Exit', font=myFont, command = Exit).grid(row = 13, column=1, sticky = "ew")

    tk.Label(window_Main, height = 1, width = 6, bg="cadet blue").grid(row=0, column=2)
    tk.Label(window_Main, height = 1, width = 6, bg="cadet blue").grid(row=2, column=0)
    tk.Label(window_Main, height = 1, width = 6, bg="cadet blue").grid(row=4, column=0)
    tk.Label(window_Main, height = 1, width = 6, bg="cadet blue").grid(row=6, column=0)
    tk.Label(window_Main, height = 1, width = 6, bg="cadet blue").grid(row=8, column=0)
    tk.Label(window_Main, height = 1, width = 6, bg="cadet blue").grid(row=10, column=0)
    tk.Label(window_Main, height = 1, width = 6, bg="cadet blue").grid(row=12, column=0)
    tk.Label(window_Main, height = 1, width = 6, bg="cadet blue").grid(row=14, column=0)

    window_Main.mainloop()
##########---------->END: MAIN WINDOW<----------------------##########

##########---------->START: EDIT WINDOW<--------------------##########
def Edit_Window(conn):
    window_Edit = tk.Tk()
    window_Edit.title("EDIT MENU")
    window_Edit["bg"] = 'cadet blue'
    
    text = tk.Text(window_Edit)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def Open_BoxMenu_Window():
        window_Edit.destroy()
        Box_UI.MainBox_Window(conn)

    def Open_FridgeMenu_Window():
        window_Edit.destroy()
        Fridge_UI.MainFridge_Window(conn)

    def Open_SampleMenu_Window():
        window_Edit.destroy()
        Sample_UI.MainSample_Window(conn)

    def Open_AutoAddSamples_Window():
        window_Edit.destroy()
        Auto_UI.AddSamples(conn)

    def Open_ManageUserLogin_Window():
        window_Edit.destroy()
        Register_UI.Manage_Window(conn)
    
    def Open_NewClientCollection_Window():
        window_Edit.destroy()
        Register_UI.RegisterClient_Window(conn)

    def Return():
        window_Edit.destroy()
        Main_Window(conn)

    tk.Label(window_Edit, height = 1, width = 6, bg = 'cadet blue').grid(row=0, column=2)
    tk.Button(window_Edit, text = 'Fridge Menu', command = Open_FridgeMenu_Window, font=myFont).grid(row = 1, column=1, sticky = "ew")
    tk.Label(window_Edit, height = 1, width = 6, bg = 'cadet blue').grid(row=2, column=0)

    tk.Button(window_Edit, text = 'Box Menu', command = Open_BoxMenu_Window, font=myFont).grid(row = 3, column=1, sticky = "ew")
    tk.Label(window_Edit, height = 1, width = 6, bg = 'cadet blue').grid(row=4, column=0)

    tk.Button(window_Edit, text = 'Sample Menu', command = Open_SampleMenu_Window, font=myFont).grid(row = 5, column=1, sticky = "ew")
    tk.Label(window_Edit, height = 1, width = 6, bg = 'cadet blue').grid(row=6, column=0)

    tk.Button(window_Edit, text = 'Auto Add Menu', font=myFont, command = Open_AutoAddSamples_Window).grid(row = 7, column=1, sticky = "ew")
    tk.Label(window_Edit, height = 1, width = 6, bg="cadet blue").grid(row=8, column=0)

    tk.Button(window_Edit, text = 'Manage User Login', font=myFont, command = Open_ManageUserLogin_Window).grid(row = 9, column=1, sticky = "ew")
    tk.Label(window_Edit, height = 1, width = 6, bg="cadet blue").grid(row=10, column=0)

    tk.Button(window_Edit, text = 'New Client Collection', command = Open_NewClientCollection_Window, font=myFont).grid(row = 11, column=1, sticky = "ew")
    tk.Label(window_Edit, height = 1, width = 6, bg = 'cadet blue').grid(row=12, column=0)

    tk.Button(window_Edit, text = 'Return', command = Return, font=myFont).grid(row = 13, column=1, sticky = "ew")
    tk.Label(window_Edit, height = 1, width = 6, bg = 'cadet blue').grid(row=14, column=0)
    window_Edit.mainloop()
##########---------->END: EDIT WINDOW<----------------------##########

##########---------->START: WARNING WINDOW WINDOW<----------##########
def Warning_Window(conn):

    def CloseWarningWindow():
        window_Warning.destroy()

    sampleDateWarning = DataAPI.CheckAllSampleDates(conn)
    if(sampleDateWarning != ""):
        window_Warning = tk.Tk()
        window_Warning.title("SAMPLE DATE WARNING")
        window_Warning["bg"] = 'cadet blue'

        text = tk.Text(window_Warning)
        myFont = Font(family="fixedsys", size=12)
        text.configure(font=myFont)
       
        tk.Label(window_Warning, text = sampleDateWarning, bg="cadet blue", font = myFont).grid(row=1, column = 1)
        tk.Button(window_Warning, text = 'Continue', command = CloseWarningWindow, font = myFont).grid(row = 2, column=1)

        tk.Label(window_Warning, height = 1, width = 2, bg ='cadet blue').grid(row = 0, column = 0)
        tk.Label(window_Warning, height = 1, width = 2, bg ='cadet blue').grid(row = 3, column = 2)

        window_Warning.mainloop()
##########---------->END: WARNING WINDOW<------------------##########    

