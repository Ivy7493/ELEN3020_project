import SetupAPI
import sqlite3
import tkinter as tk
from tkinter.font import Font
from tkinter import ttk
from tkinter import messagebox
import DataAPI
import Main_UI

##########---------->START: MESSAGE POPUP<--------------------##########
def MessagePopup(messageText, messageTitle):
    message_window = tk.Tk()
    message_window.title(messageTitle)
    message_window["bg"] = 'cadet blue'

    text = tk.Text(message_window)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    message = tk.Label(message_window, text = messageText, font = myFont, bg = 'cadet blue')
    message.grid(row = 0, column = 0)

    def CloseMessage():
        message_window.destroy()

    backButton = tk.Button(message_window, text = 'Close', command = CloseMessage, font = myFont).grid(row=1)  
##########---------->END: MESSAGE POPUP<--------------------##########

##########---------->START: REGISTER CLIENT<--------------------##########
def RegisterClient_Window(conn):

    def AddCollection():
        _collectionTitle = newCollectionTitle.get()
        _username = newCollectionTitle.get()
        _password = password.get()
        _donorID = donorID.get()
        _clientName = clientName.get()
        _clientPhone = clientPhone.get()
        _clientEmail = clientEmail.get()
        _clientOrganization = clientOrganization.get()   
        _clientStreet = clientStreet.get()
        _clientCity = clientCity.get()
        _clientCountry = clientCountry.get()
        _clientPostalCode = clientPostalCode.get()

        if any( [_collectionTitle == "", _username =="", _password == "",  _donorID == "", _clientName == "", _clientPhone == "", _clientEmail == "", _clientOrganization == "", _clientStreet == "", _clientCity == "", _clientCountry == "", _clientPostalCode == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        else:
            messageText1 = DataAPI.AddCollection(conn, _collectionTitle, _donorID, _clientName, _clientPhone, _clientEmail, _clientOrganization, _clientStreet, _clientCity, _clientCountry, _clientPostalCode)
            MessagePopup(messageText1, "COLLECTION RECORD STATUS")

            messageText2 = DataAPI.AddUser(conn, _username, _password, "Customer")
            MessagePopup(messageText2, "COLLECTION USER STATUS")

    def Return():
        window_Collection.destroy()
        Main_UI.Edit_Window(conn)

    window_Collection = tk.Tk()
    window_Collection.title("COLLECTION")
    window_Collection["bg"] = 'cadet blue'

    text = tk.Text(window_Collection)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    label1 = tk.Label(window_Collection, text = "Collection Title", anchor = "w", bg = 'cadet blue', font = myFont)
    label1.grid(row = 1, column = 1,  sticky = "ew")
    newCollectionTitle = tk.Entry(window_Collection)
    newCollectionTitle.grid(row = 1, column = 2, sticky = "ew")

    label2 = tk.Label(window_Collection, text = "Donor ID", anchor = "w", bg = 'cadet blue', font = myFont)
    label2.grid(row = 2, column = 1,  sticky = "ew")
    donorID = tk.Entry(window_Collection)
    donorID.grid(row = 2, column = 2, sticky = "ew")

    label3 = tk.Label(window_Collection, text = "Client Name", anchor = "w", bg = 'cadet blue', font = myFont)
    label3.grid(row = 3,  column = 1, sticky = "ew")
    clientName = tk.Entry(window_Collection)
    clientName.grid(row = 3, column = 2, sticky = "ew")

    label4 = tk.Label(window_Collection, text = "Client Phone", anchor = "w", bg = 'cadet blue', font = myFont)
    label4.grid(row = 4,  column = 1, sticky = "ew")
    clientPhone = tk.Entry(window_Collection)
    clientPhone.grid(row = 4, column = 2, sticky = "ew")

    label5 = tk.Label(window_Collection, text = "Client Email", anchor = "w", bg = 'cadet blue', font = myFont)
    label5.grid(row = 5,  column = 1, sticky = "ew")
    clientEmail = tk.Entry(window_Collection)
    clientEmail.grid(row = 5, column = 2, sticky = "ew")

    label6 = tk.Label(window_Collection, text = "Client Organization", anchor = "w", bg = 'cadet blue', font = myFont)
    label6.grid(row = 6, column = 1, sticky = "ew")
    clientOrganization = tk.Entry(window_Collection)
    clientOrganization.grid(row = 6, column = 2, sticky = "ew")

    label7 = tk.Label(window_Collection, text = "Client Street", anchor = "w", bg = 'cadet blue', font = myFont)
    label7.grid(row = 7, column = 1, sticky = "ew")
    clientStreet = tk.Entry(window_Collection)
    clientStreet.grid(row = 7, column = 2, sticky = "ew")

    label8 = tk.Label(window_Collection, text = "Client City", anchor = "w", bg = 'cadet blue', font = myFont)
    label8.grid(row = 8, column = 1, sticky = "ew")
    clientCity = tk.Entry(window_Collection)
    clientCity.grid(row = 8, column = 2, sticky = "ew")

    label9 = tk.Label(window_Collection, text = "Client Country", anchor = "w", bg = 'cadet blue', font = myFont)
    label9.grid(row = 9, column = 1, sticky = "ew")
    clientCountry = tk.Entry(window_Collection)
    clientCountry.grid(row = 9, column = 2, sticky = "ew")

    label10 = tk.Label(window_Collection, text = "Client Postal Code", anchor = "w", bg = 'cadet blue', font = myFont)
    label10.grid(row = 10, column = 1, sticky = "ew")
    clientPostalCode = tk.Entry(window_Collection)
    clientPostalCode.grid(row = 10, column = 2, sticky = "ew")

    label12 = tk.Label(window_Collection, text = "Client Password", anchor = "w", bg = 'cadet blue', font = myFont)
    label12.grid(row = 12, column = 1, sticky = "ew")
    password = tk.Entry(window_Collection)
    password.grid(row = 12, column = 2, sticky = "ew")

    addButton = tk.Button(window_Collection, text = 'Add New Collection', command = AddCollection, font = myFont)
    addButton.grid(row = 13, column=2, sticky = "ew")

    returnButton = tk.Button(window_Collection, text = "Return", command = Return, font = myFont)
    returnButton.grid(row = 15, column = 2, sticky = "ew")

    tk.Label(window_Collection, height = 1, width = 2, bg ='cadet blue').grid(row = 0, column = 0)
    tk.Label(window_Collection, height = 1, width = 2, bg ='cadet blue').grid(row = 14, column = 3)
    tk.Label(window_Collection, height = 1, width = 2, bg ='cadet blue').grid(row = 16, column = 0)

    window_Collection.mainloop()
##########---------->END: REGISTER CLIENT<--------------------##########

##########---------->START: REGISTER USER<--------------------##########
def RegisterUser_Window(conn):
    def AddUser():
        _username = username.get()
        _password = password.get()
        _accessLevel = accessLevel.get()

        if any( [_username == "", _password == "", _accessLevel == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        else:
            try:
                messageText = DataAPI.AddUser(conn, _username, _password, _accessLevel)
                MessagePopup(messageText, "REGISTER STATUS")
            except:
                MessagePopup("ERROR: Invalid data entered", "REGISTER STATUS")

    def GetAccessLevel():
        return ["Employee", "Supervisor"]

    def Return():
        window_register.destroy()
        Manage_Window(conn)

    window_register = tk.Tk()
    window_register.title("ADD USER")
    window_register["bg"] = 'cadet blue'

    text = tk.Text(window_register)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    userLabel = tk.Label(window_register, text = "Username: ", anchor = "w", bg = 'cadet blue', font = myFont)
    userLabel.grid(row = 1, column = 1, sticky = "ew")
    username = tk.Entry(window_register)
    username.grid(row = 1, column = 2, sticky = "ew")

    passLabel = tk.Label(window_register, text = "Password: ", anchor = "w", bg = 'cadet blue', font = myFont)
    passLabel.grid(row = 2, column = 1, sticky = "ew")
    password = tk.Entry(window_register)
    password.grid(row = 2, column = 2, sticky = "ew")
    
    accessLabel = tk.Label(window_register, text = "Access Level: ", anchor = "w", bg = 'cadet blue', font = myFont)
    accessLabel.grid(row = 3, column = 1, sticky = "ew")
    accessLevel = ttk.Combobox(window_register, state="readonly", values=GetAccessLevel()) 
    accessLevel.grid(row = 3, column = 2, sticky = "ew")

    registerButton = tk.Button(window_register, text = "Register", command = AddUser, font = myFont)
    registerButton.grid(row = 4, column = 2, sticky = "ew")

    returnButton = tk.Button(window_register, text = "Return", command = Return, font = myFont)
    returnButton.grid(row = 6, column = 2, sticky = "ew")

    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 0, column = 0)
    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 5, column = 0)
    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 7, column = 3)

    window_register.mainloop()
##########---------->END: REGISTER USER<--------------------##########

##########---------->START: DELETE USER<--------------------##########
def DeleteUser_Window(conn):
    window_register = tk.Tk()
    window_register.title("DELETE USER")
    window_register["bg"] = 'cadet blue'

    text = tk.Text(window_register)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def RefreshUsernameList():
        usernameList = DataAPI.GetUsernames(conn)
        username['values'] = usernameList

    def DeleteUser():
        _username = username.get()

        if any( [_username == ""]):
            MessagePopup("One or more fields are missing data", "ERROR")
        else:
            message_window = tk.Tk()
            message_window.title("CONFIRM DELETION")
            message_window["bg"] = 'cadet blue'

            text = tk.Text(message_window)
            myFont = Font(family="fixedsys", size=12)
            text.configure(font=myFont)
            messageText = "Are you sure you want to delete user " + _username + "?"
            message = tk.Label(message_window, text = messageText, font = myFont, bg = 'cadet blue', wraplength = 200)
            message.grid(row = 1, column = 1)

            def CloseMessage():
                message_window.destroy()
            
            def Confirm():
                try:
                    messageText = DataAPI.DeleteUser(conn, _username)
                    RefreshUsernameList()
                    message_window.destroy()
                    MessagePopup(messageText, "DELETION STATUS")

                except:
                    message_window.destroy()
                    MessagePopup("ERROR: Invalid data entered", "DELETION STATUS")
            
            confirmButton = tk.Button(message_window, text = 'Yes', command = Confirm, font = myFont).grid(row=3, column=1, sticky = "ew")              
            cancelButton = tk.Button(message_window, text = 'No', command = CloseMessage, font = myFont).grid(row=5, column=1, sticky = "ew") 
             
            tk.Label(message_window, height = 1, width = 2, bg="cadet blue").grid(row=0, column=2)
            tk.Label(message_window, height = 1, width = 2, bg="cadet blue").grid(row=2, column=0)
            tk.Label(message_window, height = 1, width = 2, bg="cadet blue").grid(row=4, column=0)
            tk.Label(message_window, height = 1, width = 2, bg="cadet blue").grid(row=6, column=0)

    def Return():
        window_register.destroy()
        Manage_Window(conn)

    userLabel = tk.Label(window_register, text = "Username: ", anchor = "w", bg = 'cadet blue', font = myFont)
    userLabel.grid(row = 1, column = 1, sticky = "ew")

    usernameList = DataAPI.GetUsernames(conn)
    username = ttk.Combobox(window_register, state="readonly", values = usernameList)
    username.grid(row = 1, column = 2, sticky = "ew")

    deleteButton = tk.Button(window_register, text = "Delete User", command = DeleteUser, font = myFont)
    deleteButton.grid(row = 2, column = 2, sticky = "ew")

    returnButton = tk.Button(window_register, text = "Return", command = Return, font = myFont)
    returnButton.grid(row = 4, column = 2, sticky = "ew")

    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 0, column = 0)
    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 3, column = 0)
    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 5, column = 3)

    window_register.mainloop()
