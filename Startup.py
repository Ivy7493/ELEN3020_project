from tkinter import *
import tkinter as tk
from tkinter.font import Font
import sqlite3
import DataAPI
import SetupAPI
import User_CredentialCheck
import GuestLogin

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

SetupAPI.CreateAllTables(conn)
DataAPI.LogoutAll(conn)


def Start_Window():
    start_window = Tk()
    # start_window.geometry("300x300")
    start_window.title("START")
    start_window["bg"] = 'cadet blue'

    text = tk.Text(start_window)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)
    
    def Employee_Window():
    	start_window.destroy()
    	User_CredentialCheck.Check_Window()

    def Guest_Window():
        start_window.destroy()
        GuestLogin.LoginScreen()

    def Exit():
        start_window.destroy()

    employeeButton = Button(start_window, text="Employee", font = myFont,
                            command=Employee_Window, height=1, width=8)
    guestButton = Button(start_window, text="Guest", font = myFont,
                         command=Guest_Window, height=1, width=8)
    info = Label(start_window, text="Please select Employee or Guest to go to login", font = myFont, bg="cadet blue")
    exitButton = Button(start_window, text="Exit", font = myFont,
                        command=Exit, height=1, width=8)

    info.grid(row=0, column=0)
    employeeButton.grid(row=1, column=0)
    guestButton.grid(row=2, column=0)
    exitButton.grid(row=3, column=0)

    start_window.mainloop()


Start_Window()
