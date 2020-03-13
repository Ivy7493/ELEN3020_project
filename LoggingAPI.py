from datetime import datetime


mainlog = 'Logs/Mainlog.txt'

def Log(LogInfo):
    f = open(mainlog,"a")
    now = datetime.now()
    now = now.strftime("%Y-%M-%D %H:%M:%S")
    logmes = now + " - " + LogInfo + '\n'
    f.write(logmes)
    f.close()
