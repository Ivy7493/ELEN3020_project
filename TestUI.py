import SetupAPI
import sqlite3

conn = sqlite3.connect('Test.db')
conn.execute("PRAGMA foreign_keys = ON")
SetupAPI.CreateFridgeTable(conn)

