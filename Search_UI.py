import tkinter as tk
from tkinter.font import Font
import SetupAPI
import sqlite3
import DataAPI
import Main_UI
import DisplayFridges
import DisplayBoxes
import DisplaySamples

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
    searchLabel1 = tk.Label(window_SearchFridge, text = 'Fridge ID:', anchor = "w", font=myFont, bg = 'cadet blue').grid(row=3, column = 1)
    searchField1 = tk.Entry(window_SearchFridge)
    searchField1.grid(row=3, column=2, sticky = "ew")

    def runDisplayFridges():
        DisplayFridges.OpenFridgeSearch(conn, searchField1.get())

    searchButton1 = tk.Button(window_SearchFridge, text='Search', command=runDisplayFridges, font=myFont)
    searchButton1.grid(row=3, column=3, sticky = "ew")
    #--------------------
    searchLabel2 = tk.Label(window_SearchFridge, text = 'Fridge Temperature:', anchor = "w", font=myFont, bg = 'cadet blue').grid(row=4, column = 1)
    searchField2 = tk.Entry(window_SearchFridge)
    searchField2.grid(row=4, column=2, sticky = "ew")

    def runDisplayTemperatures():
        DisplayFridges.OpenTemperatureSearch(conn, searchField2.get())

    searchButton2 = tk.Button(window_SearchFridge, text='Search', command=runDisplayTemperatures, font=myFont)
    searchButton2.grid(row=4, column=3, sticky = "ew")
    #--------------------
    searchLabel3 = tk.Label(window_SearchFridge, text = 'Number of Shelves:', font=myFont, bg = 'cadet blue', anchor = "w").grid(row=5, column = 1)
    searchField3 = tk.Entry(window_SearchFridge)
    searchField3.grid(row=5, column=2, sticky = "ew")

    def runDisplayShelves():
        DisplayFridges.OpenNumShelvesSearch(conn, searchField3.get())

    searchButton3 = tk.Button(window_SearchFridge, text='Search', command=runDisplayShelves, font=myFont)
    searchButton3.grid(row=5, column=3, sticky = "ew")
    #--------------------
    def Open_MainMenu_Window():
        window_SearchFridge.destroy()
        MainSearch_Window(conn)

    returnButton = tk.Button(window_SearchFridge, text='Back to Fridge Menu', command=Open_MainMenu_Window, font=myFont)
    returnButton.grid(row=7, column=2, sticky = "ew")
    #--------------------

    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =0, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =2, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =6, column =0)
    tk.Label(window_SearchFridge, height = 1, width = 2, bg="cadet blue").grid(row =8, column =4)

    window_SearchFridge.mainloop()
##########---------->END: WINDOW FOR SEARCHING FRIDGES<-------##########

##########---------->START: WINDOW FOR SEARCHING BOXES<------##########


def SearchBox_Window(conn):
    window_SearchBox = tk.Tk()
    window_SearchBox.title("SEARCH BOX WINDOW")
    #window_SearchBox.geometry("400x250")
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
    searchLabel1 = tk.Label(window_SearchBox, text = 'Box ID:', anchor = "w", font = myFont, bg = 'cadet blue').grid(row=3, column = 1)
    searchField1 = tk.Entry(window_SearchBox)
    searchField1.grid(row=3, column=2, sticky = "ew")
    
    def runDisplayBoxes():
        DisplayBoxes.OpenBoxIDSearch(conn, searchField1.get())

    searchButton1 = tk.Button(window_SearchBox, text='Search', command= runDisplayBoxes, font = myFont)
    searchButton1.grid(row=3, column=3, sticky = "ew")
    #--------------------
    searchLabel2 = tk.Label(window_SearchBox, text = 'Fridge ID:', anchor = "w", font = myFont, bg = 'cadet blue').grid(row = 4, column = 1)
    searchField2 = tk.Entry(window_SearchBox)
    searchField2.grid(row=4, column=2, sticky = "ew")

    def runDisplayFridgeID():
    	DisplayBoxes.OpenFridgeIDSearch(conn, searchField2.get())

    searchButton2 = tk.Button(window_SearchBox, text = 'Search', command=runDisplayFridgeID, font = myFont)
    searchButton2.grid(row=4, column=3, sticky = "ew")
    #--------------------
    def Open_MainMenu_Window():
        window_SearchBox.destroy()
        MainSearch_Window(conn)

    ReturnButton = tk.Button(window_SearchBox, text='Back to Box Menu', command=Open_MainMenu_Window, font = myFont).grid(row=6, column=2)
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
	window_SampleSearch.geometry("300x300")
	window_SampleSearch["bg"] = 'cadet blue'

	text = tk.Text(window_SampleSearch)
	myFont = Font(family='fixedsys', size=12)
	text.configure(font=myFont)

	def OpenAllSamples():
		DisplaySamples.OpenAllSamples(conn)

	DisplayButton = tk.Button(window_SampleSearch, text = 'Display All Samples', command=OpenAllSamples, font=myFont).grid(row=0, column=2, sticky = "ew")
	
	#--------------------
	def Open_MainMenu_Window():
		window_SampleSearch.destroy()
		MainSearch_Window(conn)

	ReturnButton = tk.Button(window_SampleSearch, text='Back to Box Menu', command=Open_MainMenu_Window, font = myFont).grid(row=6, column=2)
	#--------------------

	window_SampleSearch.mainloop()

##########---------->END: WINDOW FOR SEARCHING SAMPLES<-----##########

#########----------->START: MAIN WINDOW FOR SEARCH<----------###########


def MainSearch_Window(conn):
	window_MainSearch = tk.Tk()
	window_MainSearch.title("SEARCH MENU")
	window_MainSearch.geometry("300x250")
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

	def Open_MainMenu_Window():
		window_MainSearch.destroy()
		Main_UI.Main_Window(conn)



	tk.Button(window_MainSearch, text='Search Fridges', command = Open_SearchFridge_Window, font=myFont).grid(row=1, column=1, sticky = "ew")
	tk.Button(window_MainSearch, text='Search Boxes', command = Open_SearchBox_Window, font=myFont).grid(row=3, column=1, sticky = "ew")
	tk.Button(window_MainSearch, text='Search Samples', command = Open_SearchSample_Window, font=myFont).grid(row=5, column=1, sticky = "ew")
	tk.Button(window_MainSearch, text='Back to Main Menu', command = Open_MainMenu_Window, font=myFont).grid(row=7, column=1, sticky = "ew")
	
	tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =0, column =0)
	tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =2, column =0)
	tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =4, column =0)
	tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =6, column =0) 
	tk.Label(window_MainSearch, height = 1, width = 6, bg="cadet blue").grid(row =8, column =0) 

	window_MainSearch.mainloop()


