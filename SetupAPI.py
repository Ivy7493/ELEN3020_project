
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
                                    sampleHistory TEXT NOT NULL,
                                    subjectAge INTEGER NOT NULL,
                                    tubeRating INTEGER NOT NULL,
                                    collectionTitle TEXT NOT NULL,
                                    donorPhone TEXT NOT NULL,
                                    authorisedPhone TEXT NOT NULL,
                                    returnType TEXT NOT NULL,
                                    returnDate TEXT NOT NULL,
                                    testResults TEXT NOT NULL,
                                    phenotypeValue TEXT NOT NULL,
                                    diseaseState TEXT NOT NULL,
                                    FOREIGN KEY(boxID) REFERENCES BoxTable(boxID))""")
    _conn.commit()
                                    

def CreateFridgeTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS FridgeTable(
                                    fridgeID TEXT NOT NULL PRIMARY KEY,
                                    temperature INTEGER NOT NULL,
                                    numShelves INTEGER NOT NULL,
                                    widthShelves INTEGER NOT NULL)""")
    _conn.commit()                               

def CreateBoxTable(_conn):
    c = _conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS BoxTable(
                                    boxID TEXT NOT NULL PRIMARY KEY,
                                    fridgeID TEXT NOT NULL,
                                    boxX INTEGER NOT NULL,                                    
                                    boxY INTEGER NOT NULL,                                    
                                    boxZ INTEGER NOT NULL,
                                    FOREIGN KEY(fridgeID) REFERENCES FridgeTable(fridgeID))""")
    _conn.commit()  



def CreateAllTables(_conn):
    CreateFridgeTable(_conn)
    CreateBoxTable(_conn)
    CreateSampleTable(_conn)


