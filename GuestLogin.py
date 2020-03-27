from tkinter import *
import sqlite3
import Display_Guest_Samples

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

#***** MAIN WINDOW *****
#Currently bypasses TestUI_MAIN in favour of the drop down menu script
#works with TestUI_MAIN as well, but need to comment out the window instatiation
def LoginScreen():
    login_window = Tk()
    login_window.title("Login as Guest")
    
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
        Display_Guest_Samples.FetchGuestSamples(p1)  
    
    def enterPress(event):
        checkCreds()

    def Exit():
        login_window.destroy()


    name = Label(login_window, text = "Name")
    password = Label(login_window, text = "Cell Number")
    message = Label(login_window, text = "Enter name and cellphone number")
    entry_name = Entry(login_window)
    entry_pass = Entry(login_window, show = "*")

    loginButton = Button(login_window, text = "Login", command = checkCreds)
    quitButton = Button(login_window, text = "Exit", command = Exit)
    #check = Checkbutton(login_window, text = "Stay signed in")

    name.grid(row = 0, column = 0, sticky = E)
    password.grid(row = 1, column = 0, sticky = E)
    entry_name.grid(row = 0, column = 1)
    entry_pass.grid(row = 1, column = 1)
    message.grid(row = 2, columnspan = 2)
    #check.grid(row = 3, columnspan = 2)
    loginButton.grid(row = 4, columnspan = 2)
    quitButton.grid(row = 5, columnspan = 2)

    login_window.bind("<Return>", enterPress) #user can press enter instead of clicking Login
    
    login_window.mainloop()


#LoginScreen()
