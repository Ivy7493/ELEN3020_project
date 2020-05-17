import tkinter as tk
from tkinter.font import Font
import SetupAPI
import sqlite3
import DataAPI
import Main_UI
import DisplayFridges
import DisplayBoxes
import DisplaySamples
import DisplayCollections
import DisplayTestResults
from tkcalendar import *
from tkinter import ttk

##########---------->START: WINDOW FOR SEARCHING FRIDGES<-------##########
def SearchFridge_Window(conn):
    window_SearchFridge = tk.Tk()
    window_SearchFridge.title("SEARCH FRIDGE WINDOW")
    window_SearchFridge["bg"] = 'cadet blue'
    
    text = tk.Text(window_SearchFridge)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    #--------------------
    def OpenAllFridges():
        DisplayFridges.OpenAllFridges(conn)

    searchButton = tk.Button(window_SearchFridge, text='Display All Fridges', command=OpenAllFridges, font=myFont)
    searchButton.grid(row=1, column=2, sticky = "ew")
    #--------------------
    searchLabel1 = tk.Label(window_SearchFridge, text = 'Fridge ID:', anchor = "w", font=myFont, bg = 'cadet blue')
    searchLabel1.grid(row=3, column = 1, sticky = "ew")
    searchField1 = tk.Entry(window_SearchFridge)
    searchField1.grid(row=3, column=2, sticky = "ew")

    def runDisplayFridges():
        DisplayFridges.OpenFridgeSearch(conn, searchField1.get(), "fridgeID")

    searchButton1 = tk.Button(window_SearchFridge, text='Search', command=runDisplayFridges, font=myFont)
    searchButton1.grid(row=3, column=3, sticky = "ew")
    #--------------------
    searchLabel2 = tk.Label(window_SearchFridge, text = 'Fridge Temperature:', anchor = "w", font=myFont, bg = 'cadet blue')
    searchLabel2.grid(row=4, column = 1, sticky = "ew")
    searchField2 = tk.Entry(window_SearchFridge)
    searchField2.grid(row=4, column=2, sticky = "ew")

    def runDisplayTemperatures():
        DisplayFridges.OpenFridgeSearch(conn, searchField2.get(), "temperature")

    searchButton2 = tk.Button(window_SearchFridge, text='Search', command=runDisplayTemperatures, font=myFont)
    searchButton2.grid(row=4, column=3, sticky = "ew")
    #--------------------
    searchLabel3 = tk.Label(window_SearchFridge, text = 'Number of Shelves:', font=myFont, bg = 'cadet blue', anchor = "w")
    searchLabel3.grid(row=5, column = 1, sticky = "ew")
    searchField3 = tk.Entry(window_SearchFridge)
    searchField3.grid(row=5, column=2, sticky = "ew")

    def runDisplayShelves():
        DisplayFridges.OpenFridgeSearch(conn, searchField3.get(), "numShelves")

    searchButton3 = tk.Button(window_SearchFridge, text='Search', command=runDisplayShelves, font=myFont)
    searchButton3.grid(row=5, column=3, sticky = "ew")
    #--------------------
    #--------------------
    searchLabel4 = tk.Label(window_SearchFridge, text = 'Monthly Rate:', font=myFont, bg = 'cadet blue', anchor = "w")
    searchLabel4.grid(row=6, column = 1, sticky = "ew")
    searchField4 = tk.Entry(window_SearchFridge)
    searchField4.grid(row=6, column=2, sticky = "ew")

    def runDisplayRate():
        DisplayFridges.OpenFridgeSearch(conn, searchField4.get(), "rate")

    searchButton4 = tk.Button(window_SearchFridge, text='Search', command=runDisplayRate, font=myFont)
    searchButton4.grid(row=6, column=3, sticky = "ew")
    #--------------------
    def Open_MainMenu_Window():
        window_SearchFridge.destroy()
        MainSearch_Window(conn)

    returnButton = tk.Button(window_SearchFridge, text='Back to Search Menu', command=Open_MainMenu_Window, font=myFont)
    returnButton.grid(row=8, column=2, sticky = "ew")
    #--------------------

    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =7, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =9, column =4)

    window_SearchFridge.mainloop()
##########---------->END: WINDOW FOR SEARCHING FRIDGES<-------##########

