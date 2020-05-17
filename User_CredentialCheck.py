from tkinter import *
from tkinter.font import Font
import sqlite3
import Box_UI
import Fridge_UI
import Sample_UI
import Main_UI
import ViewMode_UI

def Check_Window(conn):
    window_check = Tk()
    window_check.title("Employee Login")
    window_check["bg"] = 'cadet blue'
    
    text = Text(window_check)
    myFont = Font(family = "fixedsys", size=12)
    text.configure(font=myFont)
    message = Label(window_check, text = "Enter username and password", font = myFont, bg ='cadet blue')
    message.grid(row = 3, column = 1)

    def checkCreds(): #checks the user's credentials
        n1 = entry_name.get()
        p1 = entry_pass.get()
        c = conn.cursor()
        c.execute("SELECT password FROM LoginTable WHERE username=?", (str(n1),))
        temp_password = c.fetchall()
        c.execute("SELECT clientPhoneNumber FROM CollectionTable WHERE clientName=?", (str(n1),))
        temp_number = c.fetchall()
        count = 0
        count2 = 0
        employeeLog = "FALSE"

        for result in temp_password:
            count = count + 1

        for result in temp_number:
            count2 = count2 + 1

        if count == 0:
            message['text'] = "No such username or password"
        elif count > 0:   
            employeeLog = "TRUE"
            c.execute("SELECT password FROM LoginTable WHERE username=?", (str(n1),))
            result = c.fetchone()[0]
            if p1 == result:
                c.execute("SELECT accessLevel FROM LoginTable WHERE username=?", (str(n1),))
                access = c.fetchone()[0]
                if any ([access == 2, access == 1]):
                    c.execute("UPDATE LoginTable SET loggedIn =? WHERE username = ?", ("1",str(n1),))
                    conn.commit()
                    openMain()
                elif access == 0:
                    openCustomerMain()
            else:
                message['text'] = "Invalid Credentials"

        if employeeLog == "FALSE":
            if count2 == 0:
                message['text'] = "No such username or password"
            elif count2 > 0:
                c.execute("SELECT clientPhoneNumber FROM CollectionTable WHERE clientName=?", (str(n1),))
                result2 = c.fetchone()[0]      
                if p1 == result2:
                    c.execute("SELECT collectionTitle FROM CollectionTable WHERE clientPhoneNumber=?", (str(p1),))
                    collTitle = c.fetchone()[0]
                    openDonorMain(collTitle)
                else:
                    message['text'] = "Invalid Credentials"

    def openMain():
            window_check.destroy()
            Main_UI.Warning_Window(conn)
            Main_UI.Main_Window(conn)

    #def openDonorMain(donorNum):
        #window_check.destroy()
        #Display_Guest_Samples.FetchGuestSamples(conn, donorNum) 

    def openCustomerMain():
        username = entry_name.get()
        window_check.destroy()
        ViewMode_UI.ViewFridges(conn, username) 
 
    def enterPress(event):
        checkCreds()

    def Cancel():
        window_check.destroy()

    name = Label(window_check, text = "Username", font = myFont, bg ='cadet blue')
    name.grid(row = 1, column = 1, sticky = E)

    password = Label(window_check, text = "Password", font = myFont, bg ='cadet blue')
    password.grid(row = 2, column = 1, sticky = E)

    entry_name = Entry(window_check)
    entry_name.grid(row = 1, column = 2)

    entry_pass = Entry(window_check, show = "*")
    entry_pass.grid(row = 2, column = 2)

    message.grid(row = 3, columnspan = 2)

    window_check.bind("<Return>", enterPress) #user can press enter instead of clicking Login

    checkButton = Button(window_check, text = "Login", command = checkCreds, height = 1, width = 8, font = myFont)
    checkButton.grid(row = 4, columnspan = 2, column = 1)

    cancelButton = Button(window_check, text = "Exit", command = Cancel, height = 1, width = 8, font = myFont)
    cancelButton.grid(row = 5, columnspan = 2, column = 1)

    empty1 = Label(window_check, height = 1, width = 2, bg ='cadet blue').grid(row = 0, column = 0)
    empty2 = Label(window_check, height = 1, width = 2, bg ='cadet blue').grid(row = 6, column = 3)
    
    window_check.mainloop()
