import sqlite3 #Importing sqlite3 library

#this is for testing purposes...This will go in front end
conn = ""
c = ""

#connection to DataBase function. This will be called from front end on program start
def ConnectDatabase():
    conn = sqlite3.connect('Test.db')
    c = conn.cursor()
    print("Successfully connected to Database!")

#command to add fridge to database 
def AddFridge(_conn, _FridgeID, _Mboxes, _Temparture):
    Temp = _conn.cursor()
    FridgeID = _FridgeID
    Cboxes = 0
    Mboxes = _Mboxes
    Temparture = _Temparture
    command = "INSERT INTO Fridges VALUES (" + "'" + FridgeID + "'" + ", " + str(Cboxes) + ", " +   str(Mboxes) + ", " + str(Temparture) + ")" 
    Temp.execute(command)
    _conn.commit()

#command for returning the number of fridges in database
def ReturnNumberOfFridges(_conn):
    Temp = _conn.cursor()
    Results = Temp.execute("SELECT * FROM Fridges")
    count = 0
    for Result in Results:
        count++
    return count

#basic function for creating the fridge table in the database
def CreateFridgeTable(_conn):
    Temp = _conn.cursor()
    Temp.execute("""CREATE TABLE Fridges(
                   FridgeID TEXT NOT NULL PRIMARY KEY,
                   Cboxes INTEGER,
                   Mboxes INTEGER,
                   Tempature INTEGER
                   )""")
    _conn.commit()

def GetFile(Filename);

