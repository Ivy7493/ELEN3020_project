from datetime import datetime
import sqlite3

mainLog = 'Logs/MainLog.txt'
billingLog = 'Logs/BillingLog.txt'

def Log(conn, _logInfo):
    f = open(mainLog,"a")
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    logMes = now + " - " + " user: " + GetCurrentLogin(conn) + " "  + _logInfo + '\n'
    f.write(logMes)
    f.close()

def IndividualLog(conn, _logInfo, _fileName):
    fullName = 'Logs/'+_fileName + '.txt'
    f = open(fullName,"a")
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    logMes = now + " - " + " user: " + GetCurrentLogin(conn) + " " + _logInfo + '\n'
    f.write(logMes)
    f.close()

def BillingLog(conn, _logInfo):
    f = open(billingLog,"a")
    now = datetime.now()
    now = now.strftime("%Y-%m-%d %H:%M:%S")
    logMes = now + " - " + _logInfo + '\n'
    f.write(logMes)
    f.close()

def GetCurrentLogin(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM LoginTable WHERE loggedIn=?",("1",))
    result = c.fetchone()
    return result[0]

def GetCurrentAccess(conn):
    c = conn.cursor()
    c.execute("SELECT * FROM LoginTable WHERE loggedIn=?",("1",))
    result = c.fetchone()
    return result[2]
    

    

    
    
