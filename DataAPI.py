import sqlite3
import LoggingAPI
import datetime
from datetime import *
import time
from datetime import date

##########---------->START: MISCELLANEOUS FUNCTIONS<--------------------##########
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

def LogoutAll(_conn):
    c = _conn.cursor()
    c.execute("UPDATE LoginTable SET loggedIn = ?", ("0",))
    _conn.commit()

def AddUser(_conn, _username, _password, _accessLevelTemp):
    try:
        if _accessLevelTemp == "Customer":
            _accessLevel = 0
        elif _accessLevelTemp == "Employee":
            _accessLevel = 1
        elif _accessLevelTemp == "Supervisor":
            _accessLevel = 2

        c = _conn.cursor()
        c.execute("INSERT INTO LoginTable (username, password, accessLevel, loggedIn) VALUES (?, ?, ?, ?)",(_username,_password, int(_accessLevel), 0))
        _conn.commit()
        LoggingAPI.Log(_conn, "Added new user: " + _username + " with access level of " + _accessLevelTemp)
        return("Successfully added user " + _username)

    except sqlite3.Error as error:
        return(error)   

def DeleteUser(_conn , _username):
    c = _conn.cursor()
    c.execute("SELECT * FROM LoginTable WHERE username = ?", (_username,))  
    result = c.fetchone()
    if result is None:
        message =  "User: " + _username + " doesn't exist! Cannot be deleted."
        return message
    else:
        c.execute("DELETE FROM LoginTable WHERE username=?",(_username,))
        _conn.commit()
        message = "User: " + _username + " successfully deleted!"
        LoggingAPI.Log(_conn, message)
        return message
        
def GetUsernames(_conn):
    c = _conn.cursor()
    c.execute("SELECT * FROM LoginTable WHERE accessLevel != ?", (0,))
    results = c.fetchall()
    usernames = []
    for result in results:
        usernames.append(result[0])
    return usernames

def CheckAllSampleDates(_conn):
    c = _conn.cursor()
    c.execute("SELECT * FROM SampleTable")
    results = c.fetchall()
    output = ""
    for result in results:
        tempID = result[0]
        tempDate = result[13]
        tempType  = result[12]
        if SampleDateCheck(tempDate,tempType) != "FALSE":
            output = output + ("Sample " + tempID + SampleDateCheck(tempDate,tempType))
            output = output + '\n'
    return(output) 
##########---------->START: MISCELLANEOUS FUNCTIONS<--------------------##########

##########---------->START: FUNCTIONS FOR FRIDGES<--------------------##########
def AddFridge(_conn, _fridgeID, _temperature, _numShelves, _widthShelves, _rate):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO FridgeTable (fridgeID, temperature, numShelves, widthShelves, rate) VALUES (?, ?, ?, ?, ?)",(_fridgeID,int(_temperature), int(_numShelves), int(_widthShelves), float(_rate)))
        _conn.commit()
        LoggingAPI.Log(_conn, "Added new fridge: " + _fridgeID)
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
    if _posX <= fridgeX and _posY <= fridgeY and _posX >= 1 and _posY >= 1:
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
        LoggingAPI.Log(_conn, "Fridge: " + _fridgeID +  " deleted!")
        return "Fridge " + _fridgeID +  " successfully deleted"
    elif IsFridgeEmpty(_conn, _fridgeID) == "FALSE":
        return "Fridge does not exist or is not empty - cannot be deleted" 

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
##########---------->END: FUNCTIONS FOR FRIDGES<--------------------##########

##########---------->START: FUNCTIONS FOR BOXES<--------------------##########
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
        LoggingAPI.IndividualLog(_conn, stringMessage ,currentSample)

def MoveBox(_conn, _boxID, _fridgeID, _fridgeX, _fridgeY):
    if DoesIDExist(_conn, "FRIDGE", _fridgeID) == "TRUE" and DoesIDExist(_conn, "BOX", _boxID) == "TRUE" :
        fridgePosFree = IsFridgePositionFree(_conn, _fridgeID, _fridgeX, _fridgeY)
        if fridgePosFree == "TRUE":
            if IsFridgeFull(_conn, _fridgeID) == "TRUE":
                return ("Fridge: " + _fridgeID + " is full, please select another box!")
            else:
                c = _conn.cursor()
                c.execute("UPDATE BoxTable SET fridgeID =?, fridgeX =?, fridgeY =? WHERE boxID =?",(_fridgeID, _fridgeX, _fridgeY, _boxID,))
                _conn.commit()
                stringMessage = "Box " + _boxID + " was moved to Fridge " + _fridgeID + " (" + str(_fridgeX) + "," + str(_fridgeY) + ")"
                LoggingAPI.Log(_conn, stringMessage)
                BoxLog(_conn, _boxID, _fridgeID)
                return (stringMessage)
        elif fridgePosFree != "TRUE":
            return fridgePosFree
    elif DoesIDExist(_conn, "FRIDGE", _fridgeID) == "FALSE":
        return "Fridge ID " + _fridgeID + " does not exist" 
    elif DoesIDExist(_conn, "BOX", _boxID) == "FALSE":
        return "Box ID " + _boxID + " does not exist" 

