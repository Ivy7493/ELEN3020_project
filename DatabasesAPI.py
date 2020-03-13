import sqlite3 #Importing sqlite3 library
import LoggingAPI

#this is for testing purposes...This will go in front end
conn = ""
c = ""

#connection to DataBase function. This will be called from front end on program start
def ConnectDatabase():
    conn = sqlite3.connect('Test.db')
    c = conn.cursor()
    print("Successfully connected to Database!")
    return conn

#command to add fridge to database 
def AddFridge(_conn, _FridgeID, _Mboxes, _Temparture):
    Temp = _conn.cursor()
    FridgeID = _FridgeID
    Mboxes = _Mboxes
    Temparture = _Temparture
    command = "INSERT INTO Fridges VALUES (" + "'" + FridgeID + "'"  + ", " +   str(Mboxes) + ", " + str(Temparture) + ")" 
    Temp.execute(command)
    _conn.commit()


#confirmed working, checking to see if FridgeID given is unique
def CheckFridgeID(_conn, _FridgeID):
    Temp = _conn.cursor()
    Temp.execute("SELECT * FROM Fridges WHERE FridgeID=?", (_FridgeID,))
    Entries = Temp.fetchall()
    count = 0
    for Entry in Entries:
        count = count + 1
    if count == 0:
        return "True" #true means it doesnt exist
    return "False" #false means it exists already

#command for returning the number of fridges in database
def ReturnNumberOfFridges(_conn):
    Temp = _conn.cursor()
    Results = Temp.execute("SELECT * FROM Fridges")
    count = 0
    for Result in Results:
        count = count + 1
    return count

#basic function for creating the fridge table in the database
def CreateFridgeTable(_conn):
    Temp = _conn.cursor()
    Temp.execute("""CREATE TABLE Fridges(
                   FridgeID TEXT NOT NULL PRIMARY KEY,
                   Mboxes INTEGER,
                   Tempature INTEGER
                   )""")
    _conn.commit()

#prints all the fridge entrys to console
def PrintFridgeTable(_conn):
    Temp = _conn.cursor()
    x = Temp.execute("SELECT * FROM Fridges")
    for y in x:
        print(y)

def CreateBoxTable(_conn):
    Temp = _conn.cursor()
    Temp.execute("""CREATE TABLE Boxes(
                        BoxID TEXT NOT NULL PRIMARY KEY,
                        FridgeID TEXT NOT NULL,
                        Msamples INTEGER,
                        FOREIGN KEY (FridgeID) REFERENCES Fridges (FridgeID)
                        )""")
    _conn.commit()

def PrintBoxTable(_conn):
    Temp = _conn.cursor()
    x = Temp.execute("SELECT * FROM Boxes")
    for y in x:
        print(y)

#Function to add box to database
def AddBox(_conn,_BoxID, _FridgeID, _Msamples):
    Temp = _conn.cursor()
    if CheckFridgeID(_conn, _FridgeID) == "False" and IsFridgeFull(_conn, _FridgeID) == "False":
        command = "INSERT INTO Boxes VALUES (" + "'" + _BoxID + "'"  + ", " + "'" + _FridgeID + "'" + ", " +   str(_Msamples) + ")" 
        Temp.execute(command)
        LoggingAPI.Log("Box: " + _BoxID + " created = [" + _BoxID + "," + _FridgeID + "," + _Msamples + "]") #logging line
        _conn.commit()
    elif CheckFridgeID(_conn, _FridgeID) == "True":
        print("Not a valid entry, FridgeID does not exist")
    elif IsFridgeFull(_conn, _FridgeID) == "True":
        print("Not a Valid entry, Fridge is full and cannot take another box")

#check to see if fridge can hold another box
def IsFridgeFull(_conn, _FridgeID):
    Max = ReturnFridgeSize(_conn, _FridgeID)
    count = ReturnFridgeBoxCount(_conn, _FridgeID)
    print("count = " + str(count))
    print("Max = " + str(Max))
    if count < Max:
        print("Fridge Has space")
        return "False"
    elif count >= Max:
        print("Fridge Has No space")
        return "True"

#Returns the max capicty of fridge
def ReturnFridgeSize(_conn, _FridgeID):
    Temp = _conn.cursor()
    Temp.execute("SELECT Mboxes FROM Fridges WHERE FridgeID = " + "'" + _FridgeID + "'")
    Max = Temp.fetchall()
    Max = Max[0][0]
    return Max

#Returns the number of Boxes in a fridge
def ReturnFridgeBoxCount(_conn, _FridgeID):
    Temp = _conn.cursor()
    Temp.execute("SELECT * FROM Boxes WHERE FridgeID = " + "'" + _FridgeID + "'")
    Current = Temp.fetchall()
    print(Current)    
    count = 0    
    for x in Current:
        count = count + 1
    return count

def MoveBox(_conn, _BoxID, _FridgeID):
    Temp = _conn.cursor()
    if CheckBoxID(_conn, _BoxID) == "False" and CheckFridgeID(_conn, _FridgeID) == "False":
        if ReturnFridgeBoxCount(_conn, _FridgeID) < ReturnFridgeSize(_conn, _FridgeID):
            Temp.execute("UPDATE Boxes SET FridgeID = " + "'" + _FridgeID + "'" + " WHERE BoxID = " + "'" + _BoxID + "'")
            _conn.commit()
            print("Moved Box : " + _BoxID + " To fridge : " + _FridgeID)
            LoggingAPI.Log("Box: " + _BoxID + " moved to fridge: " + _FridgeID)
        elif ReturnFridgeBoxCount(_conn, _FridgeID) >= ReturnFridgeSize(_conn, _FridgeID):
            print("Fridge is full cannot move box")
    elif CheckBoxID(_conn, _BoxID) == "True":
        print("Not a Valid Box Code")
    elif CheckFridgeID(_conn, _FridgeID) == "True":
        print("Not a Valid Fridge Code")


def CheckBoxID(_conn, _BoxID):
    Temp = _conn.cursor()
    Temp.execute("SELECT * FROM Boxes WHERE BoxID=?", (_BoxID,))
    Entries = Temp.fetchall()
    count = 0
    for Entry in Entries:
        count = count + 1
    if count == 0:
        return "True" #true means it doesnt exist
    return "False" #false means it exists already
         
    
    


