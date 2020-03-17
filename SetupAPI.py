
def CreateFridgeTable(conn):
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS FridgeTable(
                                    fridgeID TEXT NOT NULL PRIMARY KEY,
                                    temperature INTEGER NOT NULL,
                                    numShelves INTEGER NOT NULL,
                                    widthShelves INTEGER NOT NULL)""")
    #c.execute("""CREATE UNQIUE INDEX IF NOT EXIST fridgeID ON FridgeTable(fridgeID)""")
    conn.commit()                               


def CreateAllTables(conn):
    c = conn.cursor()