def AddBox(_conn, _boxID, _fridgeID, _fridgeX, _fridgeY, _boxX, _boxY, _boxZ):
    try:
        c = _conn.cursor()
        fridgePosFree = IsFridgePositionFree(_conn, _fridgeID, _fridgeX, _fridgeY)
        if fridgePosFree == "TRUE":
            c.execute("INSERT INTO BoxTable (boxID, fridgeID, fridgeX, fridgeY, boxX, boxY, boxZ) VALUES (?, ?, ?, ?, ?, ?, ?)",(_boxID, _fridgeID, int(_fridgeX), int(_fridgeY), int(_boxX), int(_boxY), int(_boxZ)))
            _conn.commit()
            stringMessage = ("Added new box: " + _boxID + " to fridge: " + _fridgeID + " at position (" + str(_fridgeX) + "," + str(_fridgeY) + ")")
            LoggingAPI.Log(_conn, stringMessage)
            return("Successfully added Box " + _boxID)
        else:
            return (fridgePosFree + " in fridge: " + _fridgeID)

    except sqlite3.Error as error:
        return(error)

def IsBoxPositionFree(_conn, _boxID, _posX, _posY, _posZ):
    c = _conn.cursor()
    c.execute("SELECT * FROM BoxTable WHERE boxID=?",(_boxID,))
    result = c.fetchone()
    boxX = result[4]
    boxY = result[5]
    boxZ = result[6]
    if _posX <= boxX and _posY <= boxY and _posZ <= boxZ and _posX >= 1 and _posY >= 1 and _posZ >= 1:
        c.execute("SELECT * FROM SampleTable WHERE boxID=? AND boxX=? AND boxY=? AND boxZ=?",(_boxID,_posX, _posY, _posZ,))
        LocResults = c.fetchall()
        count = 0;
        for result in LocResults:
            count = count + 1
        if count > 0:
            return "Position already taken"
        elif count == 0:
            return "TRUE" 
    elif _posX > boxX or _posX < 1:
        return "Invalid X location"
    elif _posY > boxY or _posY < 1:
        return "Invalid Y location"
    elif _posZ > boxZ or _posZ < 1:
        return "Invalid Z location"

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
        LoggingAPI.Log(_conn, "Box " + _boxID +  " deleted")
        return "Box " + _boxID +  " successfully deleted"
    elif IsBoxEmpty(_conn, _boxID) == "FALSE":
        return "Box does not exist or is not empty - cannot be deleted"

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
##########---------->END: FUNCTIONS FOR BOXES<--------------------##########

