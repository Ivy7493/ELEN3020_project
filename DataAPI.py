import sqlite3
import LoggingAPI
from datetime import *

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
    c.execute("SELECT * FROM FridgeTable WHERE fridgeID=?", (_fridgeID,))
    results = c.fetchone()
    fridgeX = results[2]
    fridgeY = results[3]
    maxNumber = fridgeX * fridgeY

    for x in range(1, fridgeX + 1):
        for y in range (1, fridgeY + 1):
            if IsFridgePositionFree(_conn, _fridgeID, x, y) == "TRUE":
                return ("Fridge: " + _fridgeID + " is open for insertion at position: " + str(x) + ", " + str(y))
    return "TRUE" 

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


def MoveBox(_conn, _boxID, _fridgeID, _fridgeX, _fridgeY):
    fridgePosFree = IsFridgePositionFree(_conn, _fridgeID, _fridgeX, _fridgeY)
    if DoesIDExist(_conn, "FRIDGE", _fridgeID) == "TRUE" and DoesIDExist(_conn, "BOX", _boxID) == "TRUE" and fridgePosFree == "TRUE":
        if IsFridgeFull(_conn, _fridgeID) == "TRUE":
            return ("Fridge: " + _fridgeID + " is full, please select another box!")
        else:
            c = _conn.cursor()
            c.execute("UPDATE BoxTable SET fridgeID =?, fridgeX =?, fridgeY =? WHERE boxID =?",(_fridgeID, _fridgeX, _fridgeY, _boxID,))
            _conn.commit()
            stringMessage = "Box: " + _boxID + " was moved to fridge: " + _fridgeID + " (" + str(_fridgeX) + "," + str(_fridgeY) + ")"
            LoggingAPI.Log(stringMessage)
            BoxLog(_conn, _boxID, _fridgeID)
            return (stringMessage)
    elif DoesIDExist(_conn, "FRIDGE", _fridgeID) == "FALSE":
        return "FridgeID: " + _fridgeID + " does not exist!" 
    elif DoesIDExist(_conn, "BOX", _boxID) == "FALSE":
        return "BoxID: " + _boxID + " does not exist!" 
    elif fridgePosFree != "TRUE":
        return fridgePosFree


def AddBox(_conn, _boxID, _fridgeID, _fridgeX, _fridgeY, _boxX, _boxY, _boxZ):
    try:
        c = _conn.cursor()
        fridgePosFree = IsFridgePositionFree(_conn, _fridgeID, _fridgeX, _fridgeY)
        if fridgePosFree == "TRUE":
            c.execute("INSERT INTO BoxTable (boxID, fridgeID, fridgeX, fridgeY, boxX, boxY, boxZ) VALUES (?, ?, ?, ?, ?, ?, ?)",(_boxID, _fridgeID, int(_fridgeX), int(_fridgeY), int(_boxX), int(_boxY), int(_boxZ)))
            _conn.commit()
            stringMessage = ("Added new box: " + _boxID + " to fridge: " + _fridgeID + " at position (" + str(_fridgeX) + "," + str(_fridgeY) + ")")
            LoggingAPI.Log(stringMessage)
            return("Successfully added Box " + _boxID)
        else:
            return (fridgePosFree + " in fridge: " + _fridgeID)

    except sqlite3.Error as error:
        return(error)

