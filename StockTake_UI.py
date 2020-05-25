import sqlite3
import tkinter as tk
import Main_UI
import DataAPI
from tkinter import ttk
from tkinter.font import Font

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

##########---------->START: STOCK TAKE WINDOW<--------------------##########
def MainStockTake_Window(conn):
    window_StockTake = tk.Tk()
    window_StockTake.title("STOCK TAKE MENU")
    window_StockTake["bg"] = 'cadet blue'
    
    text = tk.Text(window_StockTake)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_StockTake, text = 'Type', bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 1, column=1, sticky = "ew")
    queryType = ttk.Combobox(window_StockTake, state = "readonly", values=['Fridges', 'Boxes', 'Samples'])
    queryType.grid(row = 1, column = 2, sticky = "ew")

    tk.Label(window_StockTake, text = 'Number', bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 2, column=1, sticky = "ew")
    number = tk.Entry(window_StockTake)
    number.grid(row = 2, column = 2, sticky = "ew")

    def StockTake_Window():
        _queryType = queryType.get()
        _number = number.get()
        try:
            _number = int(_number)
            intCheck = "TRUE"
        except:
            intCheck = "FALSE"
        if any([_queryType == "", _number == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        elif intCheck == "FALSE":
            MessagePopup("Please enter an integer value", "ERROR")
        else:
            try:
                messageText = DataAPI.StockTake(conn, _number, _queryType)
                MessagePopup(messageText, "Stock Take Result")
            except:
                MessagePopup("ERROR: Invalid data entered", "Stock Take Result")

    def Return():
        window_StockTake.destroy()
        Main_UI.Main_Window(conn)

    tk.Button(window_StockTake, text = 'Check', command = StockTake_Window, font=myFont).grid(row = 3, column=2, sticky = "ew")
    tk.Button(window_StockTake, text = 'Return', command = Return, font=myFont).grid(row = 5, column=2, sticky = "ew")

    tk.Label(window_StockTake, height = 1, width = 2, bg = 'cadet blue').grid(row=0, column=3)
    tk.Label(window_StockTake, height = 1, width = 2, bg = 'cadet blue').grid(row=4, column=0)
    tk.Label(window_StockTake, height = 1, width = 2, bg = 'cadet blue').grid(row=6, column=0)

    window_StockTake.mainloop()
##########---------->END: EDIT WINDOW<----------------------##########
