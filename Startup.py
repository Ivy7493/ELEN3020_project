from tkinter import *
import sqlite3
import User_CredentialCheck, GuestLogin, Customer_UI


def Start_Window(conn):
    start_window = Tk()  
    #start_window.geometry("300x300")
    start_window.title("START")

    def Employee_Window():
        start_window.destroy()
        User_CredentialCheck.Check_Window(conn)

    def Guest_Window():
        start_window.destroy()
        GuestLogin.LoginScreen(conn)

    def Customer_Window():
        start_window.destroy()
        Customer_UI.ShowSampleTypes(conn)

    def Exit():
        start_window.destroy()

    employeeButton = Button(start_window, text = "Employee", command = Employee_Window, height = 1, width = 8)
    guestButton = Button(start_window, text = "    Donor   ", command = Guest_Window, height = 1, width = 8)
    customerButton = Button(start_window, text = "    Customer   ", command = Customer_Window, height = 1, width = 8)
    info = Label(start_window, text = "Please select Employee or Donor to go to login")
    exitButton = Button(start_window, text = "     Exit     ", command = Exit, height = 1, width = 8)

    info.grid(row = 0, column = 0)
    employeeButton.grid(row = 1, column = 0)
    guestButton.grid(row = 2, column = 0)
    customerButton.grid(row = 3, column = 0)
    exitButton.grid(row = 4, column = 0)

    start_window.mainloop()





