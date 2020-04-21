from datetime import datetime
import sqlite3
#JESSE'S COMMENT

mainlog = 'Logs/Mainlog.txt'

def Log(conn, LogInfo):
    f = open(mainlog,"a")
    now = datetime.now()
    now = now.strftime("%Y-%M-%D %H:%M:%S")
    logMes = now + " - " + " user: " + GetCurrentLogin(conn) + " "  + LogInfo + '\n'
    f.write(logMes)
    f.close()


def IndividualLog(conn, _logInfo, _fileName):
    fullName = 'Logs/'+_fileName + '.txt'
    f = open(fullName,"a")
    now = datetime.now()
    now = now.strftime("%Y-%M-%D %H:%M:%S")
    logMes = now + " - " + " user: " + GetCurrentLogin(conn) + " " + _logInfo + '\n'
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
    

    

    
    
