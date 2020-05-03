import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import time
import datetime
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
from datetime import date
from tkinter import *
from tkcalendar import *


def Open_SuggestBox_Window(conn):
    def SuggestBox():
        messagebox.showinfo("Suggest Box", DataAPI.FindEmptyBox(conn, int(minTemp.get()), int(maxTemp.get())))
        window_SuggestBox.destroy()

    window_SuggestBox = tk.Tk()
    #window_SuggestBox.geometry("300x300")
    window_SuggestBox.title("SUGGEST BOX")
    window_SuggestBox["bg"] = 'cadet blue'

    text = tk.Text(window_SuggestBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_SuggestBox, text = "Minimum Temperature", font=myFont, bg = "cadet blue").grid(row = 0)
    minTemp = tk.Entry(window_SuggestBox)
    minTemp.grid(row = 0, column = 1)

    tk.Label(window_SuggestBox, text = "Maximum Temperature", font=myFont, bg = "cadet blue").grid(row = 1)
    maxTemp = tk.Entry(window_SuggestBox)
    maxTemp.grid(row = 1, column = 1)

    tk.Button(window_SuggestBox, text = 'Suggest Box', 
                        command = SuggestBox, font=myFOnt).grid(row = 2, column=1)


##########---------->START: WINDOW FOR ADDING SAMPLE<----------##########
def AddSample_Window(conn):
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
            _subjectAge = int(subjectAge.get())
            _tubeRating = int(tubeRating.get())
            _collectionTitle = collectionTitle.get()
            _returnType = returnType.get()
            _returnDate = returnDate.get()
            _phenotypeValue = phenotypeValue.get()
            _diseaseState = diseaseState.get()

            messagebox.showinfo("Add Sample", DataAPI.AddSample(conn, _sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState))
        except:
            messagebox.showinfo("Add Sample", "ERROR: Invalid data entered")

    def RefreshCollectionTitlesList():
        valuesList = GetCollectionTitles()
        collectionTitle['values'] = valuesList 
        
    def Open_AddNewCollection_Window():
        def AddCollection():
            #try:
            _collectionTitle = newCollectionTitle.get()
            _donorName = donorName.get()
            _donorPhone = donorPhone.get()
            _donorEmail = donorEmail.get()
            _donorOrganization = donorOrganization.get()
            _authorisorName = authorisorName.get()
            _authorisorPhone = authorisorPhone.get()
            _authorisorEmail = authorisorEmail.get()
            _authorisorOrganization = authorisorOrganization.get()

            messagebox.showinfo("Add Collection", DataAPI.AddCollection(conn, _collectionTitle, _donorName, _donorPhone, _donorEmail, _donorOrganization, _authorisorName, _authorisorPhone, _authorisorEmail, _authorisorOrganization))
            
            RefreshCollectionTitlesList()
            
            window_Collection.destroy()
            #except:
                #messagebox.showinfo("Add Collection", "ERROR: Invalid data entered")

        window_Collection = tk.Tk()
        #window_Collection.geometry("300x300")
        window_Collection.title("COLLECTION")
        window_Collection["bg"] = 'cadet blue'

        text = tk.Text(window_Collection)
        myFont = Font(family="fixedsys", size=12)
        text.configure(font=myFont)

        tk.Label(window_Collection, text = "Collection Title", font = myFont, bg = "cadet blue").grid(row = 0)
        newCollectionTitle = tk.Entry(window_Collection)
        newCollectionTitle.grid(row = 0, column = 1)

        tk.Label(window_Collection, text = "Donor Name", font = myFont, bg = "cadet blue").grid(row = 1)
        donorName = tk.Entry(window_Collection)
        donorName.grid(row = 1, column = 1)

        tk.Label(window_Collection, text = "Donor Phone", font = myFont, bg = "cadet blue").grid(row = 2)
        donorPhone = tk.Entry(window_Collection)
        donorPhone.grid(row = 2, column = 1)

        tk.Label(window_Collection, text = "Donor Email", font = myFont, bg = "cadet blue").grid(row = 3)
        donorEmail = tk.Entry(window_Collection)
        donorEmail.grid(row = 3, column = 1)

        tk.Label(window_Collection, text = "Donor Organization", font = myFont, bg = "cadet blue").grid(row = 4)
        donorOrganization = tk.Entry(window_Collection)
        donorOrganization.grid(row = 4, column = 1)

        tk.Label(window_Collection, text = "Authorisor Name", font = myFont, bg = "cadet blue").grid(row = 5)
        authorisorName = tk.Entry(window_Collection)
        authorisorName.grid(row = 5, column = 1)

        tk.Label(window_Collection, text = "Authorisor Phone", font = myFont, bg = "cadet blue").grid(row = 6)
        authorisorPhone = tk.Entry(window_Collection)
        authorisorPhone.grid(row = 6, column = 1)

        tk.Label(window_Collection, text = "Authorisor Email", font = myFont, bg = "cadet blue").grid(row = 7)
        authorisorEmail = tk.Entry(window_Collection)
        authorisorEmail.grid(row = 7, column = 1)

        tk.Label(window_Collection, text = "Authorisor Organization", font = myFont, bg = "cadet blue").grid(row = 8)
        authorisorOrganization = tk.Entry(window_Collection)
        authorisorOrganization.grid(row = 8, column = 1)

        tk.Button(window_Collection, text = 'Add New Collection', 
                            command = AddCollection, font = myFont).grid(row = 9, column=1)

    def console_PrintSample():
        print("Sample ID: %s\nBox ID: %s\nBox X: %s\nBox Y: %s\nBox Z: %s\nSample Type: %s\nCountry of Origin: %s\nCollection Date: %s\nSubject Age: %s\nTube Rating: %s\nCollection Title: %s\nReturn or Destroy?: %s\nReturn or Destroy Date: %s\nPhenotype Value: %s\nDisease State Value: %s" % 
        (sampleID.get(), boxID.get(), boxX.get(), boxY.get(), boxZ.get(), sampleType.get(), originCountry.get(), collectionDate.get(), subjectAge.get(), tubeRating.get(), collectionTitle.get(), returnType.get(), returnDate.get(), phenotypeValue.get(), diseaseState.get()))

    def Open_MainSample_Window():
        window_AddSample.destroy()
        MainSample_Window(conn)

    def GetCollectionTitles():
        return(DataAPI.GetCollectionTitles(conn))

    def Open_SuggestBox():
        Open_SuggestBox_Window(conn)

    window_AddSample = tk.Tk()
    #window_AddSample.geometry("300x300")
    window_AddSample.title("ADD SAMPLE")
    window_AddSample["bg"] = 'cadet blue'

    text = tk.Text(window_AddSample)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_AddSample, text = "Sample ID", font = myFont, bg = "cadet blue").grid(row = 0)
    sampleID = tk.Entry(window_AddSample)
    sampleID.grid(row = 0, column = 1)

    tk.Label(window_AddSample, text = "Box ID", font = myFont, bg = "cadet blue").grid(row = 1)
    boxID = tk.Entry(window_AddSample)
    boxID.grid(row = 1, column = 1)

    tk.Label(window_AddSample, text = "Box Width (X)", font = myFont, bg = "cadet blue").grid(row = 2)
    boxX = tk.Entry(window_AddSample)
    boxX.grid(row = 2, column = 1)

    tk.Label(window_AddSample, text = "Box Length (Y)", font = myFont, bg = "cadet blue").grid(row = 3)
    boxY = tk.Entry(window_AddSample)
    boxY.grid(row = 3, column = 1)

    tk.Label(window_AddSample, text = "Box Height (Z)", font = myFont, bg = "cadet blue").grid(row = 4)
    boxZ = tk.Entry(window_AddSample)
    boxZ.grid(row = 4, column = 1)

    tk.Label(window_AddSample, text = "Sample Type", font = myFont, bg = "cadet blue").grid(row = 5)
    sampleType = ttk.Combobox(window_AddSample, state="readonly", values=DataAPI.GetSampleTypes()) 
    sampleType.grid(row = 5, column = 1)

    tk.Label(window_AddSample, text = "Country of Origin", font = myFont, bg = "cadet blue").grid(row = 6)
    originCountry = tk.Entry(window_AddSample)
    originCountry.grid(row = 6, column = 1)

    tk.Label(window_AddSample, text = "Collection Date", font = myFont, bg = "cadet blue").grid(row = 7)
    collectionDate = DateEntry(window_AddSample)
    collectionDate.grid(row = 7, column = 1)

    todaysDate = time.time()
    entryDate = str(datetime.datetime.fromtimestamp(todaysDate).strftime('%Y-%m-%d %H:%M%S'))

    sampleHistory = "INSERT REFERENCE HERE"

    tk.Label(window_AddSample, text = "Age of Subject", font = myFont, bg = "cadet blue").grid(row = 8)
    subjectAge = tk.Entry(window_AddSample)
    subjectAge.grid(row = 8, column = 1)

    tk.Label(window_AddSample, text = "Tube Minimum Temperature", font = myFont, bg = "cadet blue").grid(row = 9)
    tubeRating = tk.Entry(window_AddSample)
    tubeRating.grid(row = 9, column = 1)

    tk.Label(window_AddSample, text = "Collection Title", font = myFont, bg = "cadet blue").grid(row = 10)
    valuesList = GetCollectionTitles()
    collectionTitle = ttk.Combobox(window_AddSample, state="readonly", values = valuesList) 
    collectionTitle.grid(row = 10, column = 1)

    tk.Label(window_AddSample, text = "Return or Destroy?", font = myFont, bg = "cadet blue").grid(row = 11)
    returnType = ttk.Combobox(window_AddSample, state="readonly", values=["Return", "Destroy"])
    returnType.grid(row = 11, column = 1)

    tk.Label(window_AddSample, text = "Date of Return/Destroy", font = myFont, bg = "cadet blue").grid(row = 12)
    returnDate = DateEntry(window_AddSample)
    returnDate.grid(row = 12, column = 1)

    tk.Label(window_AddSample, text = "Phenotype Value", font = myFont, bg = "cadet blue").grid(row = 13)
    phenotypeValue = tk.Entry(window_AddSample)
    phenotypeValue.grid(row = 13, column = 1)

    tk.Label(window_AddSample, text = "Disease State Value", font = myFont, bg = "cadet blue").grid(row = 14)
    diseaseState = tk.Entry(window_AddSample)
    diseaseState.grid(row = 14, column = 1)

    tk.Button(window_AddSample, text = 'Print Sample to Console', 
                        command = console_PrintSample).grid(row = 15, column=1)

    tk.Button(window_AddSample, text = 'Add Sample', command = CreateSample, font=myFont).grid(row = 16, column=1)

    tk.Button(window_AddSample, text = 'Suggest Box', command = Open_SuggestBox, font=myFont).grid(row = 1, column=3)

    tk.Button(window_AddSample, text = 'Add New Collection', command = Open_AddNewCollection_Window, font=myFont).grid(row = 10, column=3)

    tk.Button(window_AddSample, text = 'Back to Sample Menu', 
                        command = Open_MainSample_Window, font=myFont).grid(row = 17, column=1)

    window_AddSample.mainloop()
