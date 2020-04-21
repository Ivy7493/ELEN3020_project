from tkinter import *
from tkinter.font import Font
import tkinter as tk
import sqlite3
import Display_Guest_Samples
import Startup


#***** MAIN WINDOW *****
#Currently bypasses TestUI_MAIN in favour of the drop down menu script
#works with TestUI_MAIN as well, but need to comment out the window instatiation
def LoginScreen(conn):
    login_window = Tk()
    login_window.title("Donor Login")
    login_window["bg"]='cadet blue'
    
    text = tk.Text(login_window)
    myFont = Font(family = "fixedsys", size=12)
    text.configure(font=myFont)

    
    def checkCreds(): #checks the user's credentials
        n1 = entry_name.get()
        p1 = entry_pass.get()
        
        c = conn.cursor()
        c.execute("SELECT collectionTitle FROM CollectionTable WHERE donorPhoneNumber=?", (str(p1),))
        temp_result = c.fetchall()
        count = 0

        for result in temp_result:
            count = count + 1
        if count == 0:
            message['text'] = "No such name or phone number"
        elif count > 0:
            c.execute("SELECT collectionTitle FROM CollectionTable WHERE donorPhoneNumber=?", (str(p1),))
            result = c.fetchone()[0]
            openMain(result)

    def openMain(p1):
        login_window.destroy()
        Display_Guest_Samples.FetchGuestSamples(conn, p1)  
    
    def enterPress(event):
        checkCreds()

    def Exit():
        login_window.destroy()
        Startup.Start_Window(conn)


    name = Label(login_window, text = "Name", font = myFont, bg ='cadet blue')
    password = Label(login_window, text = "Cell Number", font = myFont, bg ='cadet blue')
    message = Label(login_window, text = "Enter name and cellphone number", font = myFont, bg ='cadet blue')
    entry_name = Entry(login_window)
    entry_pass = Entry(login_window, show = "*")

    loginButton = Button(login_window, text = "Login", command = checkCreds, font = myFont)
    quitButton = Button(login_window, text = "Cancel", command = Exit, font = myFont)
    #check = Checkbutton(login_window, text = "Stay signed in")

    name.grid(row = 0, column = 0, sticky ="ew")
    password.grid(row = 1, column = 0, sticky = "ew")
    entry_name.grid(row = 0, column = 1)
    entry_pass.grid(row = 1, column = 1)
    message.grid(row = 2, columnspan = 2)
    loginButton.grid(row = 4, columnspan = 2)
    quitButton.grid(row = 5, columnspan = 2)

    login_window.bind("<Return>", enterPress) #user can press enter instead of clicking Login
    
    login_window.mainloop()

