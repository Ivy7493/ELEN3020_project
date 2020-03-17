import sqlite3

def AddFridge(_conn, _fridgeID, _temperature, _numShelves, _widthShelves):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO FridgeTable (fridgeID, temperature, numShelves, widthShelves) VALUES (?, ?, ?, ?)",(_fridgeID,int(_temperature), int(_numShelves), int(_widthShelves)))
        _conn.commit()
        return("Successfully added Fridge " + _fridgeID)

    except sqlite3.Error as error:
        return(error)

def IsFridgeFull(_conn, _fridgeID):
    c = _conn.cursor()
    c.execute("SELECT * FROM BoxTable WHERE fridgeID=?", (_fridgeID,))
    boxResults = c.fetchall()
    count = 0
    for result in boxResults:
        count = count + 1 
    c.execute("SELECT * FROM FridgeTable WHERE fridgeID=?", (_fridgeID,))
    results = c.fetchone()
    _numShelves = results[2]
    _widthShelves = results[3]
    maxNumber = _numShelves * _widthShelves
    if count >= maxNumber:
        return "TRUE"
    elif count < maxNumber:
        return "FALSE"

def DoesIDExist(_conn, _type, _ID):
    if _type == "BOX":
        c = _conn.cursor()
        c.execute("SELECT * FROM BoxTable WHERE boxID=?", (_ID,))
        results = c.fetchall()
        count = 0
        for result in results:
            count = count + 1
        if count == 0:
            return "FALSE"
        elif count > 0:        
            return "TRUE" 
    elif _type == "FRIDGE":
        c = _conn.cursor()
        c.execute("SELECT * FROM FridgeTable WHERE fridgeID=?", (_ID,))
        results = c.fetchall()
        count = 0
        for result in results:
            count = count + 1
        if count == 0:
            return "FALSE"
        elif count > 0:        
            return "TRUE"    
    elif _type == "SAMPLE":
        print("NEED TO DO SAMPLE")
 

def MoveBox(_conn, _boxID, _fridgeID):
    if DoesIDExist(_conn, "FRIDGE", _fridgeID) == "TRUE" and DoesIDExist(_conn, "BOX", _boxID) == "TRUE":
        if IsFridgeFull(_conn, _fridgeID) == "TRUE":
            return ("Fridge: " + _fridgeID + " is full, please select another box!")
        elif IsFridgeFull(_conn, _fridgeID) == "FALSE":
            c = _conn.cursor()
            c.execute("UPDATE BoxTable SET fridgeID =? WHERE boxID =?",(_fridgeID,_boxID,))
            _conn.commit()
            return ("Box: " + _boxID + " was moved to fridge: " + _fridgeID)
    elif DoesIDExist(_conn, "FRIDGE", _fridgeID) == "FALSE":
        #print("Not a Valid FridgeID")
        return "Not a Valid FridgeID"
    elif DoesIDExist(_conn, "BOX", _boxID) == "FALSE":
        #print("Not a Valid BoxID")
        return "Not a Valid BoxID"
        
 


def AddBox(_conn, _boxID, _fridgeID, _boxX, _boxY, _boxZ):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO BoxTable (boxID, fridgeID, boxX, boxY, boxZ) VALUES (?, ?, ?, ?, ?)",(_boxID, _fridgeID,int(_boxX), int(_boxY), int(_boxZ)))
        _conn.commit()
        return("Successfully added Box " + _boxID)

    except sqlite3.Error as error:
        return(error)

