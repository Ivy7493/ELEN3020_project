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


##########---------->START: ADD SAMPLES AUTO WINDOW<--------------------##########
def AddSamples(conn):
    window_Check = tk.Tk()
    window_Check.title("CONFIRM")
    window_Check["bg"] = 'cadet blue'
    text = tk.Text(window_Check)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)
    
    space0 = tk.Label(window_Check, height = 1, bg = 'cadet blue').grid(row = 0, column = 0)
    space2 = tk.Label(window_Check, height = 1, bg = 'cadet blue').grid(row=2, column=0)
    space4 = tk.Label(window_Check, height = 1, bg = 'cadet blue').grid(row=4, column=0)
    space6 = tk.Label(window_Check, height = 1, bg = 'cadet blue').grid(row=6, column=0)


    lbl1 = tk.Label(window_Check, height = 1, bg = 'cadet blue', text = "Have you added the CSV file to the ToAdd folder?")
    lbl1.grid(row = 1, column = 0)

    btn1 = tk.Button()
    btn2 = tk.Button()

    def Confirm():
        lbl1.config(text = "Please enter the name of the CSV file:")
        lbl3 = tk.Label(window_Check, height = 1, bg = 'cadet blue', text = ".txt").grid(row = 1, column = 2)
        fileName = tk.Entry(window_Check)
        fileName.grid(row = 1, column = 1)


        def Return():
            window_Check.destroy()
            Main_Window(conn)

        def AutoAdd():
            result = DataAPI.CommitAuto(conn, fileName.get())
            if result == "TRUE":
                messagebox.showinfo("Success", "Successfully added all samples!")
                Return()

            else:
                messagebox.showinfo("Error", result)
                Return()
                
        btn1.config(text = "Confirm", command = AutoAdd)
        btn2.config(text = "Return", command = Return)
       


    def Cancel():
        window_Check.destroy()

    btn1 = tk.Button(window_Check, text = 'Yes', command = Confirm, font=myFont)
    btn1.grid(row = 3, column=0)

    btn2 = tk.Button(window_Check, text = 'No', command = Cancel, font=myFont)
    btn2.grid(row = 5, column=0)
    window_Check.mainloop()
##########---------->END: ADD SAMPLES AUTO WINDOW<--------------------##########

##########---------->START: MAIN AUTO WINDOW<--------------------##########
def Main_Window(conn):
    window_Main = tk.Tk()
    window_Main.title("AUTO ADD MENU")
    window_Main["bg"] = 'cadet blue'
    
    text = tk.Text(window_Main)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def Open_AddSamples():
        window_Main.destroy()
        AddSamples(conn)


    def Return():
        window_Main.destroy()
        Main_UI.Edit_Window(conn)

    tk.Label(window_Main, height = 1, width = 6, bg = 'cadet blue').grid(row=0, column=2)
    tk.Button(window_Main, text = 'Add Samples', command = Open_AddSamples, font=myFont).grid(row = 1, column=1, sticky = "ew")
    tk.Label(window_Main, height = 1, width = 6, bg = 'cadet blue').grid(row=2, column=0)

    tk.Button(window_Main, text = 'Return', command = Return, font=myFont).grid(row = 3, column=1, sticky = "ew")
    tk.Label(window_Main, height = 1, width = 6, bg = 'cadet blue').grid(row=4, column=0)

    window_Main.mainloop()
##########---------->END: MAIN AUTO WINDOW<----------------------##########