def AddSample(_conn, _sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _sampleHistory, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState):
    try:
        c = _conn.cursor()
        boxPosFree = IsBoxPositionFree(_conn, _boxID, _boxX, _boxY, _boxZ)
        if boxPosFree == "TRUE":
            c.execute("INSERT INTO SampleTable(sampleID , boxID, boxX, boxY, boxZ, sampleType, originCountry, collectionDate, entryDate, sampleHistory, subjectAge, tubeRating, collectionTitle, returnType, returnDate, phenotypeValue, diseaseState) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(_sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _sampleHistory, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState))
            _conn.commit()
            
            _FridgeID = ReturnFridgeSampleIn(_conn,_sampleID)
            fridgeTemp = ReturnTempOfFridge(_conn,_FridgeID) 
            stringMessage = ("Added new sample: " + _sampleID + " to box " + _boxID + "(" + str(_boxX) + "," + str(_boxY) + "," + str(_boxZ) + ") in fridge: " + _FridgeID + " (temperature = " + fridgeTemp + ")")

            LoggingAPI.IndividualLog(stringMessage, _sampleID)
            LoggingAPI.Log(stringMessage) #logging
            return ("Successfully added sample " + _sampleID)             
        else:
            return (boxPosFree + " in box: " + _boxID)
           
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

def IsFridgePositionFree(_conn, _fridgeID, _posX, _posY):
    c = _conn.cursor()
    c.execute("SELECT * FROM FridgeTable WHERE fridgeID=?", (_fridgeID,))
    result = c.fetchone()
    fridgeX = result[2]
    fridgeY = result[3]
    if _posY <= fridgeX and _posY <= fridgeY and _posX >= 1 and _posY >= 1:
        c.execute("SELECT * FROM BoxTable WHERE fridgeID=? AND fridgeX=? AND fridgeY=?", (_fridgeID, _posX, _posY,))
        localResults = c.fetchall()
        count = 0;
        for result in localResults:
            count = count+1
        if count > 0:
            return "Position already taken" 
        elif count == 0:
            return "TRUE" 
    elif _posX > fridgeX or _posX < 1:
        return "Invalid X location" 
    elif _posY > fridgeY or _posY < 1:
        return "Invalid Y location"

def IsBoxPositionFree(_conn, _boxID, _posX, _posY, _posZ):
    c = _conn.cursor()
    c.execute("SELECT * FROM BoxTable WHERE boxID=?",(_boxID,))
    result = c.fetchone()
    boxX = result[2]
    boxY = result[3]
    boxZ = result[4]
    if _posX <= boxX and _posY <= boxY and _posZ <= boxZ and _posX >= 1 and _posY >= 1 and _posZ >= 1:
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
    boxPosFree = IsBoxPositionFree(_conn, _boxID, _posX, _posY, _posZ)


    if IsBoxFull(_conn, _boxID) == "TRUE":
        return("Box: " + _boxID + " is full, please select another box!")
    else: 
        if DoesIDExist(_conn, "SAMPLE", _sampleID) == "TRUE" and DoesIDExist(_conn, "BOX", _boxID) == "TRUE" and boxPosFree == "TRUE":
            c.execute("UPDATE SampleTable SET boxID=?, boxX=?, boxY=?, boxZ=? WHERE sampleID=?", (_boxID,_posX,_posY,_posZ,_sampleID,))
            _conn.commit()
        
            _fridgeID = ReturnFridgeSampleIn(_conn, _sampleID)
            _fridgeTemp = ReturnTempOfFridge(_conn, _fridgeID)
            stringMessage = ("Sample: " + _sampleID + " was moved into box: " + _boxID + " in fridge: " + _fridgeID + " with temperature of: " + _fridgeTemp)

            LoggingAPI.IndividualLog(stringMessage, _sampleID)
            LoggingAPI.Log(stringMessage)
            return ("Successfully moved sample: " + _sampleID + " into box: " + _boxID)
        elif DoesIDExist(_conn, "SAMPLE", _sampleID) == "FALSE":
            return "Sample ID: " + _sampleID + " does not exist!"
        elif DoesIDExist(_conn, "BOX", _boxID) == "FALSE":
            return "Box ID: " + _boxID + " does not exist!"
        elif boxPosFree != "TRUE":
            return boxPosFree


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
        fridgeID = result[0]
        if IsFridgeFull(_conn, fridgeID) != "TRUE":
            fridgeFullResult = IsFridgeFull(_conn, fridgeID)
            if fridgeFullResult != "TRUE":
                return fridgeFullResult
    return ("No fridge is open for insertion")


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
                if IsBoxPositionFree(_conn, _boxID, x, y, z) == "TRUE":
                    return ("Box: " + _boxID + " is open for insertion, at position: " + str(x) + ", " + str(y) + ", " + str(z))
    return "TRUE"
                                 
    

def FindEmptyBox(_conn, _tempMin, _tempMax):
    c = _conn.cursor()
    c.execute("SELECT * FROM FridgeTable")
    results = c.fetchall()
    for result in results:
        fridgeID = result[0]
        fridgeTemp = result[1]
        if fridgeTemp <= _tempMax and fridgeTemp >= _tempMin and IsFridgeFull(_conn, fridgeID) != "TRUE":
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

def SampleDateCheck(_returnDate, _returnType):
    date1 = _returnDate
    date2 = str(datetime.now())
    year1 = int(date1[0:4])
    year2 = int(date2[0:4])
    if year1 - year2 < 1:
        month1 = int(date1[5:7])
        month2 = int(date2[5:7])
        if month1 - month2 < 1:
            day1 = int(date1[8:10])
            day2 = int(date2[8:10])
            x = day1 - day2
            if x <= 7 and x >= 0:
                return(" needs to be " + _returnType + "ed in " + str(x) + " days")
            elif x < 0:
                return(" should have been " + _returnType + "ed already")
        elif month1 - month2 < 0:
            return(" should have been " + _returnType + "ed already")
    elif year1 - year2 < 0:
         return(" should have been " + _returnType + "ed already") 
    return ("FALSE")

def CheckAllSampleDates(_conn):
    c = _conn.cursor()
    c.execute("SELECT * FROM SampleTable")
    results = c.fetchall()
    output = ""
    for result in results:
        tempID = result[0]
        tempDate = result[14]
        tempType  = result[13]
        if SampleDateCheck(tempDate,tempType) != "FALSE":
            output = output + ("Sample " + tempID + SampleDateCheck(tempDate,tempType))
            output = output + '\n'
    return(output)               
    

