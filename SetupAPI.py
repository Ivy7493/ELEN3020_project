import os


def CreateLogsFolder():
    try:
        os.mkdir('Logs')
    except:
        pass

def CreateInvoicesFolder():
    try:
        os.mkdir('Invoices')
    except:
        pass
    f = open("Invoices/InvoiceIndex", "a+")
    f.close()

def CreateToAddFolder():
    try:
        os.mkdir('ToAdd')
    except:
        pass
    

def CreateSampleTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS SampleTable(
                                    sampleID TEXT NOT NULL PRIMARY KEY,
                                    boxID TEXT NOT NULL,
                                    boxX INTEGER NOT NULL,     
                                    boxY INTEGER NOT NULL,
                                    boxZ INTEGER NOT NULL,
                                    sampleType TEXT NOT NULL,
                                    originCountry TEXT NOT NULL,
                                    collectionDate TEXT NOT NULL,
                                    entryDate TEXT NOT NULL,
                                    subjectAge INTEGER NOT NULL,
                                    tubeRating INTEGER NOT NULL,
                                    collectionTitle TEXT NOT NULL,
                                    returnType TEXT NOT NULL,
                                    returnDate TEXT NOT NULL,
                                    phenotypeValue TEXT NOT NULL,
                                    diseaseState TEXT NOT NULL,
                                    FOREIGN KEY(boxID) REFERENCES BoxTable(boxID),
                                    FOREIGN KEY(collectionTitle) REFERENCES CollectionTable(collectionTitle))""")
    _conn.commit()
                                    
def CreateCollectionTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS CollectionTable(
                                    collectionTitle TEXT NOT NULL PRIMARY KEY,
                                    donorID TEXT NOT NULL,
                                    clientName TEXT NOT NULL,
                                    clientPhoneNumber TEXT NOT NULL,
                                    clientEmail TEXT NOT NULL,
                                    clientOrganization TEXT NOT NULL,
                                    clientStreet TEXT NOT NULL,
                                    clientCity TEXT NOT NULL,
                                    clientCountry TEXT NOT NULL,
                                    clientPostalCode TEXT NOT NULL)""")
    _conn.commit()

def CreateFridgeTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS FridgeTable(
                                    fridgeID TEXT NOT NULL PRIMARY KEY,
                                    temperature INTEGER NOT NULL,
                                    numShelves INTEGER NOT NULL,
                                    widthShelves INTEGER NOT NULL,
                                    rate FLOAT NOT NULL)""")
    _conn.commit()

def CreateLoginTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS LoginTable(
                                    username TEXT NOT NULL PRIMARY KEY,
                                    password TEXT NOT NULL,
                                    accessLevel INTEGER NOT NULL,
                                    loggedIn INTEGER NOT NULL)""")
    _conn.commit()                               

def CreateBoxTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS BoxTable(
                                    boxID TEXT NOT NULL PRIMARY KEY,
                                    fridgeID TEXT NOT NULL,
                                    fridgeX INTEGER NOT NULL,
                                    fridgeY INTEGER NOT NULL,
                                    boxX INTEGER NOT NULL,                                    
                                    boxY INTEGER NOT NULL,                                    
                                    boxZ INTEGER NOT NULL,
                                    FOREIGN KEY(fridgeID) REFERENCES FridgeTable(fridgeID))""")
    _conn.commit()  

def CreateSampleTestTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS SampleTestTable(
                                    sampleID TEXT NOT NULL,
                                    testType TEXT NOT NULL,
                                    testResult TEXT NOT NULL,                                    
                                    FOREIGN KEY(sampleID) REFERENCES SampleTable(sampleID))""")
    _conn.commit()

def CreateCollectionInvoiceTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS CollectionInvoiceTable(
                                    collectionTitle TEXT NOT NULL,
                                    sampleID TEXT NOT NULL,
                                    invoiceCheck INTEGER NOT NULL,                                    
                                    FOREIGN KEY(collectionTitle) REFERENCES CollectionTable(collectionTitle),
                                    FOREIGN KEY(sampleID) REFERENCES SampleTable(sampleID))""")

#NOTE: This is for prototype testing purposes only
def CreateAdmin(_conn):
    c = _conn.cursor()
    c.execute("SELECT * FROM LoginTable WHERE username = ?", ("admin",))
    result = c.fetchone()
    if result is None:
        c.execute("INSERT INTO LoginTable  (username, password, accessLevel, loggedIn) VALUES (?,?,?,?)", ("admin", "admin", 2, 0))
        _conn.commit()
    else:
        pass

def CreateAllTables(_conn):
    CreateFridgeTable(_conn)
    CreateBoxTable(_conn)
    CreateSampleTable(_conn)
    CreateLoginTable(_conn)
    CreateSampleTestTable(_conn)
    CreateCollectionTable(_conn)
    CreateCollectionInvoiceTable(_conn)
    CreateLogsFolder()
    CreateInvoicesFolder()
    CreateToAddFolder()
    CreateAdmin(_conn)

#JESSE'S COMMENT
