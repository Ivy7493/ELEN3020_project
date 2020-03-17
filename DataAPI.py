import sqlite3

def AddFridge(_conn, _fridgeID, _temperature, _numShelves, _widthShelves):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO FridgeTable (fridgeID, temperature, numShelves, widthShelves) VALUES (?, ?, ?, ?)",(_fridgeID,int(_temperature), int(_numShelves), int(_widthShelves)))
        _conn.commit()
        return("Successfully added Fridge " + _fridgeID)

    except sqlite3.Error as error:
        return(error)

#def IsFridgeFull(_conn, _fridgeID)
#    c = _conn.cursor()
#    c.execute("SELECT * FROM FridgeTable WHERE fridgeID=?", _fridgeID)
#    results = c.fetchall()
#    count = 0
#    for result in results:
#        count = count + 1 
        
    


def AddBox(_conn, _boxID, _fridgeID, _boxX, _boxY, _boxZ):
    try:
        c = _conn.cursor()
        c.execute("INSERT INTO BoxTable (boxID, fridgeID, boxX, boxY, boxZ) VALUES (?, ?, ?, ?, ?)",(_boxID, _fridgeID,int(_boxX), int(_boxY), int(_boxZ)))
        _conn.commit()
        return("Successfully added Box " + _boxID)

    except sqlite3.Error as error:
        return(error)

