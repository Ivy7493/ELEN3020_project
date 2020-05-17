import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI
import Main_UI
import time
import datetime
from tkinter.font import Font
from tkinter import messagebox
from tkinter.font import Font
from tkinter import ttk
from datetime import date
from tkinter import *
from tkcalendar import *

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

def Open_SuggestBox_Window(conn):
    def SuggestBox():
        _minTemp = minTemp.get()
        _maxTemp = maxTemp.get()
        
        try:
            _minTemp = int(_minTemp)
            _maxTemp = int(_maxTemp)
            intCheck = "TRUE"
        except:
            intCheck = "FALSE"
    
        if any ([_minTemp == "", _maxTemp == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        elif intCheck == "FALSE":
            MessagePopup("One or more fields are wrong data type", "ERROR")
        else:
            messageText = DataAPI.FindEmptyBox(conn, _minTemp, _maxTemp)
            MessagePopup(messageText, "Suggest Box")
            window_SuggestBox.destroy()

    window_SuggestBox = tk.Tk()
    window_SuggestBox.title("SUGGEST BOX")
    window_SuggestBox["bg"] = 'cadet blue'

    text = tk.Text(window_SuggestBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    label1 = tk.Label(window_SuggestBox, text = "Minimum Temperature", font = myFont, bg = 'cadet blue')
    label1.grid(row = 0)
    minTemp = tk.Entry(window_SuggestBox)
    minTemp.grid(row = 0, column = 1)

    label2 = tk.Label(window_SuggestBox, text = "Maximum Temperature", font = myFont, bg = 'cadet blue')
    label2.grid(row = 1)
    maxTemp = tk.Entry(window_SuggestBox)
    maxTemp.grid(row = 1, column = 1)

    tk.Button(window_SuggestBox, text = 'Suggest Box', command = SuggestBox, font = myFont).grid(row = 2, column=1)

##########---------->START: WINDOW FOR ADDING SAMPLE<----------##########
def AddSample_Window(conn):
    def CreateSample():
        _sampleID = sampleID.get()
        _boxID = boxID.get()
        _boxX = boxX.get()
        _boxY = boxY.get()
        _boxZ = boxZ.get()
        _sampleType = sampleType.get()
        _originCountry = originCountry.get()
        _collectionDate = collectionDate.get()
        _entryDate = entryDate
        _subjectAge = subjectAge.get()
        _tubeRating = tubeRating.get()
        _collectionTitle = collectionTitle.get()
        _returnType = returnType.get()
        _returnDate = returnDate.get()
        _phenotypeValue = phenotypeValue.get()
        _diseaseState = diseaseState.get()

        try:
            _boxX = int(_boxX)
            _boxY = int(_boxY)
            _boxZ = int(_boxZ)
            _subjectAge = int(_subjectAge)
            _tubeRating = int(_tubeRating)
            intCheck = "TRUE"
        except:
            intCheck = "FALSE"
        
        if any( [_sampleID == "", _boxID == "", _boxX == "", _boxY == "", _boxZ == "", _sampleType == "", _originCountry == "",_collectionDate == "",_entryDate == "", _subjectAge== "",_tubeRating == "",_collectionTitle == "",_returnType == "", _returnDate == "", _phenotypeValue == "",_diseaseState == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        elif intCheck == "FALSE":
            MessagePopup("One or more fields are wrong data type", "ERROR")
        else:
            try:
                messageText = DataAPI.AddSample(conn, _sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState)
                MessagePopup(messageText, "Add Sample")
            except:
                MessagePopup("ERROR: Invalid data entered", "Add Sample")

    def Open_MainSample_Window():
        window_AddSample.destroy()
        MainSample_Window(conn)

    def GetCollectionTitles():
        return(DataAPI.GetCollectionTitles(conn))

    def Open_SuggestBox():
        Open_SuggestBox_Window(conn)

    window_AddSample = tk.Tk()
    window_AddSample.title("ADD SAMPLE")
    window_AddSample["bg"] = 'cadet blue'

    text = tk.Text(window_AddSample)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_AddSample, text = "Sample ID",  anchor = "w" ,bg = 'cadet blue', font=myFont).grid(row = 1, column = 1, sticky = "ew")
    sampleID = tk.Entry(window_AddSample)
    sampleID.grid(row = 1, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Box ID", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 2, column = 1, sticky = "ew")
    boxID = tk.Entry(window_AddSample)
    boxID.grid(row = 2, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Box X Position", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 3, column = 1, sticky = "ew")
    boxX = tk.Entry(window_AddSample)
    boxX.grid(row = 3, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Box Y Position", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 4, column = 1, sticky = "ew")
    boxY = tk.Entry(window_AddSample)
    boxY.grid(row = 4, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Box Z Position", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 5, column = 1, sticky = "ew")
    boxZ = tk.Entry(window_AddSample)
    boxZ.grid(row = 5, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Sample Type", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 6, column = 1, sticky = "ew")
    sampleType = ttk.Combobox(window_AddSample, state="readonly", values=DataAPI.GetSampleTypes()) 
    sampleType.grid(row = 6, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Country of Origin", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 7, column = 1, sticky = "ew")
    originCountry = tk.Entry(window_AddSample)
    originCountry.grid(row = 7, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Collection Date", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 8, column = 1, sticky = "ew")
    collectionDate = DateEntry(window_AddSample)
    collectionDate.grid(row = 8, column = 2, sticky = "ew")

    todaysDate = time.time()
    entryDate = str(datetime.datetime.fromtimestamp(todaysDate).strftime('%Y-%m-%d %H:%M%S'))

    tk.Label(window_AddSample, text = "Age of Subject", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 9, column = 1, sticky = "ew")
    subjectAge = tk.Entry(window_AddSample)
    subjectAge.grid(row = 9, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Tube Minimum Temperature", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 10, column = 1, sticky = "ew")
    tubeRating = tk.Entry(window_AddSample)
    tubeRating.grid(row = 10, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Collection Title", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 11, column = 1, sticky = "ew")
    valuesList = GetCollectionTitles()
    collectionTitle = ttk.Combobox(window_AddSample, state="readonly", values = valuesList) 
    collectionTitle.grid(row = 11, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Return or Destroy?", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 12, column = 1, sticky = "ew")
    returnType = ttk.Combobox(window_AddSample, state="readonly", values=["Return", "Destroy"])
    returnType.grid(row = 12, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Date of Return/Destroy", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 13, column = 1, sticky = "ew")
    returnDate = DateEntry(window_AddSample)
    returnDate.grid(row = 13, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Phenotype Value", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 14, column = 1, sticky = "ew")
    phenotypeValue = tk.Entry(window_AddSample)
    phenotypeValue.grid(row = 14, column = 2, sticky = "ew")

    tk.Label(window_AddSample, text = "Disease State Value", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 15, column = 1, sticky = "ew")
    diseaseState = tk.Entry(window_AddSample)
    diseaseState.grid(row = 15, column = 2, sticky = "ew")

    tk.Button(window_AddSample, text = 'Add Sample', command = CreateSample, font = myFont).grid(row = 16, column=2, sticky = "ew")
    tk.Button(window_AddSample, text = 'Suggest Box', command = Open_SuggestBox, font = myFont).grid(row = 2, column=3, sticky = "ew")
    tk.Button(window_AddSample, text = 'Back to Sample Menu', command = Open_MainSample_Window, font = myFont).grid(row = 18, column=2, sticky = "ew")

    tk.Label(window_AddSample, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_AddSample, height = 1, width = 2, bg="cadet blue").grid(row =17, column =0)
    tk.Label(window_AddSample, height = 1, width = 2, bg="cadet blue").grid(row =19, column =4)

    window_AddSample.mainloop()
##########---------->END: WINDOW FOR ADDING SAMPLE<----------##########

##########---------->START: WINDOW FOR ADDING SAMPLE TEST<----------##########
def AddSampleTest_Window(conn):
    def CreateSampleTest():
        _sampleID = sampleID.get()
        _testType = testType.get()
        _testResult = testResult.get()           

        if any( [_sampleID == "", _testType == "", _testResult == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        else:
            try:
                messageText = DataAPI.AddSampleTest(conn, _sampleID,  _testType, _testResult)
                MessagePopup(messageText, "Add Sample Test")
            except:
                MessagePopup("ERROR: Invalid data entered", "Add Sample")


    def Open_MainSample_Window():
        window_AddSampleTest.destroy()
        MainSample_Window(conn)
      
    window_AddSampleTest = tk.Tk()
    window_AddSampleTest.title("ADD SAMPLE TEST")
    window_AddSampleTest["bg"] = 'cadet blue'

    text = tk.Text(window_AddSampleTest)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_AddSampleTest, text = "Sample ID", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 1, column = 1, sticky = "ew")
    sampleID = tk.Entry(window_AddSampleTest)
    sampleID.grid(row = 1, column = 2, sticky = "ew")

    tk.Label(window_AddSampleTest, text = "Test Type", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 2, column = 1, sticky = "ew")
    testType = tk.Entry(window_AddSampleTest)
    testType.grid(row = 2, column = 2, sticky = "ew")

    tk.Label(window_AddSampleTest, text = "Test Result", bg = 'cadet blue', font=myFont, anchor = "w").grid(row = 3, column = 1, sticky = "ew")
    testResult = tk.Entry(window_AddSampleTest)
    testResult.grid(row = 3, column = 2, sticky = "ew")

    tk.Button(window_AddSampleTest, text = 'Add Sample Test', command = CreateSampleTest, font = myFont).grid(row = 4, column=2, sticky = "ew")
    tk.Button(window_AddSampleTest, text = 'Back to Sample Menu', command = Open_MainSample_Window, font = myFont).grid(row = 6, column=2, sticky = "ew")

    tk.Label(window_AddSampleTest, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_AddSampleTest, height = 1, width = 2, bg="cadet blue").grid(row =5, column =0)
    tk.Label(window_AddSampleTest, height = 1, width = 2, bg="cadet blue").grid(row =7, column =3)

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
            messageText = DataAPI.MoveSample(conn, _sampleID, _boxID, _boxX, _boxY, _boxZ)
            MessagePopup(messageText, "Move Sample")
        except:
            MessagePopup("ERROR: Invalid data entered", "Move Sample")

    def Open_MainSample_Window():
        window_MoveSample.destroy()
        MainSample_Window(conn)

    def Open_SuggestBox():
        Open_SuggestBox_Window(conn)

    window_MoveSample = tk.Tk()
    window_MoveSample.title("MOVE SAMPLE")
    window_MoveSample["bg"] = 'cadet blue'

    text = tk.Text(window_MoveSample)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    tk.Label(window_MoveSample, text = "Move sample with SampleID:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row = 1, column = 1, sticky = "ew")
    sampleID = tk.Entry(window_MoveSample)
    sampleID.grid(row = 1, column = 2, sticky = "ew")

    tk.Label(window_MoveSample, text = "To box with BoxID:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row = 2, column = 1, sticky = "ew")
    boxID = tk.Entry(window_MoveSample)
    boxID.grid(row = 2, column = 2, sticky = "ew")

    tk.Label(window_MoveSample, text = "Box X position:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row = 3, column = 1, sticky = "ew")
    boxX = tk.Entry(window_MoveSample)
    boxX.grid(row = 3, column = 2, sticky = "ew")

    tk.Label(window_MoveSample, text = "Box Y position:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row = 4, column = 1, sticky = "ew")
    boxY = tk.Entry(window_MoveSample)
    boxY.grid(row = 4, column = 2, sticky = "ew")

    tk.Label(window_MoveSample, text = "Box Z position:", font = myFont, bg = 'cadet blue', anchor = "w").grid(row = 5, column = 1, sticky = "ew")
    boxZ = tk.Entry(window_MoveSample)
    boxZ.grid(row = 5, column = 2, sticky = "ew")

    tk.Button(window_MoveSample, text = 'Move Sample', command = MoveSample, font = myFont).grid(row = 6, column=2, sticky = "ew")
    tk.Button(window_MoveSample, text = 'Back to Sample Menu', command = Open_MainSample_Window, font = myFont).grid(row = 8, column=2, sticky = "ew")
    tk.Button(window_MoveSample, text = 'Suggest Box', command = Open_SuggestBox_Window, font = myFont).grid(row = 2, column=3, sticky = "ew")

    tk.Label(window_MoveSample, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_MoveSample, height = 1, width = 2, bg="cadet blue").grid(row =7, column =0)
    tk.Label(window_MoveSample, height = 1, width = 2, bg="cadet blue").grid(row =9, column =4)

    window_MoveSample.mainloop()
##########---------->END: WINDOW FOR MOVING SAMPLE<----------##########


##########---------->START: WINDOW FOR DELETING SAMPLE<----------##########
def DeleteSample_Window(conn):
    def deleteSample():
        _sampleID = sampleID.get()
        messageText = DataAPI.DeleteSample(conn, _sampleID)
        MessagePopup(messageText, "Delete Sample")
        
    def Open_MainSample_Window():
        window_DeleteSample.destroy()
        MainSample_Window(conn)

    window_DeleteSample = tk.Tk()
    window_DeleteSample.title("DELETE SAMPLE")
    window_DeleteSample["bg"] = 'cadet blue'

    text = tk.Text(window_DeleteSample)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    label = tk.Label(window_DeleteSample, text = "Delete sample with SampleID: ", font = myFont, bg = 'cadet blue', anchor = "w")
    label.grid(row = 1, column = 1, sticky = "ew")
    sampleID = tk.Entry(window_DeleteSample)
    sampleID.grid(row = 1, column = 2, sticky = "ew")

    tk.Button(window_DeleteSample, text = 'Delete Sample', command = deleteSample).grid(row = 2, column=2, sticky = "ew")
    tk.Button(window_DeleteSample, text = 'Back to Sample Menu', command = Open_MainSample_Window).grid(row = 4, column=2, sticky = "ew")

    tk.Label(window_DeleteSample, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_DeleteSample, height = 1, width = 2, bg="cadet blue").grid(row =3, column =0)
    tk.Label(window_DeleteSample, height = 1, width = 2, bg="cadet blue").grid(row =5, column =3)

    window_DeleteSample.mainloop()
##########---------->END: WINDOW FOR DELETING SAMPLE<----------##########


##########---------->START: MAIN WINDOW FOR SAMPLES<----------##########
def MainSample_Window(conn):
    window_MainSample = tk.Tk()
    window_MainSample.title("SAMPLE MENU")
    window_MainSample["bg"] = 'cadet blue'

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

    tk.Button(window_MainSample, text = 'Add Sample', command = Open_AddSample_Window, font = myFont).grid(row = 1, column=1, sticky = "ew")
    tk.Button(window_MainSample, text = 'Move Sample', command = Open_MoveSample_Window, font = myFont).grid(row = 3, column=1, sticky = "ew")
    tk.Button(window_MainSample, text = 'Delete Sample', command = Open_DeleteSample_Window, font = myFont).grid(row = 5, column=1, sticky = "ew")
    tk.Button(window_MainSample, text = 'Add Sample Test', command = Open_SampleTest_Window, font = myFont).grid(row = 7, column=1, sticky = "ew")
    tk.Button(window_MainSample, text = 'Back to Edit Menu', command = Open_MainMenu_Window, font = myFont).grid(row = 9, column=1, sticky = "ew")

    tk.Label(window_MainSample, height = 1, width = 6, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_MainSample, height = 1, width = 6, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_MainSample, height = 1, width = 6, bg="cadet blue").grid(row =4, column =0)
    tk.Label(window_MainSample, height = 1, width = 6, bg="cadet blue").grid(row =6, column =0)
    tk.Label(window_MainSample, height = 1, width = 6, bg="cadet blue").grid(row =8, column =0)
    tk.Label(window_MainSample, height = 1, width = 6, bg="cadet blue").grid(row =10, column =3)

    window_MainSample.mainloop()
##########---------->END: MAIN WINDOW FOR SAMPLES<----------##########

