from tkinter import *
import sqlite3
import Startup


def ShowSampleTypes(conn):
    c = conn.cursor()

    customer_window = Tk()
    customer_window.geometry("250x150")
    customer_window.title("SAMPLE TYPES")

    def LogOut():
        customer_window.destroy()
        Startup.Start_Window(conn)

    backButton = Button(customer_window, text = "Return", command = LogOut, height = 1, width = 8)

    c.execute("SELECT count(*) FROM SampleTable WHERE sampleType=?", ("Urine",))
    urineCount = c.fetchall()[0][0]
    c.execute("SELECT count(*) FROM SampleTable WHERE sampleType=?", ("Blood",))
    bloodCount = c.fetchall()[0][0]
    c.execute("SELECT count(*) FROM SampleTable WHERE sampleType=?", ("Platelets",))
    plateletsCount = c.fetchall()[0][0]
    c.execute("SELECT count(*) FROM SampleTable WHERE sampleType=?", ("Skin cells",))
    skinCount = c.fetchall()[0][0]
    c.execute("SELECT count(*) FROM SampleTable WHERE sampleType=?", ("Organ tissue",))
    organCount = c.fetchall()[0][0]
    
    urineLabel = Label(customer_window, text = "Urine: " + "\t\t" + str(urineCount), anchor = "w", height = 1, width = 20)
    bloodLabel = Label(customer_window, text = "Blood: " + "\t\t" + str(bloodCount), anchor = "w", height = 1, width = 20)
    plateletsLabel = Label(customer_window, text = "Platelets: " + "\t" + str(plateletsCount), anchor = "w", height = 1, width = 20)
    skinLabel = Label(customer_window, text = "Skin cell: " + "\t\t" + str(skinCount), anchor = "w", height = 1, width = 20)
    organLabel = Label(customer_window, text = "Organ tissue: " + "\t" + str(organCount), anchor = "w", height = 1, width = 20)

    urineLabel.grid(row = 0, columnspan = 2)
    bloodLabel.grid(row = 1, columnspan = 2)
    plateletsLabel.grid(row = 2, columnspan = 2) 
    skinLabel.grid(row = 3, columnspan = 2) 
    organLabel.grid(row = 4, columnspan = 2)
    backButton.grid(row = 5) 

    customer_window.mainloop()
    c.close()
    conn.close()
