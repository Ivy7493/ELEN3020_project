import sqlite3
import tkinter as tk
from tkinter import ttk

def OpenAllSamples(conn):
	c = conn.cursor()

	window_Samples = tk.Tk()
	window_Samples.title("SAMPLES")

	cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
	tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
	for col in cols:
		tree.hading(col, text = col)
	tree.grid(row=2, column = 0, columnspan=7)

	c.execute("SELECT * FROM SampleTable")

	for row in c.fetchall():
		tree.insert("", "end", values = (row))

	def openSampleSearchMenu():
		window_Samples.destroy()

	backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

	window_Samples.mainloop()



def OpenSampleSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Sample ID")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE sampleID=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenBoxIDSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Box ID")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE boxID=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 

def OpenSampleTypeSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Sample Type")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE sampleType=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenOriginCountrySearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Country of Origin")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE originCountry=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 

def OpenCollectionDateSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Collection Date")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE collectionDate=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 

def OpenEntryDateSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "Either no samples were added on this date or the date entered is incorrect")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE entryDate=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenSubjectAgeSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Subject Age")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE subjectAge=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenTubeRatingSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Tube Rating")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE tubeRating=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenCollectionTitleSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Collection Title")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE collectionTitle=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenReturnTypeSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Return Type")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE returnType=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenReturnDateSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Return Date")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE returnDate=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenPhenoTypeValueSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Phenotype Value")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE phenotypeValue=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 



def OpenDiseaseStateSearch(conn, searchField):
	c = conn.cursor()

	if searchField == "":
		message_Window = tk.TK()
		message_Window.title("ERROR")
		message = tk.Label(message_Window, text = "That is not a valid Disease State")
		message.grid(row=0, column=0)

		def openSampleSearchMenu():
			message_Window.destroy()

		backButton = tk.Button(message_Window, text = 'Close', command = openSampleSearchMenu).grid(row=1)

	else:
		window_Samples = tk.Tk()
		window_Samples.title("SAMPLES")

		cols = ('Sample ID', 'Box ID', 'Box X', 'Box Y', 'Box Z', 'Sample Type', 'Country of Origin', 'Collection Date', 'Entry Date', 'Subject Age', 'Tube Rating', 'Collection Title', 'Return Type', 'Return Date', 'Phenotype Value', 'Disease State')
		tree = ttk.Treeview(window_Samples, columns=cols, show='headings')
		for col in cols:
			tree.hading(col, text = col)
		tree.grid(row=2, column = 0, columnspan=7)

		c.execute("SELECT * FROM SampleTable WHERE diseaseState=?", (str(searchField),))

		for row in c.fetchall():
			tree.insert("", "end", values = (row))

		def openSampleSearchMenu():
			window_Samples.destroy()

		backButton = tk.Button(window_Samples, text = 'close', command=openSampleSearchMenu).grid(row=5, column=1)

		window_Samples.mainloop() 