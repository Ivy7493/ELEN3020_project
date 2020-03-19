import sqlite3
import LoggingAPI

def AddFridge(_conn, _fridgeID, _temperature, _numShelves, _widthShelves):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO FridgeTable (fridgeID, temperature, numShelves, widthShelves) VALUES (?, ?, ?, ?)",(_fridgeID,int(_temperature), int(_numShelves), int(_widthShelves)))
        _conn.commit()
        LoggingAPI.Log("Added new fridge: " + _fridgeID) #logging
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
        c = _conn.cursor()
        c.execute("SELECT * FROM SampleTable WHERE sampleID=?", (_ID,))
        results = c.fetchall()
        count = 0
        for result in results:
            count = count + 1
        if count == 0:
            return "FALSE"
        elif count > 0:
            return "TRUE"


def ReturnFridgeTemp(_conn, _fridgeID):
    c = _conn.cursor()
    c.execute("SELECT temperature FROM FridgeTable WHERE fridgeID=?",(_fridgeID,))
    result = c.fetchone()
    return result[0]

def BoxLog(_conn, _boxID, _fridgeID):
    
    c = _conn.cursor()
    temp = ReturnFridgeTemp(_conn,_fridgeID)
    c.execute("SELECT * FROM SampleTable WHERE boxID=?",(_boxID,))
    results = c.fetchall()
    count = 0
    for result in results:
        currentSample = result[0]
        count = count + 1
        LoggingAPI.IndividualLog("Sample: " + currentSample + " was move to fridge: " + _fridgeID + " at temperature: " + temp ,currentSample)

 

def MoveBox(_conn, _boxID, _fridgeID):
    if DoesIDExist(_conn, "FRIDGE", _fridgeID) == "TRUE" and DoesIDExist(_conn, "BOX", _boxID) == "TRUE":
        if IsFridgeFull(_conn, _fridgeID) == "TRUE":
            return ("Fridge: " + _fridgeID + " is full, please select another box!")
        elif IsFridgeFull(_conn, _fridgeID) == "FALSE":
            c = _conn.cursor()
            c.execute("UPDATE BoxTable SET fridgeID =? WHERE boxID =?",(_fridgeID,_boxID,))
            _conn.commit()
            LoggingAPI.Log("Box: " + _boxID + " was moved to fridge: " + _fridgeID)#logging
            BoxLog(_conn, _boxID, _fridgeID)
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
        LoggingAPI.Log("Added new box: " + _boxID)#logging
        return("Successfully added Box " + _boxID)

    except sqlite3.Error as error:
        return(error)

