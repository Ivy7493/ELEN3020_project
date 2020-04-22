import sqlite3
import User_CredentialCheck, SetupAPI, DataAPI

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

SetupAPI.CreateAllTables(conn) 
DataAPI.LogoutAll(conn)

User_CredentialCheck.Check_Window(conn)