##########---------->END: WINDOW FOR ADDING SAMPLE<----------##########

##########---------->START: WINDOW FOR ADDING SAMPLE TEST<----------##########
def AddSampleTest_Window(conn):
    def CreateSampleTest():
        try:
            _sampleID = sampleID.get()
            _testType = testType.get()
            _testResult = testResult.get()

            messagebox.showinfo("Add Sample Test", DataAPI.AddSampleTest(conn, _sampleID,  _testType, _testResult))
        except:
            messagebox.showinfo("Add Sample Test", "ERROR: Invalid data entered")

    def console_PrintSampleTest():
        print("Sample ID: %s\nTest Type: %s\nTestResult: %s" % 
        (sampleID.get(), testType.get(), testResult.get()))

    def Open_MainSample_Window():
        window_AddSampleTest.destroy()
        MainSample_Window(conn)
      
    window_AddSampleTest = tk.Tk()
    #window_AddSampleTest.geometry("300x300")
    window_AddSampleTest.title("ADD SAMPLE TEST")
    window_AddSampleTest["bg"] = 'cadet blue'

    text = tk.Text(window_AddSampleTest)
    myFont = Font(family="fixedsys", size = 12)
    text.configure(font=myFont)

    tk.Label(window_AddSampleTest, text = "Sample ID", font=myFont, bg="cadet blue").grid(row = 0)
    sampleID = tk.Entry(window_AddSampleTest)
    sampleID.grid(row = 0, column = 1)

    tk.Label(window_AddSampleTest, text = "Test Type", font=myFont, bg="cadet blue").grid(row = 1)
    testType = tk.Entry(window_AddSampleTest)
    testType.grid(row = 1, column = 1)

    tk.Label(window_AddSampleTest, text = "Test Result", font=myFont, bg="cadet blue").grid(row = 2)
    testResult = tk.Entry(window_AddSampleTest)
    testResult.grid(row = 2, column = 1)

    tk.Button(window_AddSampleTest, text = 'Print Sample Test to Console', 
                        command = console_PrintSampleTest, font=myFont).grid(row = 3, column=1)
    tk.Button(window_AddSampleTest, text = 'Add Sample Test', command = CreateSampleTest, font=myFont).grid(row = 4, column=1)

    tk.Button(window_AddSampleTest, text = 'Back to Sample Menu', 
                        command = Open_MainSample_Window, font=myFont).grid(row = 5, column=1)

    window_AddSampleTest.mainloop()
