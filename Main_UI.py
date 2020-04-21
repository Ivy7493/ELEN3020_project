from tkinter.font import Font
import SetupAPI
import sqlite3
import tkinter as tk
import Box_UI
import Fridge_UI
import Sample_UI
import User_CredentialCheck
import DataAPI
import Startup
import ViewMode_UI
import LoggingAPI
import Billing_UI
import datetime
from datetime import date
from datetime import datetime

##########---------->START: MAIN WINDOW<--------------------##########
def Main_Window(conn):
    window_Main = tk.Tk()
    #window_Main.geometry("250x225")
    window_Main.title("MAIN MENU")
    window_Main["bg"] = 'cadet blue'
    
    text = tk.Text(window_Main)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def Open_Edit_Window():
        temp = LoggingAPI.GetCurrentAccess(conn)
        if temp == 0:
            message_window = tk.Tk()
            message_window.title("ERROR")
            message = tk.Label(message_window, text = "INVALID ACCESS LEVEL")
            message.grid(row = 0, column = 0)

            def Close():
                message_window.destroy()          

            backButton = tk.Button(message_window, text = 'Close', command =Close, bg = "mint cream").grid(row=1)

        else:
            window_Main.destroy()
            Edit_Window(conn)

    def Open_View_Window():
        window_Main.destroy()
        ViewMode_UI.ViewFridges(conn)
    
    def Open_Billing_Window():
        window_Main.destroy()
        Billing_UI.MainBilling_Window(conn)

    def Logout():
        window_Main.destroy()
        DataAPI.LogoutAll(conn)
        Startup.Start_Window(conn)

    def Exit():
        window_Main.destroy()

    tk.Label(window_Main, bg="cadet blue", text = '              ').grid(row=0, column=2)
    tk.Button(window_Main, text = 'Edit Mode', font=myFont, command = Open_Edit_Window).grid(row = 1, column=1, sticky = "ew")
    tk.Label(window_Main, bg="cadet blue", text = '              ').grid(row=2, column=0)
    tk.Button(window_Main, text = 'View Mode', font=myFont, command = Open_View_Window).grid(row = 3, column=1, sticky = "ew")
    tk.Label(window_Main, bg="cadet blue", text = '              ').grid(row=4, column=0)
    tk.Button(window_Main, text = 'Invoice Mode', font=myFont, command = Open_Billing_Window).grid(row = 5, column=1, sticky = "ew")
    tk.Label(window_Main, bg="cadet blue", text = '              ').grid(row=6, column=0)
    tk.Button(window_Main, text = 'Log Out', font=myFont, command = Logout).grid(row = 7, column=1, sticky = "ew")
    tk.Label(window_Main, bg="cadet blue", text = '              ').grid(row=8, column=0)
    tk.Button(window_Main, text = 'Exit', font=myFont, command = Exit).grid(row = 9, column=1, sticky = "ew")
    tk.Label(window_Main, bg="cadet blue", text = '              ').grid(row=10, column=0)

    window_Main.mainloop()

def Edit_Window(conn):
    window_Edit = tk.Tk()
    #window_Edit.geometry("300x250")
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
    
    def Return():
        window_Edit.destroy()
        Main_Window(conn)

    tk.Label(window_Edit, text = '              ', bg = 'cadet blue').grid(row=0, column=2)
    tk.Button(window_Edit, text = 'Open Fridge Menu', command = Open_FridgeMenu_Window, font=myFont).grid(row = 1, column=1, sticky = "ew")
    tk.Label(window_Edit, text = '              ', bg = 'cadet blue').grid(row=2, column=0)
    tk.Button(window_Edit, text = 'Open Box Menu', command = Open_BoxMenu_Window, font=myFont).grid(row = 3, column=1, sticky = "ew")
    tk.Label(window_Edit, text = '              ', bg = 'cadet blue').grid(row=4, column=0)
    tk.Button(window_Edit, text = 'Open Sample Menu', command = Open_SampleMenu_Window, font=myFont).grid(row = 5, column=1, sticky = "ew")
    tk.Label(window_Edit, text = '              ', bg = 'cadet blue').grid(row=6, column=0)
    tk.Button(window_Edit, text = 'Return', command = Return, font=myFont).grid(row = 7, column=1, sticky = "ew")
    tk.Label(window_Edit, text = '              ', bg = 'cadet blue').grid(row=8, column=0)
    #tk.Label(window_Edit, text = '').grid(row=0, column=1)


    window_Edit.mainloop()
##########---------->END: MAIN WINDOW<----------------------##########

##########---------->START: WARNING WINDOW WINDOW<----------##########
def Warning_Window(conn):

    def CloseWarningWindow():
        window_Warning.destroy()

    sampleDateWarning = DataAPI.CheckAllSampleDates(conn)
    if(sampleDateWarning != ""):
        window_Warning = tk.Tk()
        window_Warning.title("SAMPLE DATE WARNING")
        window_Warning["bg"] = 'red'
       
        tk.Label(window_Warning, text = sampleDateWarning, bg="red").grid(row=0)

        tk.Button(window_Warning, text = 'Continue', command = CloseWarningWindow).grid(column=0)

        window_Warning.mainloop()
##########---------->END: WARNING WINDOW<------------------##########    

