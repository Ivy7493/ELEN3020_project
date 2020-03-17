import sqlite3 #Importing sqlite3 library

#this is for testing purposes...This will go in front end


#connection to DataBase function. This will be called from front end on program start
def ConnectDatabase():
    conn = sqlite3.connect('Test.db')
    c = conn.cursor()
    print("Successfully connected to Database!")

def CreateFridgeTable():
    c.execute("""CREATE TABLE Fridges(
                   FridgeID TEXT NOT NULL PRIMARY KEY,
                   Cboxes INTEGER,
                   Mboxes INTEGER,
                   Tempature INTEGER
                   )""")
    conn.commit()

def TestFridge():
    FridgeID = "ABC"
    Cboxes = 0
    Mboxes = 9
    Temparture = -85
    command = "INSERT INTO Fridges VALUES (" + "'" + FridgeID + "'" + ", " + str(Cboxes) + ", " + str(Mboxes) + ", " + str(Temparture) + ")" 
    c.execute(command)
    conn.commit()

conn = sqlite3.connect('Test.db')
c = conn.cursor()
TestFridge()
c.execute("SELECT * FROM Fridges")
print(c.fetchall())
#ConnectDatabase()
#PRAGMA foreign_keys = ON
#CreateFridgeTable()
    