##########---------->END: WINDOW FOR ADDING SAMPLE<----------##########

##########---------->START: WINDOW FOR MOVING SAMPLE<----------##########
def MoveSample_Window(conn):
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
        MainSample_Window(conn)

    def Open_SuggestBox():
        Open_SuggestBox_Window(conn)

    window_MoveSample = tk.Tk()
    #window_MoveSample.geometry("300x300")
    window_MoveSample.title("MOVE SAMPLE")
    window_MoveSample["bg"] = 'cadet blue'

    text = tk.Text(window_MoveSample)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_MoveSample, text = "Move sample with SampleID:", font=myFont, bg="cadet blue").grid(row = 0)
    sampleID = tk.Entry(window_MoveSample)
    sampleID.grid(row = 0, column = 1)

    tk.Label(window_MoveSample, text = "To box with BoxID:", font=myFont, bg="cadet blue").grid(row = 1)
    boxID = tk.Entry(window_MoveSample)
    boxID.grid(row = 1, column = 1)

    tk.Label(window_MoveSample, text = "Box X position:", font=myFont, bg="cadet blue").grid(row = 2)
    boxX = tk.Entry(window_MoveSample)
    boxX.grid(row = 2, column = 1)

    tk.Label(window_MoveSample, text = "Box Y position:", font=myFont, bg="cadet blue").grid(row = 3)
    boxY = tk.Entry(window_MoveSample)
    boxY.grid(row = 3, column = 1)

    tk.Label(window_MoveSample, text = "Box Z position:", font=myFont, bg="cadet blue").grid(row = 4)
    boxZ = tk.Entry(window_MoveSample)
    boxZ.grid(row = 4, column = 1)

    tk.Button(window_MoveSample, text = 'Move Sample', command = MoveSample, font=myFont).grid(row = 5, column=1)
    tk.Button(window_MoveSample, text = 'Back to Sample Menu', 
                        command = Open_MainSample_Window, font=myFont).grid(row = 10, column=1)

    tk.Button(window_MoveSample, text = 'Suggest Box', command = Open_SuggestBox_Window, font=myFont).grid(row = 1, column=3)

    window_MoveSample.mainloop()