##########---------->START: WINDOW FOR SEARCHING BOXES<------##########
def SearchBox_Window(conn):
    window_SearchBox = tk.Tk()
    window_SearchBox.title("SEARCH BOX WINDOW")
    window_SearchBox["bg"] = 'cadet blue'
    
    text = tk.Text(window_SearchBox)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    #--------------------
    def Open_AllBoxes():
        DisplayBoxes.OpenAllBoxes(conn)

    displayBoxesButton = tk.Button(window_SearchBox, text='Display All Boxes', command=Open_AllBoxes, font = myFont)
    displayBoxesButton.grid(row=1, column=2, sticky = "ew")
    #--------------------
    searchLabel1 = tk.Label(window_SearchBox, text = 'Box ID:', anchor = "w", font = myFont, bg = 'cadet blue')
    searchLabel1.grid(row=3, column = 1, sticky = "ew")
    searchField1 = tk.Entry(window_SearchBox)
    searchField1.grid(row=3, column=2, sticky = "ew")
    
    def runDisplayBoxes():
        DisplayBoxes.OpenBoxSearch(conn, searchField1.get(), "boxID")

    searchButton1 = tk.Button(window_SearchBox, text='Search', command= runDisplayBoxes, font = myFont)
    searchButton1.grid(row=3, column=3, sticky = "ew")
    #--------------------
    searchLabel2 = tk.Label(window_SearchBox, text = 'Fridge ID:', anchor = "w", font = myFont, bg = 'cadet blue')
    searchLabel2.grid(row = 4, column = 1, sticky = "ew")
    searchField2 = tk.Entry(window_SearchBox)
    searchField2.grid(row=4, column=2, sticky = "ew")

    def runDisplayFridgeID():
    	DisplayBoxes.OpenBoxSearch(conn, searchField2.get(), "fridgeID")

    searchButton2 = tk.Button(window_SearchBox, text = 'Search', command=runDisplayFridgeID, font = myFont)
    searchButton2.grid(row=4, column=3, sticky = "ew")
    #--------------------
    def Open_MainMenu_Window():
        window_SearchBox.destroy()
        MainSearch_Window(conn)

    ReturnButton = tk.Button(window_SearchBox, text='Back to Search Menu', command=Open_MainMenu_Window, font = myFont).grid(row=6, column=2)
    #--------------------

    tk.Label(window_SearchBox, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_SearchBox, height = 1, width = 2, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_SearchBox, height = 1, width = 2, bg="cadet blue").grid(row =5, column =0)
    tk.Label(window_SearchBox, height = 1, width = 2, bg="cadet blue").grid(row =7, column = 4)

    window_SearchBox.mainloop()

##########---------->END: WINDOW FOR SEARCHING BOXES<------##########

