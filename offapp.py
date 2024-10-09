import subprocess
from difflib import get_close_matches as find
import pyttsx3
from os import system

v = pyttsx3.init()

program=[]
progid=[]
progdict={}
cmd='powershell "gps |where mainwindowtitle |select Description'
cmd1='powershell "gps |where mainwindowtitle |select id'

proc=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
proc1=subprocess.Popen(cmd1,shell=True,stdout=subprocess.PIPE)

for line in proc.stdout:
    st=str(line.decode().rstrip())
    program.append(st)

for line in proc1.stdout:
    st=str(line.decode().rstrip())
    progid.append(st)


for i in range(0,len(progid)):
    progdict[program[i]]=progid[i]


def close(c):
    global program,progid,progdict
    q=find(c,program)
    if q==[]:
        v.say("app is not found to close")
        v.runAndWait()
    else:
        for key,value in progdict.items():
            if key==q[0]:
                v.say(f"{key} is closing")
                v.runAndWait()
                system("taskkill /im  "+ str(value))



