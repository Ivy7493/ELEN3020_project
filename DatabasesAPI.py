import sqlite3 #Importing sqlite3 library


#connection to DataBase function. This will be called from front end on program start
def ConnectDatabase():
    conn = sqlite3.connect('Test.db')
    c = conn.cursor()
    print("Successfully connected to Database!")

#this is for testing purposes...This will go in front end
conn = ""
c = ""
ConnectDatabase()

