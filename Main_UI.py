import SetupAPI
import sqlite3
import tkinter as tk
import Box_UI
import Fridge_UI
import Sample_UI
import User_CredentialCheck

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

##########---------->START: MAIN WINDOW<----------##########
def Main_Window():
    window_Main = tk.Tk()
    window_Main.geometry("300x300")
    window_Main.title("MAIN MENU")
    window_Main["bg"] = 'cyan'

    def Open_BoxMenu_Window():
        window_Main.destroy()
        User_CredentialCheck.Check_Window("Box")

    def Open_FridgeMenu_Window():
        window_Main.destroy()
        User_CredentialCheck.Check_Window("Fridge")

    def Open_SampleMenu_Window():
        window_Main.destroy()
        User_CredentialCheck.Check_Window("Sample")


    tk.Button(window_Main, text = 'Open Fridge Menu', 
                        command = Open_FridgeMenu_Window).grid(row = 0, column=0)

    tk.Button(window_Main, text = 'Open Box Menu', 
                        command = Open_BoxMenu_Window).grid(row = 1, column=0)

    tk.Button(window_Main, text = 'Open Sample Menu', 
                        command = Open_SampleMenu_Window).grid(row = 2, column=0)

    window_Main.mainloop()
##########---------->END: MAIN WINDOW<----------##########

