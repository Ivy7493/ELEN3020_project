from tkinter import *
import sqlite3
import Main_UI
import DataAPI
import SetupAPI

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")

SetupAPI.CreateAllTables(conn) 

DataAPI.LogoutAll(conn)

Main_UI.Main_Window()


