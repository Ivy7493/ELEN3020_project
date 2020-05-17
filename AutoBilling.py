import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import LoggingAPI
import time
import datetime
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
from datetime import date
from datetime import datetime
from tkinter import *
from tkcalendar import *
from fpdf import FPDF

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

def CreateStoringPDF(_conn, _clientName, _streetAddress, _city, _country, _postalCode, _sampleArray, _rateArray, _fridgeArray):
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
        pdf.cell(pdf.width_cell[0], 10, "SAMPLE ID", 1, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, "SAMPLE TYPE", 1, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "FRIDGE ID", 1,0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "RATE", 1,1, 'L')

        subtotal = 0
        count = 0
        for sample in _sampleArray:            
            pdf.width_cell = [70, 40, 40, 40]
            pdf.cell(pdf.width_cell[0], 10, sample[0], 1, 0, 'L') 
            pdf.cell(pdf.width_cell[1], 10, sample[5], 1, 0, 'L')
            pdf.cell(pdf.width_cell[2], 10, str(_fridgeArray[count]), 1, 0, 'L')
            pdf.cell(pdf.width_cell[3], 10, "R"+str(_rateArray[count]), 1, 1, 'L')
            subtotal = subtotal + _rateArray[count]
            count = count + 1

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "SUBTOTAL:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(subtotal), 0, 1, 'L')
        
        taxRate = 15
        taxAmount = float(subtotal) * float(taxRate) / 100

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "(TAX RATE):", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, str(taxRate) + "%", 0, 1, 'L')

        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "TAX:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(round(taxAmount, 2)), 0, 1, 'L')

        pdf.width_cell = [120,50]
        pdf.cell(pdf.width_cell[0], 10, "   ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[1], 10, "   ", 0, 1, 'L')

        total = float(subtotal) + float(taxAmount)
        pdf.width_cell = [70, 40, 40, 40]
        pdf.cell(pdf.width_cell[0], 10, " ", 0, 0, 'L') 
        pdf.cell(pdf.width_cell[1], 10, " ", 0, 0, 'L')
        pdf.cell(pdf.width_cell[2], 10, "TOTAL:", 0, 0, 'L')
        pdf.cell(pdf.width_cell[3], 10, "R"+str(round(total,2)), 0, 1, 'L')

        pdf.output("Invoices/Invoice" + str(index)+".pdf")  

        invoiceMessage = ("Invoiced " + _clientName + " for storing samples in the biobank for the month of " + str(invoiceDate.strftime('%B')) + " (TOTAL: R"+ str(round(total,2)) + ")")
        return invoiceMessage
    except:
        return "FALSE"   

def AutoBilling(_conn):
    c = _conn.cursor()
    c.execute("SELECT * FROM CollectionTable")
    results = c.fetchall()

    messageArray = []
    count = 0

    for collectionInfo in results:
        collectionTitle = collectionInfo[0]
        clientName = collectionInfo[2]
        clientPhoneNumber = collectionInfo[3]
        clientEmail = collectionInfo[4]
        clientOrganization = collectionInfo[5]
        clientStreet = collectionInfo[6]
        clientCity = collectionInfo[7]
        clientCountry = collectionInfo[8]
        clientPostalCode = collectionInfo[9]
        
        sampleArray = []
        fridgeRateArray = []
        fridgeIDArray = []

        c.execute("SELECT * FROM SampleTable WHERE collectionTitle = ?", (collectionTitle,))
        sampleResults = c.fetchall()
        for sampleResult in sampleResults:
            sampleArray.append(sampleResult) 
            sampleID = sampleResult[0]
            fridgeID = DataAPI.ReturnFridgeSampleIn(_conn, sampleID)
            fridgeIDArray.append(fridgeID)
            c.execute("SELECT rate FROM FridgeTable WHERE fridgeID = ?", (fridgeID,))
            fridgeRate = c.fetchone()[0]
            fridgeRateArray.append(fridgeRate)
        
        invoiceStatus =  CreateStoringPDF(_conn, clientName, clientStreet, clientCity, clientCountry, clientPostalCode, sampleArray, fridgeRateArray, fridgeIDArray)
        if invoiceStatus == "FALSE":
            messageArray.append("ERROR invoicing client " + clientName)
        else:
            #REMOVE THIS IF WE DON'T WANT TO DISPLAY THE SUCCESSFUL INVOICES
            messageArray.append(invoiceStatus)
            LoggingAPI.Log(_conn, invoiceStatus)
    stringMessage = ""
    for message in messageArray:
        stringMessage = stringMessage + '\n' + message
    MessagePopup(stringMessage, "INVOICE RESULT")

