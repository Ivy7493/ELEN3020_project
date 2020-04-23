import SetupAPI
import sqlite3
import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox
import DataAPI
import Main_UI


def Register_Window(conn):
    def AddUser():
        try:
            _username = username.get()
            _password = password.get()
            _accessLevel = accessLevel.get()
            
            messagebox.showinfo("Add User", DataAPI.AddUser(conn, _username, _password, _accessLevel))
        except:
            messagebox.showinfo("Add User", "ERROR: Invalid data entered")

    def GetAccessLevel():
        return ["Customer", "Employee", "Supervisor"]

    def Return():
        window_register.destroy()
        Main_UI.Edit_Window(conn)

    window_register = tk.Tk()
    window_register.title("ADD USER")
    window_register["bg"] = 'cadet blue'

    text = tk.Text(window_register)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    userLabel = tk.Label(window_register, text = "Username: ", anchor = "w", bg = 'cadet blue', font = myFont)
    passLabel = tk.Label(window_register, text = "Password: ", anchor = "w", bg = 'cadet blue', font = myFont)
    accessLabel = tk.Label(window_register, text = "Access Level: ", anchor = "w", bg = 'cadet blue', font = myFont)

    username = tk.Entry(window_register)
    password = tk.Entry(window_register)
    accessLevel = ttk.Combobox(window_register, state="readonly", values=GetAccessLevel()) 

    registerButton = tk.Button(window_register, text = "Register", command = AddUser, font = myFont)
    returnButton = tk.Button(window_register, text = "Return", command = Return, font = myFont)

    tk.Label(window_register, height = 1, width = 6, bg ='cadet blue').grid(row = 0, column = 0)
    userLabel.grid(row = 1, column = 1, sticky = "ew")
    username.grid(row = 1, column = 3, sticky = "ew")
    tk.Label(window_register, height = 1, width = 6, bg ='cadet blue').grid(row = 2, column = 2)
    passLabel.grid(row = 3, column = 1, sticky = "ew")
    password.grid(row = 3, column = 3, sticky = "ew")
    tk.Label(window_register, height = 1, width = 6, bg ='cadet blue').grid(row = 4, column = 3)
    accessLabel.grid(row = 5, column = 1, sticky = "ew")
    accessLevel.grid(row = 5, column = 3, sticky = "ew")
    tk.Label(window_register, height = 1, width = 6, bg ='cadet blue').grid(row = 6, column = 4)
    registerButton.grid(row = 7, column = 2, sticky = "ew")
    tk.Label(window_register, height = 1, width = 6, bg ='cadet blue').grid(row = 8, column = 4)
    returnButton.grid(row = 9, column = 2, sticky = "ew")
    tk.Label(window_register, height = 1, width = 6, bg ='cadet blue').grid(row = 10, column = 4)

    window_register.mainloop()
