import sqlite3



def AddFridge(_conn, _fridgeID, _temperature, _numShelves, _widthShelves):
    c = _conn.cursor()
    c.execute("INSERT INTO fridgeTable (fridgeID, temperature, numShelves, widthShelves) VALUES (?, ?, ?, ?)",(_fridgeID,int(_temperature), int(_numShelves), int(_widthShelves)))
    _conn.commit()
