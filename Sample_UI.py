import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import time
import datetime
from tkinter import messagebox
from tkinter import ttk

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

##########---------->START: WINDOW FOR ADDING SAMPLE<----------##########
def AddSample_Window():
    def CreateSample():
        try:
            _sampleID = sampleID.get()
            _boxID = boxID.get()
            _boxX = int(boxX.get())
            _boxY = int(boxY.get())
            _boxZ = int(boxZ.get())
            _sampleType = sampleType.get()
            _originCountry = originCountry.get()
            _collectionDate = collectionDate.get()
            _entryDate = entryDate
            _sampleHistory = sampleHistory
            _subjectAge = int(subjectAge.get())
            _tubeRating = int(tubeRating.get())
            _collectionTitle = collectionTitle.get()
            _donorPhone = donorPhone.get()
            _authorisedPhone = authorisedPhone.get()
            _returnType = returnType.get()
            _returnDate = returnDate.get()
            _testResults = testResults.get()
            _phenotypeValue = phenotypeValue.get()
            _diseaseState = diseaseState.get()

            messagebox.showinfo("Add Sample", DataAPI.AddSample(conn, _sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _sampleHistory, _subjectAge, _tubeRating, _collectionTitle, _donorPhone, _authorisedPhone, _returnType, _returnDate, _testResults, _phenotypeValue, _diseaseState))
        except:
            messagebox.showinfo("Add Sample", "ERROR: Invalid data entered")

    def console_PrintSample():
        print("Sample ID: %s\nBox ID: %s\nBox X: %s\nBox Y: %s\nBox Z: %s\nSample Type: %s\nCountry of Origin: %s\nCollection Date: %s\nSubject Age: %s\nTube Rating: %s\nCollection Title: %s\nDonor Phone: %s\nAuthorised Phone: %s\nReturn or Destroy?: %s\nReturn or Destroy Date: %s\nTest Results: %s\nPhenotype Value: %s\nDisease State Value: %s" % 
        (sampleID.get(), boxID.get(), boxX.get(), boxY.get(), boxZ.get(), sampleType.get(), originCountry.get(), collectionDate.get(), subjectAge.get(), tubeRating.get(), collectionTitle.get(), donorPhone.get(), authorisedPhone.get(), returnType.get(), returnDate.get(), testResults.get(), phenotypeValue.get(), diseaseState.get()))

    def Open_MainSample_Window():
        window_AddSample.destroy()
        MainSample_Window()
      
    window_AddSample = tk.Tk()
    #window_AddSample.geometry("300x300")
    window_AddSample.title("ADD SAMPLE")
    window_AddSample["bg"] = 'red'

    tk.Label(window_AddSample, text = "Sample ID").grid(row = 0)
    sampleID = tk.Entry(window_AddSample)
    sampleID.grid(row = 0, column = 1)

    tk.Label(window_AddSample, text = "Box ID").grid(row = 1)
    boxID = tk.Entry(window_AddSample)
    boxID.grid(row = 1, column = 1)

    tk.Label(window_AddSample, text = "Box X").grid(row = 2)
    boxX = tk.Entry(window_AddSample)
    boxX.grid(row = 2, column = 1)

    tk.Label(window_AddSample, text = "Box Y").grid(row = 3)
    boxY = tk.Entry(window_AddSample)
    boxY.grid(row = 3, column = 1)

    tk.Label(window_AddSample, text = "Box Z").grid(row = 4)
    boxZ = tk.Entry(window_AddSample)
    boxZ.grid(row = 4, column = 1)

    tk.Label(window_AddSample, text = "Sample Type").grid(row = 5)
    sampleType = ttk.Combobox(window_AddSample, values=["Blood", "Urine", "Skin cells", "Organ tissue"]) 
    sampleType.grid(row = 5, column = 1)

    tk.Label(window_AddSample, text = "Country of Origin").grid(row = 6)
    originCountry = tk.Entry(window_AddSample)
    originCountry.grid(row = 6, column = 1)

    tk.Label(window_AddSample, text = "Collection Date").grid(row = 7)
    collectionDate = tk.Entry(window_AddSample)
    collectionDate.grid(row = 7, column = 1)

    todaysDate = time.time()
    entryDate = str(datetime.datetime.fromtimestamp(todaysDate).strftime('%Y-%m-%d %H:%M%S'))

    sampleHistory = "INSERT REFERENCE HERE"

    tk.Label(window_AddSample, text = "Age of Subject").grid(row = 8)
    subjectAge = tk.Entry(window_AddSample)
    subjectAge.grid(row = 8, column = 1)

    tk.Label(window_AddSample, text = "Tube's Rating").grid(row = 9)
    tubeRating = tk.Entry(window_AddSample)
    tubeRating.grid(row = 9, column = 1)

    tk.Label(window_AddSample, text = "Collection Title").grid(row = 10)
    collectionTitle = tk.Entry(window_AddSample)
    collectionTitle.grid(row = 10, column = 1)

    tk.Label(window_AddSample, text = "Donor Phone Number").grid(row = 11)
    donorPhone = tk.Entry(window_AddSample)
    donorPhone.grid(row = 11, column = 1)

    tk.Label(window_AddSample, text = "Authorised Phone Number").grid(row = 12)
    authorisedPhone = tk.Entry(window_AddSample)
    authorisedPhone.grid(row = 12, column = 1)

    tk.Label(window_AddSample, text = "Return or Destroy?").grid(row = 13)
    returnType = tk.Entry(window_AddSample)
    returnType.grid(row = 13, column = 1)

    tk.Label(window_AddSample, text = "Date of Return/Destroy").grid(row = 14)
    returnDate = tk.Entry(window_AddSample)
    returnDate.grid(row = 14, column = 1)

    tk.Label(window_AddSample, text = "Test Results").grid(row = 15)
    testResults = tk.Entry(window_AddSample)
    testResults.grid(row = 15, column = 1)

    tk.Label(window_AddSample, text = "Phenotype Value").grid(row = 16)
    phenotypeValue = tk.Entry(window_AddSample)
    phenotypeValue.grid(row = 16, column = 1)

    tk.Label(window_AddSample, text = "Disease Stae Value").grid(row = 17)
    diseaseState = tk.Entry(window_AddSample)
    diseaseState.grid(row = 17, column = 1)

    tk.Button(window_AddSample, text = 'Print Sample to Console', 
                        command = console_PrintSample).grid(row = 18, column=1)
    tk.Button(window_AddSample, text = 'Add Sample', command = CreateSample).grid(row = 19, column=1)

    tk.Button(window_AddSample, text = 'Back to Sample Menu', 
                        command = Open_MainSample_Window).grid(row = 20, column=1)

    window_AddSample.mainloop()