##########---------->END: DELETE USER<--------------------##########

##########---------->START: MANAGE USERS<--------------------##########
def Manage_Window(conn):
    window_register = tk.Tk()
    window_register.title("MANAGE USERS")
    window_register["bg"] = 'cadet blue'

    text = tk.Text(window_register)
    myFont = Font(family="fixedsys", size=12)
    text.configure(font=myFont)

    def AddUser():
        window_register.destroy()
        RegisterUser_Window(conn)

    def DeleteUser():
        window_register.destroy()
        DeleteUser_Window(conn)

    def Return():
        window_register.destroy()
        Main_UI.Edit_Window(conn)

    addUserButton = tk.Button(window_register, text = "Add User", command = AddUser, font = myFont)
    addUserButton.grid(row = 1, column = 2, sticky = "ew")

    deleteUserButton = tk.Button(window_register, text = "Delete User", command = DeleteUser, font = myFont)
    deleteUserButton.grid(row = 3, column = 2, sticky = "ew")

    returnButton = tk.Button(window_register, text = "Return", command = Return, font = myFont)
    returnButton.grid(row = 5, column = 2, sticky = "ew")

    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 0, column = 0)
    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 2, column = 0)
    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 4, column = 3)
    tk.Label(window_register, height = 1, width = 2, bg ='cadet blue').grid(row = 6, column = 3)

    window_register.mainloop()
##########---------->END: MANAGE USERS<--------------------##########
