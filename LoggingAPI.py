from datetime import datetime


mainlog = 'Logs/Mainlog.txt'

def Log(LogInfo):
    f = open(mainlog,"a")
    now = datetime.now()
    now = now.strftime("%Y-%M-%D %H:%M:%S")
    logMes = now + " - " + LogInfo + '\n'
    f.write(logMes)
    f.close()


def IndividualLog(_logInfo, _fileName):
    fullName = 'Logs/'+_fileName + '.txt'
    f = open(fullName,"a")
    now = datetime.now()
    now = now.strftime("%Y-%M-%D %H:%M:%S")
    logMes = now + " - " + _logInfo + '\n'
    f.write(logMes)
    f.close()
    
