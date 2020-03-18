from tkinter import *
import TestUI_MAIN
import dropDownMenu

#***** MAIN WINDOW *****
#Currently bypasses TestUI_MAIN in favour of the drop down menu script
#works with TestUI_MAIN as well, but need to comment out the window instatiation
def LoginScreen():
    login_window = Tk()
    
    def checkCreds(): #checks the user's credentials
        n1 = entry_name.get()
        p1 = entry_pass.get()
        
        if n1 == "Test":
            if p1 == "Test":
                openMain()
        else:
            message['text'] = "Incorrect username or password"

    def openMain():
        login_window.destroy()
        dropDownMenu.Main_Window()  
    
    def enterPress(event):
        checkCreds()


    name = Label(login_window, text = "Name")
    password = Label(login_window, text = "Password")
    message = Label(login_window, text = "Enter name and password")
    entry_name = Entry(login_window)
    entry_pass = Entry(login_window, show = "*")

    loginButton = Button(login_window, text = "Login", command = checkCreds)
    quitButton = Button(login_window, text = "Exit", command = login_window.quit)
    check = Checkbutton(login_window, text = "Stay signed in")

    name.grid(row = 0, column = 0, sticky = E)
    password.grid(row = 1, column = 0, sticky = E)
    entry_name.grid(row = 0, column = 1)
    entry_pass.grid(row = 1, column = 1)
    message.grid(row = 2, columnspan = 2)
    check.grid(row = 3, columnspan = 2)
    loginButton.grid(row = 4, columnspan = 2)
    quitButton.grid(row = 5, columnspan = 2)

    login_window.bind("<Return>", enterPress) #user can press enter instead of clicking Login
    
    login_window.mainloop()


LoginScreen()
