import AutoBilling
import sqlite3
from datetime import datetime

conn = sqlite3.connect('Test.db')
now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

print("Monthly billing successfully ran at " + now)
AutoBilling.AutoBilling(conn)
conn.close()

