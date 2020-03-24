from datetime import datetime
import sqlite3
#JESSE'S COMMENT

mainlog = 'Logs/Mainlog.txt'

def Log(LogInfo):
    f = open(mainlog,"a")
    now = datetime.now()
    now = now.strftime("%Y-%M-%D %H:%M:%S")
    logMes = now + " - " + " user: " + GetCurrentLogin() + " "  + LogInfo + '\n'
    f.write(logMes)
    f.close()


def IndividualLog(_logInfo, _fileName):
    fullName = 'Logs/'+_fileName + '.txt'
    f = open(fullName,"a")
    now = datetime.now()
    now = now.strftime("%Y-%M-%D %H:%M:%S")
    logMes = now + " - " + " user: " + GetCurrentLogin() + " " + _logInfo + '\n'
    f.write(logMes)
    f.close()

def GetCurrentLogin():
    conn = sqlite3.connect("Test.db") #check database reference later if we change
    c = conn.cursor()
    c.execute("SELECT * FROM LoginTable WHERE loggedIn=?",("1",))
    result = c.fetchone()
    conn.close()
    return result[0]
    

    

    
    
