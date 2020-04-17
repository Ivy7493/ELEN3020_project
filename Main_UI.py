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

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

##########---------->START: MAIN WINDOW<--------------------##########
def Main_Window():
    window_Main = tk.Tk()
    window_Main.geometry("300x300")
    window_Main.title("MAIN MENU")
    window_Main["bg"] = 'cyan'

    def Open_Edit_Window():
        temp = LoggingAPI.GetCurrentAccess()
        if temp == 0:
            message_window = tk.Tk()
            message_window.title("ERROR")
            message = tk.Label(message_window, text = "INVALID ACCESS LEVEL")
            message.grid(row = 0, column = 0)

            def Close():
                message_window.destroy()          

            backButton = tk.Button(message_window, text = 'Close', command =Close).grid(row=1)

        else:
            window_Main.destroy()
            Edit_Window()

    def Open_View_Window():
        window_Main.destroy()
        ViewMode_UI.ViewFridges(conn)
    
    def Logout():
        window_Main.destroy()
        DataAPI.LogoutAll(conn)
        Startup.Start_Window()

    def Exit():
        window_Main.destroy()

    tk.Button(window_Main, text = 'Edit Mode', command = Open_Edit_Window).grid(row = 0, column=0)
    tk.Button(window_Main, text = 'View Mode', command = Open_View_Window).grid(row = 1, column=0)
    tk.Button(window_Main, text = 'Log Out', command = Logout).grid(row = 3, column=0)
    tk.Button(window_Main, text = 'Exit', command = Exit).grid(row = 4, column=0)

    window_Main.mainloop()



def Edit_Window():
    window_Edit = tk.Tk()
    window_Edit.geometry("300x300")
    window_Edit.title("MAIN MENU")
    window_Edit["bg"] = 'cyan'

    def Open_BoxMenu_Window():
        window_Edit.destroy()
        Box_UI.MainBox_Window()

    def Open_FridgeMenu_Window():
        window_Edit.destroy()
        Fridge_UI.MainFridge_Window()

    def Open_SampleMenu_Window():
        window_Edit.destroy()
        Sample_UI.MainSample_Window()
    
    def Return():
        window_Edit.destroy()
        Main_Window()

    tk.Button(window_Edit, text = 'Open Fridge Menu', command = Open_FridgeMenu_Window).grid(row = 0, column=0)
    tk.Button(window_Edit, text = 'Open Box Menu', command = Open_BoxMenu_Window).grid(row = 1, column=0)
    tk.Button(window_Edit, text = 'Open Sample Menu', command = Open_SampleMenu_Window).grid(row = 2, column=0)
    tk.Button(window_Edit, text = 'Return', command = Return).grid(row = 3, column=0)


    window_Edit.mainloop()
##########---------->END: MAIN WINDOW<----------------------##########

##########---------->START: WARNING WINDOW WINDOW<----------##########
def Warning_Window():

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