##########---------->START: WINDOW FOR SEARCHING SAMPLES<-----##########
def SearchSample_Window(conn):
    window_SampleSearch = tk.Tk()
    window_SampleSearch.title("SAMPLE SEARCH MENU")
    window_SampleSearch["bg"] = 'cadet blue'

    text = tk.Text(window_SampleSearch)
    myFont = Font(family='fixedsys', size=12)
    text.configure(font=myFont)

    def OpenAllSamples():
        DisplaySamples.OpenAllSamples(conn)

    DisplayButton = tk.Button(window_SampleSearch, text = 'Display All Samples', command=OpenAllSamples, font=myFont)
    DisplayButton.grid(row=1, column=2, sticky = "ew")

	#--------------------------------
    searchLabel1 = tk.Label(window_SampleSearch, text = 'Sample ID:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel1.grid(row=2, column =1, sticky = "ew")
    searchField1 = tk.Entry(window_SampleSearch)
    searchField1.grid(row = 2, column = 2, sticky = "ew")

    def runDisplaySamples():
        DisplaySamples.OpenSampleSearch(conn, searchField1.get(), "sampleID")

    searchButton1 = tk.Button(window_SampleSearch, text='Search', command = runDisplaySamples, font = myFont).grid(row=2, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel2 = tk.Label(window_SampleSearch, text = 'Box ID:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel2.grid(row=3, column =1, sticky = "ew")
    searchField2 = tk.Entry(window_SampleSearch)
    searchField2.grid(row = 3, column = 2, sticky = "ew")

    def runDisplayBoxID():
        DisplaySamples.OpenSampleSearch(conn, searchField2.get(), "boxID")

    searchButton2 = tk.Button(window_SampleSearch, text='Search', command = runDisplayBoxID, font = myFont).grid(row=3, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel3 = tk.Label(window_SampleSearch, text = 'Sample Type:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel3.grid(row=4, column =1, sticky = "ew")
    searchField3 = ttk.Combobox(window_SampleSearch, state="readonly", values=DataAPI.GetSampleTypes()) 
    searchField3.grid(row = 4, column = 2, sticky = "ew")

    def runDisplaySampleType():
        DisplaySamples.OpenSampleSearch(conn, searchField3.get(), "sampleType")

    searchButton3 = tk.Button(window_SampleSearch, text='Search', command = runDisplaySampleType, font = myFont).grid(row=4, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel4 = tk.Label(window_SampleSearch, text = 'Country of Origin:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel4.grid(row=5, column =1, sticky = "ew")
    searchField4 = tk.Entry(window_SampleSearch)
    searchField4.grid(row = 5, column = 2, sticky = "ew")

    def runOriginCountrySearch():
        DisplaySamples.OpenSampleSearch(conn, searchField4.get(), "originCountry")

    searchButton4 = tk.Button(window_SampleSearch, text='Search', command = runOriginCountrySearch, font = myFont).grid(row=5, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel5 = tk.Label(window_SampleSearch, text = 'Collection Date:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel5.grid(row=6, column =1, sticky = "ew")
    searchField5 = DateEntry(window_SampleSearch)
    searchField5.grid(row = 6, column = 2, sticky = "ew")

    def runCollectionDateSearch():
        DisplaySamples.OpenSampleSearch(conn, searchField5.get(), "collectionDate")

    searchButton5 = tk.Button(window_SampleSearch, text='Search', command = runCollectionDateSearch, font = myFont).grid(row=6, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel6 = tk.Label(window_SampleSearch, text = 'Entry Date:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel6.grid(row=7, column =1, sticky = "ew")
    searchField6 = DateEntry(window_SampleSearch)
    searchField6.grid(row = 7, column = 2, sticky = "ew")

    def runEntryDateSearch():
        DisplaySamples.OpenSampleSearch(conn, searchField6.get(), "entryDate")

    searchButton6 = tk.Button(window_SampleSearch, text='Search', command = runEntryDateSearch, font = myFont).grid(row=7, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel7 = tk.Label(window_SampleSearch, text = 'Subject Age:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel7.grid(row=8, column =1, sticky = "ew")
    searchField7 = tk.Entry(window_SampleSearch)
    searchField7.grid(row = 8, column = 2, sticky = "ew")

    def runDisplaySubjectAge():
        DisplaySamples.OpenSampleSearch(conn, searchField7.get(), "subjectAge")

    searchButton7 = tk.Button(window_SampleSearch, text='Search', command = runDisplaySubjectAge, font = myFont).grid(row=8, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel8 = tk.Label(window_SampleSearch, text = 'Tube Rating:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel8.grid(row=9, column =1, sticky = "ew")
    searchField8 = tk.Entry(window_SampleSearch)
    searchField8.grid(row = 9, column = 2, sticky = "ew")

    def runDisplayTubeRating():
        DisplaySamples.OpenSampleSearch(conn, searchField8.get(), "tubeRating")

    searchButton8 = tk.Button(window_SampleSearch, text='Search', command = runDisplayTubeRating, font = myFont).grid(row=9, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel9 = tk.Label(window_SampleSearch, text = 'Collection Title:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel9.grid(row=10, column =1, sticky = "ew")
    searchField9 = ttk.Combobox(window_SampleSearch, state="readonly", values = DataAPI.GetCollectionTitles(conn))
    searchField9.grid(row = 10, column = 2, sticky = "ew")

    def runDisplayCollectionTitle():
        DisplaySamples.OpenSampleSearch(conn, searchField9.get(), "collectionTitle")

    searchButton9 = tk.Button(window_SampleSearch, text='Search', command = runDisplayCollectionTitle, font = myFont).grid(row=10, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel10 = tk.Label(window_SampleSearch, text = 'Return Type:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel10.grid(row=11, column =1, sticky = "ew")
    searchField10 = ttk.Combobox(window_SampleSearch, state = "readonly", values = ["Return", "Destroy"])
    searchField10.grid(row = 11, column = 2, sticky = "ew")

    def runDisplayReturnType():
        DisplaySamples.OpenSampleSearch(conn, searchField10.get(), "returnType")

    searchButton10 = tk.Button(window_SampleSearch, text='Search', command = runDisplayReturnType, font = myFont).grid(row=11, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel11 = tk.Label(window_SampleSearch, text = 'Return Date:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel11.grid(row=12, column =1, sticky = "ew")
    searchField11 = DateEntry(window_SampleSearch)
    searchField11.grid(row = 12, column = 2, sticky = "ew")

    def runDisplayReturnDate():
        DisplaySamples.OpenSampleSearch(conn, searchField11.get(), "returnDate")

    searchButton11 = tk.Button(window_SampleSearch, text='Search', command = runDisplayReturnDate, font = myFont).grid(row=12, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel12 = tk.Label(window_SampleSearch, text = 'Phenotype Value:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel12.grid(row=13, column =1, sticky = "ew")
    searchField12 = tk.Entry(window_SampleSearch)
    searchField12.grid(row = 13, column = 2, sticky = "ew")

    def runDisplayPhenotypeValue():
        DisplaySamples.OpenSampleSearch(conn, searchField12.get(), "phenotypeValue")

    searchButton12 = tk.Button(window_SampleSearch, text='Search', command = runDisplayPhenotypeValue, font = myFont).grid(row=13, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    searchLabel13 = tk.Label(window_SampleSearch, text = 'Disease State:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel13.grid(row=14, column =1, sticky = "ew")
    searchField13 = tk.Entry(window_SampleSearch)
    searchField13.grid(row = 14, column = 2, sticky = "ew")

    def runDisplayDiseaseState():
        DisplaySamples.OpenSampleSearch(conn, searchField13.get(), "diseaseState")

    searchButton13 = tk.Button(window_SampleSearch, text='Search', command = runDisplayDiseaseState, font = myFont).grid(row=14, column=3, sticky = "ew")
	#-------------------------------
	
    #-------------------------------
    searchLabel14 = tk.Label(window_SampleSearch, text = 'Fridge ID:', anchor = "w", font=myFont, bg='cadet blue')
    searchLabel14.grid(row=15, column =1, sticky = "ew")
    searchField14 = tk.Entry(window_SampleSearch)
    searchField14.grid(row = 15, column = 2, sticky = "ew")

    def runDisplayFridgeID():
        fridgeID = searchField14.get()
        DisplaySamples.OpenSampleFridgeSearch(conn, fridgeID)

    searchButton14 = tk.Button(window_SampleSearch, text='Search', command = runDisplayFridgeID, font = myFont).grid(row=15, column=3, sticky = "ew")
	#-------------------------------

	#-------------------------------
    def Open_MainMenu_Window():
        window_SampleSearch.destroy()
        MainSearch_Window(conn)
    
    ReturnButton = tk.Button(window_SampleSearch, text='Back to Search Menu', command=Open_MainMenu_Window, font = myFont).grid(row=17, column=2)
	#-------------------------------

    tk.Label(window_SampleSearch, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_SampleSearch, height = 1, width = 2, bg="cadet blue").grid(row =16, column =0)
    tk.Label(window_SampleSearch, height = 1, width = 2, bg="cadet blue").grid(row =18, column =4)

    window_SampleSearch.mainloop()

##########---------->END: WINDOW FOR SEARCHING SAMPLES<----------##########

##########---------->START: WINDOW FOR SEARCHING COLLECTIONS<-----##########
def SearchCollections_Window(conn):
    window_SearchCollections = tk.Tk()
    window_SearchCollections.title("SEARCH COLLECTION WINDOW")
    window_SearchCollections["bg"] = 'cadet blue'
    
    text = tk.Text(window_SearchCollections)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    #--------------------
    def OpenAllCollections():
        DisplayCollections.OpenAllCollections(conn)

    searchButton = tk.Button(window_SearchCollections, text='Display All Collections', command=OpenAllCollections, font=myFont)
    searchButton.grid(row=1, column=2, sticky = "ew")
    #--------------------
    searchLabel1 = tk.Label(window_SearchCollections, text = 'Collection Title:', anchor = "w", font=myFont, bg = 'cadet blue')
    searchLabel1.grid(row=3, column = 1, sticky = "ew")
    searchField1 = tk.Entry(window_SearchCollections)
    searchField1.grid(row=3, column=2, sticky = "ew")

    def runDisplayCollections():
        DisplayCollections.OpenCollectionSearch(conn, searchField1.get(), "collectionTitle")

    searchButton1 = tk.Button(window_SearchCollections, text='Search', command=runDisplayCollections, font=myFont)
    searchButton1.grid(row=3, column=3, sticky = "ew")
    #--------------------
    searchLabel2 = tk.Label(window_SearchCollections, text = 'Donor ID:', anchor = "w", font=myFont, bg = 'cadet blue')
    searchLabel2.grid(row=4, column = 1, sticky = "ew")
    searchField2 = tk.Entry(window_SearchCollections)
    searchField2.grid(row=4, column=2, sticky = "ew")

    def runDisplayDonorID():
        DisplayCollections.OpenCollectionSearch(conn, searchField2.get(), "donorID")

    searchButton2 = tk.Button(window_SearchCollections, text='Search', command=runDisplayDonorID, font=myFont)
    searchButton2.grid(row=4, column=3, sticky = "ew")
    #--------------------
    searchLabel3 = tk.Label(window_SearchCollections, text = 'Client Name:', font=myFont, bg = 'cadet blue', anchor = "w")
    searchLabel3.grid(row=5, column = 1, sticky = "ew")
    searchField3 = tk.Entry(window_SearchCollections)
    searchField3.grid(row=5, column=2, sticky = "ew")

    def runDisplayClientName():
        DisplayCollections.OpenCollectionSearch(conn, searchField3.get(), "clientName")

    searchButton3 = tk.Button(window_SearchCollections, text='Search', command=runDisplayClientName, font=myFont)
    searchButton3.grid(row=5, column=3, sticky = "ew")
    #--------------------
    #--------------------
    searchLabel4 = tk.Label(window_SearchCollections, text = 'Client Organization:', font=myFont, bg = 'cadet blue', anchor = "w")
    searchLabel4.grid(row=6, column = 1, sticky = "ew")
    searchField4 = tk.Entry(window_SearchCollections)
    searchField4.grid(row=6, column=2, sticky = "ew")

    def runDisplayClientOrganization():
        DisplayCollections.OpenCollectionSearch(conn, searchField4.get(), "clientOrganization")

    searchButton4 = tk.Button(window_SearchCollections, text='Search', command=runDisplayClientOrganization, font=myFont)
    searchButton4.grid(row=6, column=3, sticky = "ew")
    #--------------------
    def Open_MainMenu_Window():
        window_SearchCollections.destroy()
        MainSearch_Window(conn)

    returnButton = tk.Button(window_SearchCollections, text='Back to Search Menu', command=Open_MainMenu_Window, font=myFont)
    returnButton.grid(row=8, column=2, sticky = "ew")
    #--------------------

    tk.Label(window_SearchCollections, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_SearchCollections, height = 1, width = 2, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_SearchCollections, height = 1, width = 2, bg="cadet blue").grid(row =7, column =0)
    tk.Label(window_SearchCollections, height = 1, width = 2, bg="cadet blue").grid(row =9, column =4)

    window_SearchCollections.mainloop()
##########---------->END: WINDOW FOR SEARCHING COLLECTIONS<-------##########


##########---------->START: WINDOW FOR SEARCHING TEST RESULTS<-----##########
def SearchTestResults_Window(conn):
    window_SearchTestResults = tk.Tk()
    window_SearchTestResults.title("SEARCH TEST RESULTS WINDOW")
    window_SearchTestResults["bg"] = 'cadet blue'
    
    text = tk.Text(window_SearchTestResults)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    #--------------------
    def OpenAllTestResults():
        DisplayTestResults.OpenAllTestResults(conn)

    searchButton = tk.Button(window_SearchTestResults, text='Display All Test Results', command=OpenAllTestResults, font=myFont)
    searchButton.grid(row=1, column=2, sticky = "ew")
    #--------------------
    searchLabel1 = tk.Label(window_SearchTestResults, text = 'Test Type:', anchor = "w", font=myFont, bg = 'cadet blue')
    searchLabel1.grid(row=3, column = 1, sticky = "ew")
    searchField1 = tk.Entry(window_SearchTestResults)
    searchField1.grid(row=3, column=2, sticky = "ew")

    def runDisplayTestType():
        DisplayTestResults.OpenTestResultSearch(conn, searchField1.get(), "testType")

    searchButton1 = tk.Button(window_SearchTestResults, text='Search', command=runDisplayTestType, font=myFont)
    searchButton1.grid(row=3, column=3, sticky = "ew")
    #--------------------
    searchLabel2 = tk.Label(window_SearchTestResults, text = 'Sample ID:', anchor = "w", font=myFont, bg = 'cadet blue')
    searchLabel2.grid(row=4, column = 1, sticky = "ew")
    searchField2 = tk.Entry(window_SearchTestResults)
    searchField2.grid(row=4, column=2, sticky = "ew")

    def runDisplaySampleID():
        DisplayTestResults.OpenTestResultSearch(conn, searchField2.get(), "sampleID")

    searchButton2 = tk.Button(window_SearchTestResults, text='Search', command=runDisplaySampleID, font=myFont)
    searchButton2.grid(row=4, column=3, sticky = "ew")
    #--------------------
    def Open_MainMenu_Window():
        window_SearchTestResults.destroy()
        MainSearch_Window(conn)

    returnButton = tk.Button(window_SearchTestResults, text='Back to Search Menu', command=Open_MainMenu_Window, font=myFont)
    returnButton.grid(row=8, column=2, sticky = "ew")
    #--------------------

    tk.Label(window_SearchTestResults, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_SearchTestResults, height = 1, width = 2, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_SearchTestResults, height = 1, width = 2, bg="cadet blue").grid(row =7, column =0)
    tk.Label(window_SearchTestResults, height = 1, width = 2, bg="cadet blue").grid(row =9, column =4)

    window_SearchTestResults.mainloop()
##########---------->END: WINDOW FOR SEARCHING TEST RESULTS<-------##########


#########----------->START: MAIN WINDOW FOR SEARCH<----------###########
def MainSearch_Window(conn):
    window_MainSearch = tk.Tk()
    window_MainSearch.title("SEARCH MENU")
    window_MainSearch["bg"] = 'cadet blue'

    text = tk.Text(window_MainSearch)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def Open_SearchFridge_Window():
        window_MainSearch.destroy()
        SearchFridge_Window(conn)

    def Open_SearchBox_Window():
        window_MainSearch.destroy()
        SearchBox_Window(conn)

    def Open_SearchSample_Window():
        window_MainSearch.destroy()
        SearchSample_Window(conn)

    def Open_SearchCollections_Window():
        window_MainSearch.destroy()
        SearchCollections_Window(conn)

    def Open_SearchTestResults_Window():
        window_MainSearch.destroy()
        SearchTestResults_Window(conn)

    def Open_MainMenu_Window():
        window_MainSearch.destroy()
        Main_UI.Main_Window(conn)

    tk.Button(window_MainSearch, text='Search Fridges', command = Open_SearchFridge_Window, font=myFont).grid(row=1, column=1, sticky = "ew")
    tk.Button(window_MainSearch, text='Search Boxes', command = Open_SearchBox_Window, font=myFont).grid(row=3, column=1, sticky = "ew")
    tk.Button(window_MainSearch, text='Search Samples', command = Open_SearchSample_Window, font=myFont).grid(row=5, column=1, sticky = "ew")
    tk.Button(window_MainSearch, text='Search Collections', command = Open_SearchCollections_Window, font=myFont).grid(row=7, column=1, sticky = "ew")
    tk.Button(window_MainSearch, text='Search Test Results', command = Open_SearchTestResults_Window, font=myFont).grid(row=9, column=1, sticky = "ew")
    tk.Button(window_MainSearch, text='Back to Main Menu', command = Open_MainMenu_Window, font=myFont).grid(row=11, column=1, sticky = "ew")

    tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =4, column =0)
    tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =6, column =0) 
    tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =8, column =0) 
    tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =10, column =0) 
    tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =12, column =2) 

    window_MainSearch.mainloop()


