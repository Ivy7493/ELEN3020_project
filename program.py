import sqlite3
import Startup, SetupAPI, DataAPI

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

SetupAPI.CreateAllTables(conn) 
DataAPI.LogoutAll(conn)

Startup.Start_Window(conn)
