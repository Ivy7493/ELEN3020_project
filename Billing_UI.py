import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import LoggingAPI
import time
import datetime
import AutoBilling
from tkinter import ttk
from datetime import date
from datetime import datetime
from tkinter import *
from tkcalendar import *
from fpdf import FPDF
from tkinter.font import Font


def MessagePopup(messageText, messageTitle):
    message_window = tk.Tk()
    message_window.title(messageTitle)

    text = tk.Text(message_window)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    message_window["bg"] = 'cadet blue'
    message = tk.Label(message_window, text = messageText, font = myFont, bg = 'cadet blue', wraplength = 400, justify = "center")
    message.grid(row = 0, column = 0)

    def CloseMessage():
        message_window.destroy()

    backButton = tk.Button(message_window, text = 'Close', command = CloseMessage, font = myFont).grid(row=1) 
    tk.Label(message_window, height = 1, width = 2, bg="cadet blue").grid(row = 2)
    message_window.mainloop()

def MainBilling_Window(conn):
    window_MainBilling = tk.Tk()
    window_MainBilling.title("INVOICE")
    window_MainBilling["bg"] = 'cadet blue'

    text = tk.Text(window_MainBilling)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def RunAutoBilling():
        MessagePopup(AutoBilling.AutoBilling(conn), "INVOICE RESULT")

    def RunNewSampleBilling():
        MessagePopup(AutoBilling.BillNewSamples(conn), "INVOICE RESULT")

    def Return():
        window_MainBilling.destroy()
        Main_UI.Main_Window(conn)

    tk.Button(window_MainBilling, text = 'Invoice for New Samples', command = RunNewSampleBilling, font = myFont).grid(row = 1, column=1, sticky = "ew")
    tk.Button(window_MainBilling, text = 'Invoice for Storage', command = RunAutoBilling, font = myFont, bg = "red").grid(row = 3, column=1, sticky = "ew")
    tk.Button(window_MainBilling, text = 'Return', command = Return, font = myFont).grid(row = 5, column=1, sticky = "ew")

    tk.Label(window_MainBilling, height = 1, width = 6, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_MainBilling, height = 1, width = 6, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_MainBilling, height = 1, width = 6, bg="cadet blue").grid(row =4, column =2)
    tk.Label(window_MainBilling, height = 1, width = 6, bg="cadet blue").grid(row =6, column =2)

    window_MainBilling.mainloop()


