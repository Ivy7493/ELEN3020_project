import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import LoggingAPI
import time
import datetime
from tkinter import messagebox
from tkinter import ttk
from datetime import date
from datetime import datetime
from tkinter import *
from tkcalendar import *
from fpdf import FPDF


def CreateBuyingPDF(_clientName, _streetAddress, _city, _country, _postalCode, _sampleType, _quantity, _unitCost):
    try:    
        pdf = FPDF()
        pdf.add_page()

        indexFileIn = open("Invoices/InvoiceIndex", "r")
        index = indexFileIn.read()
        if index == "":
            index = 1
        else:
            index = int(index) + 1
        indexFileIn.close()

        indexFileOut = open("Invoices/InvoiceIndex", "w")
        indexFileOut.write(str(index))     
        indexFileOut.close()
            
        pdf.set_font("Arial", size = 42)
        pdf.cell(175, 50, txt = "INVOICE", ln = 1, align = 'C')

        pdf.set_font("Arial", size = 15)
        invoiceDate = date.today()
        invoiceNumber = "Invoice Number: " + str(index)

        pdf.width_cell = [100,50]
        pdf.cell(pdf.width_cell[0], 10, invoiceNumber, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, str(invoiceDate), 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "BILLED TO:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "Your Company Name", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, _clientName, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "123 Your Street", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, _streetAddress, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "Your City, Your Country", 0, 1, 'L')

        addressLine2 = _city + ", " + _country
        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, addressLine2, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "000-000-0000", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, _postalCode, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "youremail@company.xx", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, "DESCRIPTION", 1, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, "UNIT COST", 1, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "QTY", 1,0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "AMOUNT", 1,1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, "Purchase of: " + _sampleType, 1, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, _unitCost, 1, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, _quantity, 1, 0, 'L')

        amount = int(_quantity) * int(_unitCost)
        pdf.cell(pdf.width_cell[3], 10, "R"+str(amount), 1, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "SUBTOTAL:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(amount), 0, 1, 'L')
        
        taxRate = 15
        taxAmount = amount * taxRate / 100

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "(TAX RATE):", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, str(taxRate) + "%", 0, 1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "TAX:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(taxAmount), 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        total = amount + taxAmount
        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "TOTAL:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(total), 0, 1, 'L')

        pdf.output("Invoices/Invoice" + str(index)+".pdf")  

        invoiceMessage = ("invoiced " + _clientName + " for the potential purchase of " + _quantity + " sample(s) of " + _sampleType + " at R" + _unitCost + " per sample (TOTAL: R"+ str(total) + ")")
        return invoiceMessage   
    except:
        return "FALSE"


def CreateStoringPDF(_conn, _clientName, _streetAddress, _city, _country, _postalCode, _sampleID, _dailyRate):
    try:
        pdf = FPDF()
        pdf.add_page()

        indexFileIn = open("Invoices/InvoiceIndex", "r")
        index = indexFileIn.read()
        if index == "":
            index = 1
        else:
            index = int(index) + 1
        indexFileIn.close()

        indexFileOut = open("Invoices/InvoiceIndex", "w")
        indexFileOut.write(str(index))     
        indexFileOut.close()
            
        pdf.set_font("Arial", size = 42)
        pdf.cell(175, 50, txt = "INVOICE", ln = 1, align = 'C')

        pdf.set_font("Arial", size = 15)
        invoiceDate = date.today()
        invoiceNumber = "Invoice Number: " + str(index)

        pdf.width_cell = [100,50]
        pdf.cell(pdf.width_cell[0], 10, invoiceNumber, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, str(invoiceDate), 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "BILLED TO:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "Your Company Name", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, _clientName, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "123 Your Street", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, _streetAddress, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "Your City, Your Country", 0, 1, 'L')

        addressLine2 = _city + ", " + _country
        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, addressLine2, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "000-000-0000", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, _postalCode, 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "youremail@company.xx", 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, "DESCRIPTION", 1, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, "DAILY RATE", 1, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "DAYS", 1,0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "AMOUNT", 1,1, 'L')

        days = int(DataAPI.GetSampleDays(_conn, _sampleID))
        amount = float(_dailyRate) * float(days)

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, "Storage of sample: " + _sampleID, 1, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, str(_dailyRate), 1, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, str(days), 1, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(amount), 1, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "SUBTOTAL:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(amount), 0, 1, 'L')
        
        taxRate = 15
        taxAmount = float(amount) * float(taxRate) / 100

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "(TAX RATE):", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, str(taxRate) + "%", 0, 1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "TAX:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(taxAmount), 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        total = float(amount) + float(taxAmount)
        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "TOTAL:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(total), 0, 1, 'L')

        pdf.output("Invoices/Invoice" + str(index)+".pdf")  


        invoiceMessage = ("invoiced " + _clientName + " for storing sample " + _sampleID + " in the biobank for " + str(days) + " days at a rate of R" + _dailyRate + " per day (TOTAL: R"+ str(total) + ")")
        return invoiceMessage
    except:
        return "FALSE"   

##########---------->BILLING: MAIN WINDOW<--------------------##########
def Buying_Window(conn):
    window_Billing = tk.Tk()
    #window_Billing.geometry("250x250")
    window_Billing.title("INVOICE")
    window_Billing["bg"] = 'cyan'

    def AddSampleButton():
        tk.Label(window_Billing, text = "Sample Type").grid(row = 6)
        sampleType = ttk.Combobox(window_Billing, state="readonly", values=DataAPI.GetSampleTypes()).grid(row = 6, column = 1)

    def Return():
        window_Billing.destroy()
        MainBilling_Window(conn)

    def Exit():
        window_Billing.destroy()

    tk.Label(window_Billing, text="Client Name").grid(row=0, column = 0)
    clientName = tk.Entry(window_Billing)
    clientName.grid(row=0, column = 1)
    
    tk.Label(window_Billing, text="CLIENT ADDRESS:").grid(row=1, column = 0)

    tk.Label(window_Billing, text="Street Address").grid(row=2, column = 0)
    streetAddress = tk.Entry(window_Billing)
    streetAddress.grid(row=2, column = 1)

    tk.Label(window_Billing, text="City").grid(row=3, column = 0)
    city = tk.Entry(window_Billing)
    city.grid(row=3, column = 1)

    tk.Label(window_Billing, text="Country").grid(row=4, column = 0)
    country = tk.Entry(window_Billing)
    country.grid(row=4, column = 1)

    tk.Label(window_Billing, text="Postal Code").grid(row=5, column = 0)
    postalCode = tk.Entry(window_Billing)
    postalCode.grid(row=5, column = 1)

    #tk.Button(window_Billing, text = 'Add Sample', command = AddSampleButton).grid(row = 6)

    tk.Label(window_Billing, text = "Sample Type").grid(row = 6)
    sampleType = ttk.Combobox(window_Billing, state="readonly", values=DataAPI.GetSampleTypes())
    sampleType.grid(row = 6, column = 1)

    tk.Label(window_Billing, text = "Quantity").grid(row = 7)
    quantity = tk.Entry(window_Billing)
    quantity.grid(row=7, column = 1)
    
    def SamplesAvailable():
        messagebox.showinfo("Samples Available", DataAPI.GetAmountOfTypes(conn, sampleType.get()))

    tk.Button(window_Billing, text = "How many are available?", command = SamplesAvailable).grid(row = 7, column = 2) 

    tk.Label(window_Billing, text = "Price per Sample").grid(row = 8)
    samplePrice = tk.Entry(window_Billing)
    samplePrice.grid(row=8, column = 1)

    def CreateInvoice():    
        invoiceStatus = CreateBuyingPDF(clientName.get(), streetAddress.get(), city.get(), country.get(), postalCode.get(), sampleType.get(), quantity.get(), samplePrice.get())
        if invoiceStatus != "FALSE":
             messagebox.showinfo("Invoice Successful", "Invoice created successfully")
             LoggingAPI.Log(conn, invoiceStatus)
        else:
             messagebox.showinfo("Invoice Unsuccessful", "Error creating invoice")

    def EntryCheck():
        cN = clientName.get()
        sA = streetAddress.get()
        ci = city.get()
        co = country.get()
        pC = postalCode.get()
        sT = sampleType.get()
        qu = quantity.get()
        sP = samplePrice.get()

        try: 
            qu = int(qu)
            sP = int(sP)
            intCheck = "TRUE"
        except:
            intCheck = "FALSE"

        if any( [cN == "", sA == "", ci == "", co == "", pC == "", sT == "", qu == "", sP == ""]):
            message_window = tk.Tk()
            message_window.title("ERROR")
            message = tk.Label(message_window, text = "One or more fields are missing data")
            message.grid(row = 0, column = 0)

            def CloseMessage():
                message_window.destroy()

            backButton = tk.Button(message_window, text = 'Close', command = CloseMessage).grid(row=1)

        elif intCheck == "FALSE":
            message_window = tk.Tk()
            message_window.title("ERROR")
            message = tk.Label(message_window, text = "One or more fields are wrong data type")
            message.grid(row = 0, column = 0)

            def CloseMessage():
                message_window.destroy()

            backButton = tk.Button(message_window, text = 'Close', command = CloseMessage).grid(row=1)

        else:
            CreateInvoice()        

    tk.Button(window_Billing, text = 'Create Invoice', command = EntryCheck).grid(row = 19, column=1)#, sticky = "ew")

    tk.Button(window_Billing, text = 'Return', command = Return).grid(row = 20, column=1)#, sticky = "ew")
    #tk.Label(window_Billing, bg="cyan", text = '                 ').grid(row=3, column=0)
    tk.Button(window_Billing, text = 'Exit', command = Exit).grid(row = 21, column=1)#, sticky = "ew")

    window_Billing.mainloop()



def Storage_Window(conn):
    window_BillingStorage = tk.Tk()
    #window_Billing.geometry("250x250")
    window_BillingStorage.title("INVOICE - STORAGE")
    window_BillingStorage["bg"] = 'cyan'

    def AddSampleButton():
        tk.Label(window_BillingStorage, text = "Sample Type").grid(row = 6)
        sampleType = ttk.Combobox(window_BillingStorage, state="readonly", values=DataAPI.GetSampleTypes()).grid(row = 6, column = 1)

    def Return():
        window_BillingStorage.destroy()
        MainBilling_Window(conn)

    def Exit():
        window_BillingStorage.destroy()

    tk.Label(window_BillingStorage, text="Client Name").grid(row=0, column = 0)
    clientName = tk.Entry(window_BillingStorage)
    clientName.grid(row=0, column = 1)
    
    tk.Label(window_BillingStorage, text="CLIENT ADDRESS:").grid(row=1, column = 0)

    tk.Label(window_BillingStorage, text="Street Address").grid(row=2, column = 0)
    streetAddress = tk.Entry(window_BillingStorage)
    streetAddress.grid(row=2, column = 1)

    tk.Label(window_BillingStorage, text="City").grid(row=3, column = 0)
    city = tk.Entry(window_BillingStorage)
    city.grid(row=3, column = 1)

    tk.Label(window_BillingStorage, text="Country").grid(row=4, column = 0)
    country = tk.Entry(window_BillingStorage)
    country.grid(row=4, column = 1)

    tk.Label(window_BillingStorage, text="Postal Code").grid(row=5, column = 0)
    postalCode = tk.Entry(window_BillingStorage)
    postalCode.grid(row=5, column = 1)

    #tk.Button(window_BillingStorage, text = 'Add Sample', command = AddSampleButton).grid(row = 6)

    tk.Label(window_BillingStorage, text = "Sample ID").grid(row = 6)
    sampleID = ttk.Entry(window_BillingStorage)
    sampleID.grid(row = 6, column = 1)

    tk.Label(window_BillingStorage, text = "Daily rate").grid(row = 8)
    dailyRate = tk.Entry(window_BillingStorage)
    dailyRate.grid(row=8, column = 1)

    def CreateInvoice():
        invoiceStatus = CreateStoringPDF(conn, clientName.get(), streetAddress.get(), city.get(), country.get(), postalCode.get(), sampleID.get(), dailyRate.get())
        if invoiceStatus != "FALSE":
            messagebox.showinfo("Invoice Successful", "Invoice created successfully")
            LoggingAPI.Log(conn, invoiceStatus)
        else:
            messagebox.showinfo("Invoice Unsuccessful", "Error creating invoice")


    def EntryCheck():
        cN = clientName.get()
        sA = streetAddress.get()
        ci = city.get()
        co = country.get()
        pC = postalCode.get()
        sI = sampleID.get()
        dR = dailyRate.get()

        try: 
            dR = int(dR)
            intCheck = "TRUE"
        except:
            intCheck = "FALSE"

        if any( [cN == "", sA == "", ci == "", co == "", pC == "", sI == "", dR == ""]):
            message_window = tk.Tk()
            message_window.title("ERROR")
            message = tk.Label(message_window, text = "One or more fields are missing data")
            message.grid(row = 0, column = 0)

            def CloseMessage():
                message_window.destroy()

            backButton = tk.Button(message_window, text = 'Close', command = CloseMessage).grid(row=1)

        elif intCheck == "FALSE":
            message_window = tk.Tk()
            message_window.title("ERROR")
            message = tk.Label(message_window, text = "One or more fields are wrong data type")
            message.grid(row = 0, column = 0)

            def CloseMessage():
                message_window.destroy()

            backButton = tk.Button(message_window, text = 'Close', command = CloseMessage).grid(row=1)      

        elif DataAPI.DoesIDExist(conn, "SAMPLE", sI) == "FALSE":
            message_window = tk.Tk()
            message_window.title("ERROR")
            message = tk.Label(message_window, text = "Sample does not exist")
            message.grid(row = 0, column = 0)

            def CloseMessage():
                message_window.destroy()

            backButton = tk.Button(message_window, text = 'Close', command = CloseMessage).grid(row=1)

        else:
            CreateInvoice()


    tk.Button(window_BillingStorage, text = 'Create Invoice', command = EntryCheck).grid(row = 19, column=1)#, sticky = "ew")

    tk.Button(window_BillingStorage, text = 'Return', command = Return).grid(row = 20, column=1)#, sticky = "ew")
    #tk.Label(window_BillingStorage, bg="cyan", text = '                 ').grid(row=3, column=0)
    tk.Button(window_BillingStorage, text = 'Exit', command = Exit).grid(row = 21, column=1)#, sticky = "ew")

    window_BillingStorage.mainloop()


def MainBilling_Window(conn):
    window_MainBilling = tk.Tk()
    #window_MainBilling.geometry("250x250")
    window_MainBilling.title("INVOICE")
    window_MainBilling["bg"] = 'cyan'

    def Open_Buying_Window():
        window_MainBilling.destroy()
        Buying_Window(conn)

    def Open_Storing_Window():
        window_MainBilling.destroy()
        Storage_Window(conn)

    def Return():
        window_MainBilling.destroy()
        Main_UI.Main_Window(conn)

    def Exit():
        window_MainBilling.destroy()

    tk.Button(window_MainBilling, text = 'Invoice for Buying', command = Open_Buying_Window).grid(row = 18, column=1)#, sticky = "ew")
    tk.Button(window_MainBilling, text = 'Invoice for Storage', command = Open_Storing_Window).grid(row = 19, column=1)#, sticky = "ew")
    tk.Button(window_MainBilling, text = 'Return', command = Return).grid(row = 20, column=1)#, sticky = "ew")
    #tk.Label(window_MainBilling, bg="cyan", text = '                 ').grid(row=3, column=0)
    tk.Button(window_MainBilling, text = 'Exit', command = Exit).grid(row = 21, column=1)#, sticky = "ew")

    window_MainBilling.mainloop()


