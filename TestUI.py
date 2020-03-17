import SetupAPI
import sqlite3

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")
SetupAPI.CreateFridgeTable(conn)

def OpenAddFridge():
    conn = sqlite3.connect('test.db')
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    window_AddFridge = tk.Tk()
    window_AddFridge.geometry("300x300")
    window_AddFridge.title("ADD FRIDGE")

    #SETTING UP NEW FRIDGE FORM----------------------------------------------------------------
    tk.Label(window_AddFridge, text = "Fridge ID").grid(row = 0)
    fridgeID = tk.Entry(window_AddFridge)
    fridgeID.grid(row = 0, column = 1)

    tk.Label(window_AddFridge, text = "Temperature").grid(row = 1)
    temp = tk.Entry(window_AddFridge)
    temp.grid(row = 1, column = 1)

    tk.Label(window_AddFridge, text = "Number of Shelves").grid(row = 2)
    numShelves = tk.Entry(window_AddFridge)
    numShelves.grid(row = 2, column = 1)

    tk.Label(window_AddFridge, text = "Number of Boxes").grid(row = 3)
    numBoxes = tk.Entry(window_AddFridge)
    numBoxes.grid(row = 3, column = 1)

    tk.Label(window_AddFridge, text = "Width of Box (X)").grid(row = 4)
    boxX = tk.Entry(window_AddFridge)
    boxX.grid(row = 4, column = 1)

    tk.Label(window_AddFridge, text = "Length of Box (Y)").grid(row = 5)
    boxY = tk.Entry(window_AddFridge)
    boxY.grid(row = 5, column = 1)

    tk.Label(window_AddFridge, text = "Height of Box (Z)").grid(row = 6)
    boxZ = tk.Entry(window_AddFridge)
    boxZ.grid(row = 6, column = 1)

    def console_PrintFridge():
        print("Fridge ID: %s\nTemperature: %s\nNumShelves: %s\nNumBoxes: %s\nBox X: %s\nBox Y: %s\nBox Z: %s" % (fridgeID.get(), temp.get(), numShelves.get(), numBoxes.get(), boxX.get(), boxY.get(), boxZ.get()))

    def data_newFridge():
        c.execute("INSERT INTO fridgeTable (fridgeID, temperature, numShelves, numBoxes, boxX, boxY, boxZ) VALUES (?, ?, ?, ?, ?, ?, ?)",
    (str(fridgeID.get()), int(temp.get()), int(numShelves.get()), int(numBoxes.get()), int(boxX.get()), int(boxY.get()), int(boxZ.get())))
        conn.commit()

    tk.Button(window_AddFridge, text = 'Console Print', command = console_PrintFridge).grid(row = 7, column=1)
    tk.Button(window_AddFridge, text = 'Populate', command = data_newFridge).grid(row = 8, column=1)


    window_AddFridge.mainloop()
    c.close()
    conn.close()
    #----------------------------------------------------------------------------------------
