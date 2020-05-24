from tkinter.font import Font
import Main_UI
import sqlite3
import tkinter as tk
import DataAPI
import LoggingAPI
import datetime
from datetime import date
from datetime import datetime
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


##########---------->START: ADD SAMPLES AUTO WINDOW<--------------------##########
def AddSamples(conn):
    window_Check = tk.Tk()
    window_Check.title("CONFIRM")
    window_Check["bg"] = 'cadet blue'

    text = tk.Text(window_Check)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    lbl1 = tk.Label(window_Check, bg = 'cadet blue', text = "Have you added the CSV file to the ToAdd folder?", font = myFont, wraplength = 200, justify = "center")
    lbl1.grid(row = 1, column = 1)

    btn1 = tk.Button()
    btn2 = tk.Button()

    tk.Label(window_Check, height = 1, width = 2, bg = 'cadet blue').grid(row=0, column=0)
    tk.Label(window_Check, height = 1, width = 2, bg = 'cadet blue').grid(row=2, column=0)
    tk.Label(window_Check, height = 1, width = 2, bg = 'cadet blue').grid(row=4, column=0)
    tk.Label(window_Check, height = 1, width = 2, bg = 'cadet blue').grid(row=6, column=2)

    def Confirm():
        lbl1.config(text = "Please enter the name of the CSV file:")
        lbl3 = tk.Label(window_Check, height = 1, bg = 'cadet blue', text = ".txt").grid(row = 2, column = 2)
        fileName = tk.Entry(window_Check)
        fileName.grid(row = 2, column = 1)

        def Return():
            window_Check.destroy()
            Main_Window(conn)

        def AutoAdd():
            _fileName = fileName.get()
            if _fileName == "":
                MessagePopup("Please enter valid file", "ERROR")
            else:
                result = DataAPI.CommitAuto(conn, _fileName)
                if result == "TRUE":
                    MessagePopup("Successfully added all samples!","Success")
                else:
                    MessagePopup(result, "ERROR")
                
        btn1.config(text = "Confirm", command = AutoAdd)
        btn2.config(text = "Return", command = Return)

    def Cancel():
        window_Check.destroy()
        Main_Window(conn)

    btn1 = tk.Button(window_Check, text = 'Yes', command = Confirm, font=myFont)
    btn1.grid(row = 3, column=1, sticky = "ew")

    btn2 = tk.Button(window_Check, text = 'No', command = Cancel, font=myFont)
    btn2.grid(row = 5, column=1, sticky = "ew")
    window_Check.mainloop()
##########---------->END: ADD SAMPLES AUTO WINDOW<--------------------##########

##########---------->START: MAIN AUTO WINDOW<--------------------##########
def Main_Window(conn):
    window_Main = tk.Tk()
    window_Main.title("AUTO ADD MENU")
    window_Main["bg"] = 'cadet blue'
    window_Main
    
    text = tk.Text(window_Main)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def Open_AddSamples():
        window_Main.destroy()
        AddSamples(conn)


    def Return():
        window_Main.destroy()
        Main_UI.Edit_Window(conn)

    tk.Label(window_Main, text = 'Make sure to Add CSV files to the ToAdd folder', font=myFont, bg = 'cadet blue', wraplength = 200, justify = "center").grid(row=0, column=1)
    tk.Label(window_Main, height = 1, width = 6, bg = 'cadet blue').grid(row=1, column=2)
    tk.Button(window_Main, text = 'Add Samples', command = Open_AddSamples, font=myFont).grid(row = 2, column=1, sticky = "ew")
    tk.Label(window_Main, height = 1, width = 6, bg = 'cadet blue').grid(row=3, column=0)

    tk.Button(window_Main, text = 'Return', command = Return, font=myFont).grid(row = 4, column=1, sticky = "ew")
    tk.Label(window_Main, height = 1, width = 6, bg = 'cadet blue').grid(row=5, column=2)

    window_Main.mainloop()
##########---------->END: MAIN AUTO WINDOW<----------------------##########