##########---------->END: WINDOW FOR ADDING SAMPLE<----------##########


##########---------->START: WINDOW FOR MOVING SAMPLE<----------##########
def MoveSample_Window():
    def MoveSample():
        try:
            _sampleID = sampleID.get()
            _boxID = boxID.get()
            _boxX = int(boxX.get())
            _boxY = int(boxY.get())
            _boxZ = int(boxZ.get())
            messagebox.showinfo("Move Sample", DataAPI.MoveSample(conn, _sampleID, _boxID, _boxX, _boxY, _boxZ))
        except:
            messagebox.showinfo("Move Sample", "ERROR: Invalid data entered")

    def Open_MainSample_Window():
        window_MoveSample.destroy()
        MainSample_Window()

    window_MoveSample = tk.Tk()
    #window_MoveSample.geometry("300x300")
    window_MoveSample.title("MOVE SAMPLE")
    window_MoveSample["bg"] = 'red'

    tk.Label(window_MoveSample, text = "Move sample with SampleID:").grid(row = 0)
    sampleID = tk.Entry(window_MoveSample)
    sampleID.grid(row = 0, column = 1)

    tk.Label(window_MoveSample, text = "To box with BoxID:").grid(row = 1)
    boxID = tk.Entry(window_MoveSample)
    boxID.grid(row = 1, column = 1)

    tk.Label(window_MoveSample, text = "Box X position:").grid(row = 2)
    boxX = tk.Entry(window_MoveSample)
    boxX.grid(row = 2, column = 1)

    tk.Label(window_MoveSample, text = "Box Y position:").grid(row = 3)
    boxY = tk.Entry(window_MoveSample)
    boxY.grid(row = 3, column = 1)

    tk.Label(window_MoveSample, text = "Box Z position:").grid(row = 4)
    boxZ = tk.Entry(window_MoveSample)
    boxZ.grid(row = 4, column = 1)

    tk.Button(window_MoveSample, text = 'Move Sample', command = MoveSample).grid(row = 5, column=1)
    tk.Button(window_MoveSample, text = 'Back to Sample Menu', 
                        command = Open_MainSample_Window).grid(row = 10, column=1)

    window_MoveSample.mainloop()