##########---------->END: WINDOW FOR MOVING SAMPLE<----------##########


##########---------->START: WINDOW FOR DELETING SAMPLE<----------##########
def DeleteSample_Window(conn):
    def deleteSample():
        _sampleID = sampleID.get()
        messagebox.showinfo("Delete Sample", DataAPI.DeleteSample(conn, _sampleID))
        
    def Open_MainSample_Window():
        window_DeleteSample.destroy()
        MainSample_Window(conn)

    window_DeleteSample = tk.Tk()
    #window_DeleteSample.geometry("300x300")
    window_DeleteSample.title("DELETE SAMPLE")
    window_DeleteSample["bg"] = 'cadet blue'

    text = tk.Text(window_DeleteSample)
    myFont = Font(family="fixedsys",size=12)
    text.configure(font=myFont)

    tk.Label(window_DeleteSample, text = "Delete sample with SampleID: ", font=myFont, bg="cadet blue").grid(row = 0)
    sampleID = tk.Entry(window_DeleteSample)
    sampleID.grid(row = 0, column = 1)

    tk.Button(window_DeleteSample, text = 'Delete Sample', command = deleteSample, font=myFont).grid(row = 5, column=1)
    tk.Button(window_DeleteSample, text = 'Back to Sample Menu', 
                        command = Open_MainSample_Window, font=myFont).grid(row = 10, column=1)

    window_DeleteSample.mainloop()