def AddSample(_conn, _sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _sampleHistory, _subjectAge, _tubeRating, _collectionTitle, _donorPhone, _authorisedPhone, _returnType, _returnDate, _testResults, _phenotypeValue, _diseaseState):
    try:
        c = _conn.cursor()
        if IsPositionFree(_conn, _boxID, _boxX, _boxY, _boxZ) == "TRUE":
            c.execute("INSERT INTO SampleTable(sampleID , boxID, boxX, boxY, boxZ, sampleType, originCountry, collectionDate, entryDate, sampleHistory, subjectAge, tubeRating, collectionTitle, donorPhone, authorisedPhone, returnType, returnDate, testResults, phenotypeValue, diseaseState) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(_sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _sampleHistory, _subjectAge, _tubeRating, _collectionTitle, _donorPhone, _authorisedPhone, _returnType, _returnDate, _testResults, _phenotypeValue, _diseaseState))
            _conn.commit()
            LoggingAPI.Log("Added new sample: " + _sampleID)#logging
            _FridgeID = ReturnFridgeSampleIn(_conn,_sampleID)
            #print(_FridgeID)
            #fridgeTemp = ReturnFridgeTemp(_conn,_FridgeID) 
            #print(fridgeTemp)
            LoggingAPI.IndividualLog("Added new sample:" + _sampleID,_sampleID)
            return ("Successfully added sample " + _sampleID)             
        else:
            return (IsPositionFree(_conn, _boxID, _boxX, _boxY, _boxZ) + " in box: " + _boxID)
           
    except sqlite3.Error as error:
        return error

def ReturnFridgeSampleIn(_conn, _sampleID):
    c = _conn.cursor()
    c.execute("SELECT boxID FROM SampleTable WHERE sampleID=?",(_sampleID,))
    A = c.fetchone()
    result = A[0]
    c.execute("SELECT fridgeID FROM BoxTable WHERE boxID=?",(result,))
    b = c.fetchone()
    resultB = b[0]
    return resultB         

def IsPositionFree(_conn, _boxID, _posX, _posY, _posZ):
    c = _conn.cursor()
    c.execute("SELECT * FROM BoxTable WHERE boxID=?",(_boxID,))
    results = c.fetchone()
    boxX = results[2]
    boxY = results[3]
    boxZ = results[4]
    if _posX <= boxX and _posY <= boxY and _posZ <= boxZ and _posX >= 1 and _posY >= 1 and _posZ >= 1:
        ##################################
        c.execute("SELECT * FROM SampleTable WHERE boxID=? AND boxX=? AND boxY=? AND boxZ=?",(_boxID,_posX, _posY, _posZ,))
        LocResults = c.fetchall()
        count = 0;
        for result in LocResults:
            count = count + 1
        if count > 0:
            return "Position Already taken"
        elif count == 0:
            return "TRUE" 
    elif _posX > boxX or _posX < 1:
        return "Invalid X location"
    elif _posY > boxY or _posY < 1:
        return "Invalid Y Location"
    elif _posZ > boxZ or _posZ < 1:
        return "Invalid Z Location"

def MoveSample(_conn, _sampleID, _boxID, _posX , _posY, _posZ):
    c = _conn.cursor()
    if DoesIDExist(_conn, "SAMPLE", _sampleID) == "TRUE" and DoesIDExist(_conn, "BOX", _boxID) == "TRUE" and IsPositionFree(_conn, _boxID, _posX, _posY, _posZ) == "TRUE":
        c.execute("UPDATE SampleTable SET boxID=?, boxX=?, boxY=?, boxZ=? WHERE sampleID=?", (_boxID,_posX,_posY,_posZ,_sampleID,))
        _conn.commit()
        LoggingAPI.Log("Sample: " + _sampleID + " was move into box: " + _boxID) #logging
        LoggingAPI.IndividualLog("Sample: " + _sampleID + " was move into box: " + _boxID, _sampleID)
        return "Successfully moved sample: " + _sampleID + " into box: " + _boxID
    elif DoesIDExist(_conn, "SAMPLE", _sampleID) == "FALSE":
        return "Sample ID: " + _sampleID + " does not exist!"
    elif DoesIDExist(_conn, "BOX", _boxID) == "FALSE":
        return "Box ID: " + _boxID + " does not exist!"
    elif IsPositionFree(_conn, _boxID, _posX, _posY, _posZ) != "TRUE":
        return IsPositionFree(_conn, _boxID, _posX, _posY, _posZ)

def IsBoxEmpty(_conn , _boxID):
    c = _conn.cursor()
    if DoesIDExist(_conn, "BOX", _boxID) == "TRUE":
        c.execute("SELECT * FROM SampleTable WHERE boxID=?", (_boxID,))
        results = c.fetchall()
        count = 0
        for result in results:
            count = count + 1
        if count == 0:
            return "TRUE"
        elif count >= 1:
            return "FALSE"
    elif DoesIDExist(_conn, "BOX", _boxID) == "FALSE":
        return "FALSE" 

def DeleteBox(_conn , _boxID):
    if IsBoxEmpty(_conn, _boxID) == "TRUE":
        c = _conn.cursor()
        c.execute("DELETE FROM BoxTable WHERE boxID=?",(_boxID,))
        _conn.commit()
        LoggingAPI.Log("Box: " + _boxID +  " deleted!")#logging
        return "Box: " + _boxID +  " succesfully deleted!"
    elif IsBoxEmpty(_conn, _boxID) == "FALSE":
        return "Box doesn't exist or is not empty! Cannot be deleted"

def IsFridgeEmpty(_conn, _fridgeID):
    c = _conn.cursor()
    if DoesIDExist(_conn, "FRIDGE", _fridgeID) == "TRUE":
        c.execute("SELECT * FROM BoxTable WHERE fridgeID=?", (_fridgeID,))
        results = c.fetchall()
        count = 0
        for result in results:
            count = count + 1
        if count == 0:
            return "TRUE"
        elif count >= 1:
            return "FALSE"
    elif DoesIDExist(_conn, "FRIDGE", _fridgeID) == "FALSE":
        return "FALSE" 

def DeleteFridge(_conn, _fridgeID):
    if IsFridgeEmpty(_conn, _fridgeID) == "TRUE":
        c = _conn.cursor()
        c.execute("DELETE FROM FridgeTable WHERE fridgeID=?",(_fridgeID,))
        _conn.commit()
        LoggingAPI.Log("Fridge: " + _fridgeID +  " deleted!")#logging
        return "Fridge: " + _fridgeID +  " succesfully deleted!"
    elif IsFridgeEmpty(_conn, _fridgeID) == "FALSE":
        return "Fridge doesn't exist or is not empty! Cannot be deleted"    

def DeleteSample(_conn, _sampleID):
    if DoesIDExist(_conn, "SAMPLE", _sampleID) == "TRUE":
        c = _conn.cursor()
        c.execute("DELETE FROM SampleTable WHERE sampleID=?",(_sampleID,))
        _conn.commit()
        LoggingAPI.Log("Sample: " + _sampleID +  " deleted!")#logging
        LoggingAPI.IndividualLog("Sample: " + _sampleID +  " deleted!", _sampleID)
        return "Sample: " + _sampleID + " successfully deleted!"
    elif DoesIDExist(_conn, "SAMPLE", _sampleID) == "FALSE":
        return "Sample ID: " + _sampleID + " does not exist"  
         
        
    