##########---------->END: WINDOW FOR MOVING SAMPLE<----------##########


##########---------->START: WINDOW FOR DELETING SAMPLE<----------##########
def DeleteSample_Window():
    def deleteSample():
        _sampleID = sampleID.get()
        messagebox.showinfo("Delete Sample", DataAPI.DeleteSample(conn, _sampleID))
        
    def Open_MainSample_Window():
        window_DeleteSample.destroy()
        MainSample_Window()

    window_DeleteSample = tk.Tk()
    #window_DeleteSample.geometry("300x300")
    window_DeleteSample.title("DELETE SAMPLE")
    window_DeleteSample["bg"] = 'red'

    tk.Label(window_DeleteSample, text = "Delete sample with SampleID: ").grid(row = 0)
    sampleID = tk.Entry(window_DeleteSample)
    sampleID.grid(row = 0, column = 1)

    tk.Button(window_DeleteSample, text = 'Delete Sample', command = deleteSample).grid(row = 5, column=1)
    tk.Button(window_DeleteSample, text = 'Back to Sample Menu', 
                        command = Open_MainSample_Window).grid(row = 10, column=1)

    window_DeleteSample.mainloop()
##########---------->END: WINDOW FOR DELETING SAMPLE<----------##########



##########---------->START: MAIN WINDOW FOR SAMPLES<----------##########
def MainSample_Window():
    window_MainSample = tk.Tk()
    window_MainSample.geometry("300x300")
    window_MainSample.title("SAMPLE MENU")

    def Open_AddSample_Window():
        window_MainSample.destroy()
        AddSample_Window()

    def Open_MoveSample_Window():
        window_MainSample.destroy()
        MoveSample_Window()

    def Open_DeleteSample_Window():
        window_MainSample.destroy()
        DeleteSample_Window()

    def Open_MainMenu_Window():
        window_MainSample.destroy()
        Main_UI.Main_Window()

    tk.Button(window_MainSample, text = 'Add Sample', 
                        command = Open_AddSample_Window).grid(row = 0, column=0)

    tk.Button(window_MainSample, text = 'Move Sample', 
                        command = Open_MoveSample_Window).grid(row = 2, column=0)

    tk.Button(window_MainSample, text = 'Delete Sample', 
                        command = Open_DeleteSample_Window).grid(row = 3, column=0)

    tk.Button(window_MainSample, text = 'Back to Main Menu', 
                        command = Open_MainMenu_Window).grid(row = 4, column=0)

    window_MainSample.mainloop()
##########---------->END: MAIN WINDOW FOR SAMPLES<----------##########



#SetupAPI.CreateAllTables(conn)   
#MainSample_Window()
#AddSample_Window()