##########---------->END: WINDOW FOR DELETING SAMPLE<----------##########



##########---------->START: MAIN WINDOW FOR SAMPLES<----------##########
def MainSample_Window(conn):
    window_MainSample = tk.Tk()
    window_MainSample.geometry("300x300")
    window_MainSample.title("SAMPLE MENU")
    window_MainSample["bg"]='cadet blue'

    text = tk.Text(window_MainSample)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def Open_AddSample_Window():
        window_MainSample.destroy()
        AddSample_Window(conn)

    def Open_MoveSample_Window():
        window_MainSample.destroy()
        MoveSample_Window(conn)

    def Open_DeleteSample_Window():
        window_MainSample.destroy()
        DeleteSample_Window(conn)

    def Open_SampleTest_Window():
        window_MainSample.destroy()
        AddSampleTest_Window(conn)

    def Open_MainMenu_Window():
        window_MainSample.destroy()
        Main_UI.Edit_Window(conn)

    tk.Label(window_MainSample, text="", width=6, height=1, bg='cadet blue').grid(row=0,column=1)
    tk.Button(window_MainSample, text = 'Add Sample', 
                        command = Open_AddSample_Window, font=myFont).grid(row = 1, column=1, sticky="ew")
    tk.Label(window_MainSample, text="", width=6, height=1, bg='cadet blue').grid(row=2, column=0)
    tk.Button(window_MainSample, text = 'Move Sample', 
                        command = Open_MoveSample_Window, font=myFont).grid(row = 3, column=1, sticky="ew")
    tk.Label(window_MainSample, text="", width=6, height=1, bg='cadet blue').grid(row=4, column=0)
    tk.Button(window_MainSample, text = 'Delete Sample', 
                        command = Open_DeleteSample_Window, font=myFont).grid(row =5, column=1, sticky="ew")
    tk.Label(window_MainSample, text="", width=6, height=1, bg='cadet blue').grid(row=6, column=0)
    tk.Button(window_MainSample, text = 'Add Sample Test', 
                        command = Open_SampleTest_Window, font=myFont).grid(row = 7, column=1, sticky="ew")
    tk.Label(window_MainSample, text="", width=6, height=1, bg='cadet blue').grid(row=8, column=0)
    tk.Button(window_MainSample, text = 'Back to Edit Menu', 
                        command = Open_MainMenu_Window, font=myFont).grid(row = 9, column=1, sticky="ew")
    tk.Label(window_MainSample, text="", width=6, height=1, bg='cadet blue').grid(row=10, column=0)

    window_MainSample.mainloop()
##########---------->END: MAIN WINDOW FOR SAMPLES<----------##########