##########---------->START: FUNCTIONS FOR SAMPLES<--------------------##########
def AddSample(_conn, _sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState):
    try:
        c = _conn.cursor()
        checkCollection = CheckCollection(_conn, _collectionTitle)
        if checkCollection == "TRUE":
            checkBox = DoesIDExist(_conn, "BOX", _boxID)
            if checkBox == "TRUE":
                boxPosFree = IsBoxPositionFree(_conn, _boxID, _boxX, _boxY, _boxZ)
                if boxPosFree == "TRUE":
                    c.execute("INSERT INTO SampleTable(sampleID , boxID, boxX, boxY, boxZ, sampleType, originCountry, collectionDate, entryDate, subjectAge, tubeRating, collectionTitle, returnType, returnDate, phenotypeValue, diseaseState) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(_sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState))
                    _conn.commit()
                    
                    _FridgeID = ReturnFridgeSampleIn(_conn,_sampleID)
                    fridgeTemp = ReturnTempOfFridge(_conn,_FridgeID) 
                    stringMessage = ("Added new sample: " + _sampleID + " to box " + _boxID + "(" + str(_boxX) + "," + str(_boxY) + "," + str(_boxZ) + ") in fridge: " + _FridgeID + " (temperature = " + fridgeTemp + ")")

                    LoggingAPI.IndividualLog(_conn, stringMessage, _sampleID)
                    LoggingAPI.Log(_conn, stringMessage) 
                    return ("Successfully added sample " + _sampleID)             
                else:
                    return (boxPosFree + " in box " + _boxID)
            else:
                return "Box " + _boxID + " does not exist"
        else:
            return(checkCollection)
    except sqlite3.Error as error:
        return error

def AddSampleTest(_conn, _sampleID, _testType, _testResult):
    try:
        checkSample = DoesIDExist(_conn, "SAMPLE", _sampleID)
        if checkSample == "TRUE":
            c = _conn.cursor()
            c.execute("INSERT INTO SampleTestTable (sampleID, testType, testResult) VALUES (?, ?, ?)",(_sampleID, _testType, _testResult))
            _conn.commit()
            LoggingAPI.IndividualLog(_conn, "Added new test: " + _testType + " to sample: " + _sampleID, _sampleID)
            return("Successfully added sample test for sample ID " + _sampleID)
        else:
            return "Sample ID " + _sampleID + " does not exist - cannot add sample test"
    except sqlite3.Error as error:
        return(error)

def MoveSample(_conn, _sampleID, _boxID, _posX , _posY, _posZ):
    c = _conn.cursor()
    checkSample = DoesIDExist(_conn, "SAMPLE", _sampleID)
    if checkSample == "TRUE":
        checkBox = DoesIDExist(_conn, "BOX", _boxID)
        if checkBox == "TRUE":
            if IsBoxFull(_conn, _boxID) == "TRUE":
                return("Box " + _boxID + " is full - please select another box")
            else: 
                boxPosFree = IsBoxPositionFree(_conn, _boxID, _posX, _posY, _posZ)
                if boxPosFree == "TRUE":
                    c.execute("UPDATE SampleTable SET boxID=?, boxX=?, boxY=?, boxZ=? WHERE sampleID=?", (_boxID,_posX,_posY,_posZ,_sampleID,))
                    _conn.commit()
                
                    _fridgeID = ReturnFridgeSampleIn(_conn, _sampleID)
                    _fridgeTemp = ReturnTempOfFridge(_conn, _fridgeID)
                    stringMessage = ("Sample: " + _sampleID + " was moved into Box " + _boxID + " in Fridge " + _fridgeID + " with temperature of " + _fridgeTemp)
                    LoggingAPI.IndividualLog(_conn, stringMessage, _sampleID)
                    LoggingAPI.Log(_conn, stringMessage)
                    return ("Successfully moved Sample ID " + _sampleID + " into Box " + _boxID)
                else:
                    return boxPosFree + " in box " + _boxID
        else:
            return "Box ID " + _boxID + " does not exist"
    else:
        return "Sample ID " + _sampleID + " does not exist"

def DeleteSample(_conn, _sampleID):
    if DoesIDExist(_conn, "SAMPLE", _sampleID) == "TRUE":
        DeleteSampleTest(_conn, _sampleID)
        DeleteSampleCollectionInvoiceEntry(_conn, _sampleID)
        c = _conn.cursor()
        c.execute("DELETE FROM SampleTable WHERE sampleID=?",(_sampleID,))
        _conn.commit()
        LoggingAPI.Log(_conn, "Sample: " + _sampleID +  " deleted!")
        LoggingAPI.IndividualLog(_conn, "Sample: " + _sampleID +  " deleted!", _sampleID)
        return "Sample " + _sampleID + " successfully deleted"
    elif DoesIDExist(_conn, "SAMPLE", _sampleID) == "FALSE":
        return "Sample ID " + _sampleID + " does not exist"  
         
def DeleteSampleTest(_conn, _sampleID):
    checkSample = DoesIDExist(_conn, "SAMPLE", _sampleID)
    if checkSample == "TRUE":
        c = _conn.cursor()
        c.execute("DELETE FROM SampleTestTable WHERE sampleID=?",(_sampleID,))
        _conn.commit()
        return "Successfully deleted sample test from sample ID " + _sampleID
    else:
        return checkSample + " - cannot delete sample test"

def DeleteSampleCollectionInvoiceEntry(_conn, _sampleID):
    checkSample = DoesIDExist(_conn, "SAMPLE", _sampleID)
    if checkSample == "TRUE":
        c = _conn.cursor()
        c.execute("DELETE FROM CollectionInvoiceTable WHERE sampleID=?",(_sampleID,))
        _conn.commit()
        return "TRUE"
    else:
        return checkSample + " - cannot delete"
##########---------->END: FUNCTIONS FOR SAMPLES<--------------------##########

##########---------->START: FUNCTIONS FOR COLLECTIONS<--------------------##########
def AddCollection(_conn, _collectionTitle, _donorID, _clientName, _clientPhone, _clientEmail, _clientOrganization, _clientStreet, _clientCity, _clientCountry, _clientPostalCode):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO CollectionTable (collectionTitle, donorID, clientName, clientPhoneNumber, clientEmail, clientOrganization, clientStreet, clientCity, clientCountry, clientPostalCode) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",(_collectionTitle, _donorID, _clientName, _clientPhone, _clientEmail, _clientOrganization, _clientStreet, _clientCity, _clientCountry, _clientPostalCode,))
        _conn.commit()
        return("Successfully added Collection " + _collectionTitle)

    except sqlite3.Error as error:
        return(error)

def DeleteCollection(_conn , _collectionTitle):
    c = _conn.cursor()
    c.execute("SELECT * FROM SampleTable WHERE collectionTitle = ?", (_collectionTitle,))  
    result = c.fetchone()
    if result is None:
        checkCollection = CheckCollection(_conn, _collectionTitle)
        if checkCollection == "TRUE":
            c.execute("DELETE FROM CollectionTable WHERE collectionTitle=?",(_collectionTitle,))
            _conn.commit()
            message =  "Collection " + _collectionTitle + " successfully deleted"
            LoggingAPI.Log(_conn, message)
            return message
        else:
            return checkCollection + " - cannot be deleted"
    else:
        return "Collection " + _collectionTitle + " is not empty - cannot be deleted"
            
def GetCollectionTitles(_conn):
    c = _conn.cursor()
    c.execute("SELECT collectionTitle FROM CollectionTable")
    collectionList = c.fetchall()
    return collectionList
##########---------->END: FUNCTIONS FOR COLLECTIONS<--------------------##########

##########---------->START: FUNCTIONS FOR TELLING USER A RETURN/DESTROY DATE IS APPROACHING<--------------------##########
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

def GetSampleTypes():
    return["Urine", "Blood", "Platelets", "Skin cells", "Organ tissue"]

def GetSampleDays(_conn, _sampleID):
    c = _conn.cursor()
    TempID = _sampleID
    c.execute("SELECT * FROM SampleTable WHERE sampleID=?",(TempID,))
    result = c.fetchone()
    startDate = result[8]
    years = int(startDate[0:4])
    months = int(startDate[5:7])
    days = int(startDate[8:10])
    startDate = datetime(years,months,days)
    currentDate = datetime.today()
    delta = currentDate - startDate
    delta = delta.days
    return delta 
##########---------->END: FUNCTIONS FOR TELLING USER A RETURN/DESTROY DATE IS APPROACHING<--------------------##########

##########---------->START: FUNCTIONS FOR AUTOMATICALLY ADDING SAMPLES<--------------------##########
def CheckFridge(_conn, _fridgeID):
    result = DoesIDExist(_conn, "FRIDGE", _fridgeID)
    if result == "FALSE":
        return ("Fridge " + _fridgeID + " does not exist")
    else:
        return "TRUE"

def CheckBox(_conn , _boxID, _boxX, _boxY, _boxZ):
    result = DoesIDExist(_conn,"BOX",_boxID)
    if result == "FALSE":
        return ("Box " + _boxID + " does not exist")
    result = IsBoxPositionFree(_conn, _boxID,_boxX, _boxY, _boxZ)
    if result != "TRUE":
        return ("Box position already taken " + str(_boxX) + "," + str(_boxY) + "," + str(_boxZ))
    return "TRUE"

def CheckSampleID(_conn, _sampleID):
    result = DoesIDExist(_conn, "SAMPLE", _sampleID)
    if result == "TRUE":
        return ("Sample " + _sampleID + " already exists")
    else:
        return "TRUE"

def CheckCollection(_conn, _collectionID):
    c = _conn.cursor()
    c.execute("SELECT * FROM CollectionTable WHERE collectionTitle =?",(_collectionID,))
    result = c.fetchone()
    if result is None:
        return ("Collection " + _collectionID + " does not exist")
    else:
        return "TRUE"

def CheckReturnStatus(_returnType):
    if _returnType == "Destroy" or _returnType == "Return":
        return "TRUE"
    else:
        return "FALSE"

def CheckSampleType(_sampleType):
    if _sampleType == "Blood" or _sampleType == "Urine" or _sampleType == "Platelets" or _sampleType == "Skin cells" or _sampleType == "Organ tissue":
        return "TRUE"
    else:
        return "FALSE"
        
def CheckValidEntry(_conn, _fileName):
    try:
        f = open(_fileName, 'r')
    except:
        return "That file does not exist"    
    lines = f.readlines()
    count = 0
    for line in lines:
        count = count + 1
        info = line.split(",")
        tempSampleID = info[0]
        sampleIDResult = CheckSampleID(_conn, tempSampleID)
        if sampleIDResult != "TRUE":
            return ("Failed at line " + str(count) + ": " + sampleIDResult)  
        tempFridgeID = info[1]
        fridgeResult = CheckFridge(_conn, tempFridgeID)
        if fridgeResult != "TRUE":
            return ("Failed at line " + str(count) + ": " + fridgeResult)
        tempBoxID = info[2]
        tempBoxX = int(info[3])
        tempBoxY = int(info[4])
        tempBoxZ = int(info[5])
        boxResult = CheckBox(_conn, tempBoxID, tempBoxX, tempBoxY, tempBoxZ)
        if boxResult != "TRUE":
            return ("Failed at line " + str(count) + ": " + boxResult)
        tempCollection = info[6]
        collectionResult = CheckCollection(_conn, tempCollection)
        if collectionResult != "TRUE":
            return ("Failed at line " + str(count) + ": " + collectionResult)
        tempReturnType = info[12]
        if CheckReturnStatus(tempReturnType) != "TRUE":
            return ("Failed at line " + str(count) + ": " + "return type not of defined set")
        tempSampleType = info[7]        
        if CheckSampleType(tempSampleType) != "TRUE":
            return ("Failed at line " + str(count) + ": " + "sample type not of defined set")
    f.close()   
    return "TRUE"

def AutoAddSamples(_conn, _fileName):
    try:
        f = open(_fileName, 'r')
    except:
        return("That file does not exist")
    lines = f.readlines()
    count = 0
    error = ""
    for line in lines:
        count = count + 1
        info = line.split(",")
        try:
            sampleID = info[0]
            boxID = info[2]
            boxX = int(info[3])
            boxY = int(info[4])
            boxZ  = int(info[5])
            collectionTitle = info[6]
            sampleType = info[7]
            originCountry = info[8]
            collectionDate = info[9]
            entryDate = str(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M%S'))
            subjectAge = int(info[10])
            tubeRating = int(info[11])
            returnType = info[12]
            returnDate = info[13]
            phenotypeValue = info[14]
            diseaseState = info[15]
            AddSample(_conn, sampleID, boxID, boxX, boxY, boxZ, sampleType, originCountry,collectionDate,entryDate,subjectAge,tubeRating,collectionTitle,returnType,returnDate,phenotypeValue,diseaseState)       
        except:
            error = error + "Failed to add sample at line: " + str(count) + '\n'
    if error == "":
        return "TRUE"
    else:
        return error

def CommitAuto(_conn, _fileName):
    fileName = "ToAdd/" + _fileName
    result = CheckValidEntry(_conn, fileName) 
    if result == "TRUE":
        return AutoAddSamples(_conn, fileName)    
    else:
        return result      
##########---------->END: FUNCTIONS FOR AUTOMATIC ADDING SAMPLES<--------------------##########

##########---------->START: FUNCTIONS FOR STOCK TAKE<--------------------##########
def StockTake(_conn, _num, _queryType):
    c = _conn.cursor()
    if _queryType == 'Fridges':
        c.execute("SELECT * FROM FridgeTable")
    elif _queryType == 'Boxes':
        c.execute("SELECT * FROM BoxTable")
    elif _queryType == 'Samples':
        c.execute("SELECT * FROM SampleTable")
    results = c.fetchall()
    counter = 0
    for result in results:
        counter = counter + 1
    if counter == int(_num):
        return("Stock take successful, there are " + str(_num) + " " + _queryType + " in storage")
    else:
        return("Stock take mismatch, there are " + str(counter) + " " + _queryType + " in storage")
##########---------->END: FUNCTIONS FOR STOCK TAKE<--------------------##########
