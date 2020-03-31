from tkinter import *
import sqlite3
import Box_UI
import Fridge_UI
import Sample_UI
import Main_UI
import Startup

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

def Check_Window():
    window_check = Tk()


    def checkCreds(): #checks the user's credentials
        n1 = entry_name.get()
        p1 = entry_pass.get()
        c = conn.cursor()
        c.execute("SELECT password FROM LoginTable WHERE username=?", (str(n1),))
        temp_result = c.fetchone()
        try:
            result = temp_result[0]
            if p1 == result:
                c.execute("UPDATE LoginTable SET loggedIn =? WHERE username = ?", ("1",str(n1),))
                conn.commit()
                openMain()
            else:
                message['text'] = "Invalid Credentials"
        except:
            message['text'] = "Invalid Credentials"

    def openMain():
            window_check.destroy()
            Main_UI.Main_Window()
          
    
    def enterPress(event):
        checkCreds()

    def Cancel():
        window_check.destroy()
        Startup.Start_Window()

    name = Label(window_check, text = "Username")
    password = Label(window_check, text = "Password")
    message = Label(window_check, text = "Enter username and password")
    entry_name = Entry(window_check)
    entry_pass = Entry(window_check, show = "*")

    checkButton = Button(window_check, text = "Validate", command = checkCreds)
    cancelButton = Button(window_check, text = "Cancel", command = Cancel)

    name.grid(row = 0, column = 0, sticky = E)
    password.grid(row = 1, column = 0, sticky = E)
    entry_name.grid(row = 0, column = 1)
    entry_pass.grid(row = 1, column = 1)
    message.grid(row = 2, columnspan = 2)
    checkButton.grid(row = 4, columnspan = 2)
    cancelButton.grid(row = 5, columnspan = 2)

    window_check.bind("<Return>", enterPress) #user can press enter instead of clicking Login
    
    window_check.mainloop()
