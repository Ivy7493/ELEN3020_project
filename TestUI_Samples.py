import SetupAPI
import sqlite3
import tkinter as tk
import DataAPI
import TestUI_MAIN

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
            _entryDate = entryDate.get()
            _sampleHistory = sampleHistory.get()
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

            print(DataAPI.SampleBox(conn, _sampleID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _sampleHistory, _subjectAge, _tubeRating, _collectionTitle, _donorPhone, _authorisedPhone, _returnType, _returnDate, _testResults, _phenotypeValue, _diseaseState))
        except:
            print("ERROR: Invalid data entered")
        
    def console_PrintSample():
        print("Sample ID: %s\Box ID: %s\nBox X: %s\nBox Y: %s\nBox Z: %s\nSample Type: %s\nCountry of Origin: %s\nCollection Date: %s\nEntry Date: %s\nSample History (REFERENCE): %s\nSubject Age: %s\nTube Rating: %s\nCollection Title: %s\nDonor Phone: %s\nAuthorised Phone: %s\nReturn or Destroy?: %s\nReturn or Destroy Date: %s\nTest Results: %s\nPhenotype Value: %s\nDisease State Value: %s" % 
                    (sampleID.get(), boxX.get(), boxY.get(), boxZ.get(), sampleType.get(), originCountry.get(), collectionDate.get(), entryDate.get(), sampleHistory.get(), subjectAge.get(), tubeRating.get(), collectionTitle.get(), donorPhone.get(), authorisedPhone.get(), returnType.get(), returnDate.get(), testResults.get(), phenotypeValue.get(), diseaseState.get()))


    def Open_MainSample_Window():
        window_AddSample.destroy()
        MainSample_Window()
      
    window_AddSample = tk.Tk()
    #window_AddSample.geometry("300x300")
    window_AddSample.title("ADD BOX")
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
    sampleType = tk.Entry(window_AddSample)
    sampleType.grid(row = 5, column = 1)

    tk.Label(window_AddSample, text = "Country of Origin").grid(row = 6)
    originCountry = tk.Entry(window_AddSample)
    originCountry.grid(row = 6, column = 1)

    tk.Label(window_AddSample, text = "Collection Date").grid(row = 7)
    collectionDate = tk.Entry(window_AddSample)
    collectionDate.grid(row = 7, column = 1)

    todaysDate = time.time()
    entryDate = str(datetime.datetime.fromtimestamp(todaysDate).strftime('%Y-%m-%d %H:%M%S'))

    sampleHistory

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

    tk.Label(window_AddSample, text = "Return or Destroy?").grid(row = 14)
    returnDate = tk.Entry(window_AddSample)
    returnDate.grid(row = 14, column = 1)


testResults TEXT NOT NULL,
phenotypeValue TEXT NOT NULL,
diseaseState TEXT NOT NULL

    tk.Button(window_AddBox, text = 'Print Box to Console', 
                        command = console_PrintBox).grid(row = 7, column=1)
    tk.Button(window_AddBox, text = 'Add Box', command = CreateBox).grid(row = 8, column=1)

    tk.Button(window_AddBox, text = 'Back to Box Menu', 
                        command = Open_MainBox_Window).grid(row = 10, column=1)

    window_AddBox.mainloop()
##########---------->END: WINDOW FOR ADDING BOXES<----------##########

##########---------->START: WINDOW FOR MOVING BOXES<----------##########
def MoveBox_Window():
    def MoveBox():
        try:
            _boxID = boxID.get()
            _fridgeID = fridgeID.get()
            print(DataAPI.MoveBox(conn, _boxID, _fridgeID))
        except:
            print("ERROR: Invalid data entered")

    def Open_MainBox_Window():
        window_MoveBox.destroy()
        MainBox_Window()

    window_MoveBox = tk.Tk()
    #window_MoveBox.geometry("300x300")
    window_MoveBox.title("MOVE BOX")
    window_MoveBox["bg"] = 'red'

    tk.Label(window_MoveBox, text = "Move box with BoxID:").grid(row = 0)
    boxID = tk.Entry(window_MoveBox)
    boxID.grid(row = 0, column = 1)

    tk.Label(window_MoveBox, text = "To fridge with FridgeID:").grid(row = 1)
    fridgeID = tk.Entry(window_MoveBox)
    fridgeID.grid(row = 1, column = 1)

    tk.Button(window_MoveBox, text = 'Move Box', command = MoveBox).grid(row = 5, column=1)
    tk.Button(window_MoveBox, text = 'Back to Box Menu', 
                        command = Open_MainBox_Window).grid(row = 10, column=1)

    window_MoveBox.mainloop()
##########---------->END: WINDOW FOR MOVING BOXES<----------##########

##########---------->START: WINDOW FOR DELETING BOXES<----------##########
def DeleteBox_Window():
    def DeleteBox():
        try:
            _boxID = boxID.get()
            _fridgeID = fridgeID.get()
            print("HAVEN'T MADE DELETE FUNCTION YET")
        except:
            print("ERROR: Invalid data entered")

    def Open_MainBox_Window():
        window_DeleteBox.destroy()
        MainBox_Window()

    window_DeleteBox = tk.Tk()
    #window_DeleteBox.geometry("300x300")
    window_DeleteBox.title("DELETE BOX")
    window_DeleteBox["bg"] = 'red'

    tk.Label(window_DeleteBox, text = "Delete box with BoxID: ").grid(row = 0)
    boxID = tk.Entry(window_DeleteBox)
    boxID.grid(row = 0, column = 1)

    tk.Label(window_DeleteBox, text = "From fridge with FridgeID: ").grid(row = 1)
    fridgeID = tk.Entry(window_DeleteBox)
    fridgeID.grid(row = 1, column = 1)

    tk.Button(window_DeleteBox, text = 'Delete Box', command = DeleteBox).grid(row = 5, column=1)
    tk.Button(window_DeleteBox, text = 'Back to Box Menu', 
                        command = Open_MainBox_Window).grid(row = 10, column=1)

    window_DeleteBox.mainloop()
##########---------->END: WINDOW FOR DELETING BOXES<----------##########

##########---------->START: MAIN WINDOW FOR BOXES<----------##########
def MainBox_Window():
    window_MainBox = tk.Tk()
    window_MainBox.geometry("300x300")
    window_MainBox.title("BOX MENU")
    window_MainBox["bg"] = 'red'

    def Open_AddBox_Window():
        window_MainBox.destroy()
        AddBox_Window()

    def Open_MoveBox_Window():
        window_MainBox.destroy()
        MoveBox_Window()

    def Open_DeleteBox_Window():
        window_MainBox.destroy()
        DeleteBox_Window()

    def Open_MainMenu_Window():
        window_MainBox.destroy()
        TestUI_MAIN.Main_Window()

    tk.Button(window_MainBox, text = 'Add Box', 
                        command = Open_AddBox_Window).grid(row = 0, column=0)
    tk.Button(window_MainBox, text = 'Move Box', 
                        command = Open_MoveBox_Window).grid(row = 1, column=0)
    tk.Button(window_MainBox, text = 'Delete Box', 
                        command = Open_DeleteBox_Window).grid(row = 2, column=0)
    tk.Button(window_MainBox, text = 'Back to Main Menu', 
                        command = Open_MainMenu_Window).grid(row = 3, column=0)

    window_MainBox.mainloop()
##########---------->END: MAIN WINDOW FOR BOXES<----------##########


#SetupAPI.CreateAllTables(conn)   
#MainBox_Window()

