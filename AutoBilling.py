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


def CreateStoringPDF(_conn, _clientName, _streetAddress, _city, _country, _postalCode, _sampleArray, _rateArray, _fridgeArray, _addingOrStoring):
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

        if _addingOrStoring == "adding":
            invoiceMessage = ("Invoiced " + _clientName + " for adding samples to the biobank in the month of " + str(invoiceDate.strftime('%B')) + " (TOTAL: R"+ str(round(total,2)) + ")")
        else:
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

        invoiceStatus =  CreateStoringPDF(_conn, clientName, clientStreet, clientCity, clientCountry, clientPostalCode, sampleArray, fridgeRateArray, fridgeIDArray, "storing")
        if invoiceStatus == "FALSE":
            messageArray.append("ERROR invoicing client " + clientName)
        else:
            #REMOVE THIS IF WE DON'T WANT TO DISPLAY THE SUCCESSFUL INVOICES
            messageArray.append(invoiceStatus)
            LoggingAPI.BillingLog(_conn, invoiceStatus)
    stringMessage = ""
    for message in messageArray:
        stringMessage = stringMessage + '\n' + message
    if stringMessage == "":
        stringMessage = "ERROR"
    return stringMessage

def BillNewSamples(_conn):
    c = _conn.cursor()
    c.execute("SELECT * FROM CollectionInvoiceTable")
    results = c.fetchall()
    
    collectionTitleArray = []
    sampleArray = []
    invoiceCheckArray = []
    fridgeRateArray = []
    fridgeIDArray = []

    count = 0
    noSampleCount = 0
    totalSampleCount = 0

    for row in results:
        totalSampleCount = totalSampleCount + 1
        collectionTitle = row[0]
        sampleID = row[1]
        invoiceCheck = row[2]
        if(invoiceCheck == 0):
            collectionTitleArray.append(collectionTitle)

            c.execute("SELECT * FROM SampleTable WHERE sampleID = ?", (sampleID,))
            sampleRow = c.fetchone()
            sampleArray.append(sampleRow)
            invoiceCheckArray.append(invoiceCheck)

            fridgeID = DataAPI.ReturnFridgeSampleIn(_conn, sampleID)
            fridgeIDArray.append(fridgeID)
            c.execute("SELECT rate FROM FridgeTable WHERE fridgeID = ?", (fridgeID,))
            fridgeRate = c.fetchone()[0]
            fridgeRateArray.append(fridgeRate)

            count = count + 1
        else:  
            noSampleCount = noSampleCount + 1  
    messageArray = []

    while count > 0:
        c.execute("SELECT * FROM CollectionTable WHERE collectionTitle=?",(collectionTitleArray[0],))
        collection = c.fetchone()
        collectionTitle = collection[0]
        clientName = collection[2]
        clientPhoneNumber = collection[3]
        clientEmail = collection[4]
        clientOrganization = collection[5]
        clientStreet = collection[6]
        clientCity = collection[7]
        clientCountry = collection[8]
        clientPostalCode = collection[9]
        
        tempSampleArray = []
        tempFridgeRateArray = []
        tempFridgeIDArray = []
        tempSampleArray2 = []
        tempFridgeRateArray2 = []
        tempFridgeIDArray2 = []
        tempCollectionArray2 = []

        count3 = 0
        for sample in sampleArray:
            if(collectionTitleArray[count3] == collectionTitleArray[0]):
                tempSampleArray.append(sample)
                tempFridgeRateArray.append(fridgeRateArray[count3])
                tempFridgeIDArray.append(fridgeIDArray[count3])
                count = count - 1
                c.execute("UPDATE CollectionInvoiceTable SET invoiceCheck =? WHERE sampleID =?",(1, sample[0],))
                _conn.commit()
                
            else:
                tempSampleArray2.append(sample)
                tempFridgeRateArray2.append(fridgeRateArray[count3])
                tempFridgeIDArray2.append(fridgeIDArray[count3])
                tempCollectionArray2.append(collectionTitleArray[count3])
            count3 = count3 + 1

        sampleArray = tempSampleArray2
        fridgeRateArray = tempFridgeRateArray2
        fridgeIDArray = tempFridgeIDArray2
        collectionTitleArray = tempCollectionArray2

        invoiceStatus =  CreateStoringPDF(_conn, clientName, clientStreet, clientCity, clientCountry, clientPostalCode, tempSampleArray, tempFridgeRateArray, tempFridgeIDArray, "adding")
        if invoiceStatus == "FALSE":
            messageArray.append("ERROR invoicing client " + clientName)
        else:
            #REMOVE THIS IF WE DON'T WANT TO DISPLAY THE SUCCESSFUL INVOICES
            messageArray.append(invoiceStatus)
            logMessage = " user: " + LoggingAPI.GetCurrentLogin(_conn) + " " +invoiceStatus
            LoggingAPI.BillingLog(_conn, invoiceStatus)

    stringMessage = ""
    for message in messageArray:
        stringMessage = stringMessage + '\n' + message

    messageResult = ""
    if noSampleCount != totalSampleCount:
        messageResult = stringMessage
    else:
        messageResult = "No new samples to invoice"
    return messageResult


def UpdateCollectionInvoiceTable(_conn, sampleID, collectionTitle):
    c = _conn.cursor()
    try:
        c.execute("INSERT INTO CollectionInvoiceTable (collectionTitle, sampleID, invoiceCheck) VALUES (?, ?, ?)",(collectionTitle,sampleID, 0))
        _conn.commit()
        LoggingAPI.BillingLog(_conn, "Added sample " + sampleID + " from collection " + collectionTitle + " to collection invoice table, ready to invoice")
        return("Successfully added sample " + sampleID + " to the collection invoice table, ready to invoice")
    except sqlite3.Error as error:
        return(error)  

