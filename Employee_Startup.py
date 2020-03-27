from tkinter import *
import sqlite3
import User_CredentialCheck
import DataAPI
import SetupAPI

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

SetupAPI.CreateAllTables(conn) 

DataAPI.LogoutAll(conn)

User_CredentialCheck.Check_Window()


