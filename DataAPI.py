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

def BoxLog(_conn, _boxID, _fridgeID):
    c = _conn.cursor()
    temp = ReturnTempOfFridge(_conn,_fridgeID)
    c.execute("SELECT * FROM SampleTable WHERE boxID=?",(_boxID,))
    results = c.fetchall()
    count = 0
    for result in results:
        currentSample = result[0]
        count = count + 1
        stringMessage = "Sample: " + currentSample + " was moved to box: " + _boxID + " in fridge: " + _fridgeID + " with temperature of: " + temp
        LoggingAPI.IndividualLog(stringMessage ,currentSample)


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
        return "Not a Valid FridgeID"
    elif DoesIDExist(_conn, "BOX", _boxID) == "FALSE":
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

def AddSample(_conn, _sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _sampleHistory, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState):
    try:
        c = _conn.cursor()
        if IsPositionFree(_conn, _boxID, _boxX, _boxY, _boxZ) == "TRUE":
            c.execute("INSERT INTO SampleTable(sampleID , boxID, boxX, boxY, boxZ, sampleType, originCountry, collectionDate, entryDate, sampleHistory, subjectAge, tubeRating, collectionTitle, returnType, returnDate, phenotypeValue, diseaseState) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(_sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _sampleHistory, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState))
            _conn.commit()
            
            _FridgeID = ReturnFridgeSampleIn(_conn,_sampleID)
            fridgeTemp = ReturnTempOfFridge(_conn,_FridgeID) 
            stringMessage = ("Added new sample: " + _sampleID + " to fridge: " + _FridgeID + " with temperature of: " + fridgeTemp)

            LoggingAPI.IndividualLog(stringMessage, _sampleID)
            LoggingAPI.Log(stringMessage) #logging
            return ("Successfully added sample " + _sampleID)             
        else:
            return (IsPositionFree(_conn, _boxID, _boxX, _boxY, _boxZ) + " in box: " + _boxID)
           
    except sqlite3.Error as error:
        return error

def AddSampleTest(_conn, _sampleID, _testType, _testResult):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO SampleTestTable (sampleID, testType, testResult) VALUES (?, ?, ?)",(_sampleID, _testType, _testResult))
        _conn.commit()
        LoggingAPI.IndividualLog("Added new test: " + _testType + " to sample: " + _sampleID, _sampleID)
        return("Successfully added Sample Test for " + _sampleID)

    except sqlite3.Error as error:
        return(error)

def ReturnTempOfFridge(_conn, _fridgeID):
    c = _conn.cursor()
    c.execute("SELECT temperature FROM FridgeTable WHERE fridgeID=?",(_fridgeID,))
    result = c.fetchone()
    resultTemp = str(result[0])
    return resultTemp

def ReturnFridgeSampleIn(_conn, _sampleID):
    c = _conn.cursor()
    c.execute("SELECT boxID FROM SampleTable WHERE sampleID=?",(_sampleID,))
    result1 = c.fetchone()
    boxResult = result1[0]
    c.execute("SELECT fridgeID FROM BoxTable WHERE boxID=?",(boxResult,))
    result2 = c.fetchone()
    fridgeResult = result2[0]
    return fridgeResult       

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
    
        _fridgeID = ReturnFridgeSampleIn(_conn, _sampleID)
        _fridgeTemp = ReturnTempOfFridge(_conn, _fridgeID)
        stringMessage = "Sample: " + _sampleID + " was moved into box: " + _boxID + " in fridge: " + _fridgeID + " with temperature of: " + _fridgeTemp

        LoggingAPI.IndividualLog(stringMessage, _sampleID)
        LoggingAPI.Log(stringMessage) #logging
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
        DeleteSampleTest(_conn, _sampleID)
        c = _conn.cursor()
        c.execute("DELETE FROM SampleTable WHERE sampleID=?",(_sampleID,))
        _conn.commit()
        LoggingAPI.Log("Sample: " + _sampleID +  " deleted!")#logging
        LoggingAPI.IndividualLog("Sample: " + _sampleID +  " deleted!", _sampleID)
        return "Sample: " + _sampleID + " successfully deleted!"
    elif DoesIDExist(_conn, "SAMPLE", _sampleID) == "FALSE":
        return "Sample ID: " + _sampleID + " does not exist"  
         
def DeleteSampleTest(_conn, _sampleID):
    c = _conn.cursor()
    c.execute("DELETE FROM SampleTestTable WHERE sampleID=?",(_sampleID,))
    _conn.commit()


def FindEmptyFridge(_conn):
    c = _conn.cursor()
    c.execute("SELECT * FROM FridgeTable")
    results = c.fetchall()
    for result in results:
        tempID = result[0]
        #if IsFridgeFull(_conn, tempID) == "TRUE":
        #    print("Fridge: " + tempID + " is not avaible")
        if IsFridgeFull(_conn, tempID) == "FALSE":
            return ("Fridge: " + tempID + " is open for box insertion")
    return ("No Fridge is open for insertion")


def IsBoxFull(_conn, _boxID):
    c = _conn.cursor()
    c.execute("SELECT * FROM BoxTable WHERE boxID=?",(_boxID,))
    result = c.fetchone()
    boxX = result[2]
    boxY = result[3]
    boxZ = result[4]
    for x in range(1,boxX + 1):
        for y in range(1, boxY + 1):
            for z in range(1, boxZ + 1):
                if IsPositionFree(_conn, _boxID, x, y, z) == "TRUE":
                    return ("Box: " + _boxID + " is open for insertion, at position: " + str(x) + ", " + str(y) + ", " + str(z))
    return "TRUE"
                                 
    

def FindEmptyBox(_conn, _tempMin, _tempMax):
    c = _conn.cursor()
    c.execute("SELECT * FROM FridgeTable")
    results = c.fetchall()
    for result in results:
        fridgeID = result[0]
        fridgeTemp = result[1]
        if fridgeTemp <= _tempMax and fridgeTemp >= _tempMin and IsFridgeFull(_conn, fridgeID) == "FALSE":
            c.execute("SELECT * FROM BoxTable WHERE fridgeID=?",(fridgeID,))
            results1 = c.fetchall()
            for result1 in results1:
                tempBoxID = result1[0]
                boxFullResult = IsBoxFull(_conn, tempBoxID)
                if boxFullResult != "TRUE":
                    return (boxFullResult)                
                           
        #else:
        #    return ("fridge: " + fridgeID + " not open for sample insertion") 

    return ("No place found for insertion")


def AddCollection(_conn, _collectionTitle, _donorName, _donorPhone, _donorEmail, _donorOrganization, _authorisorName, _authorisorPhone, _authorisorEmail, _authorisorOrganization):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO CollectionTable (collectionTitle, donorName, donorPhoneNumber, donorEmail, donorOrganization, authorisorName, authorisorPhoneNumber, authorisorEmail, authorisorOrganization) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",(_collectionTitle, _donorName, _donorPhone, _donorEmail, _donorOrganization, _authorisorName, _authorisorPhone, _authorisorEmail, _authorisorOrganization,))
        _conn.commit()
        return("Successfully added Collection " + _collectionTitle)

    except sqlite3.Error as error:
        return(error)
            
def GetCollectionTitles(_conn):
    c = _conn.cursor()
    c.execute("SELECT collectionTitle FROM CollectionTable")
    collectionList = c.fetchall()
    return collectionList

def LogoutAll(_conn):
    c = _conn.cursor()
    c.execute("UPDATE LoginTable SET loggedIn = ?", ("0",))
    _conn.commit()
    
    

