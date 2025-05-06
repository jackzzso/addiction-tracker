import sys
import os
import time
import subprocess
from inputimeout import inputimeout, TimeoutOccurred

modulePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules'))
print(modulePath)
sys.path.append(modulePath)

from auth.checkauth import checkAuth
from auth.setauth import setAuth
from db.dbhandler.get import getDB
from db.dbhandler.post import postDB
from other.log import log

os.system("title ")

opengui = "main"

guis = {
    "main": "guiMain",
}

num1 = """░▀█░
░░█░
░▀▀▀"""
num2 = """░▀▀▄
░▄▀░
░▀▀▀"""
num3 = """░▀▀█
░░▀▄
░▀▀░"""
num4 = """░█░█
░░▀█
░░░▀"""
num5 = """░█▀▀
░▀▀▄
░▀▀░"""
num6 = """░▄▀▀
░█▀▄
░░▀░"""
num7 = """░▀▀█
░▄▀░
░▀░░"""
num8 = """░▄▀▄
░▄▀▄
░░▀░"""
num9 = """░▄▀▄
░░▀█
░▀▀░"""
num0 = """░▄▀▄
░█/█
░░▀░"""
colon = """░░░░
░░▀░
░░▀░"""

mainmenuui1 = """░█░█░░░░░█▀▄░█▀▄░█▀▄░░░░░█░█░█░█░░░░░█▄█░█▄█░░░░░█▀▀░█▀▀
░░█░░░▀░░█░█░█░█░█░█░░▀░░█▀█░█▀█░░▀░░█░█░█░█░░▀░░▀▀█░▀▀█
░░▀░░░▀░░▀▀░░▀▀░░▀▀░░░▀░░▀░▀░▀░▀░░▀░░▀░▀░▀░▀░░▀░░▀▀▀░▀▀▀"""

mainmenuui2 = """░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░█▀░░▀█░░▀█░░░░█▀▄░█▀▀░█▀▀░█▀▄░█▀▀░█▀▀░█░█░░░░░░░░░░░░░░
░█░░░░█░░░█░░░░█▀▄░█▀▀░█▀▀░█▀▄░█▀▀░▀▀█░█▀█░░░░░░░░░░░░░░
░▀▀░░▀▀▀░▀▀░░░░▀░▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░░░░░░░░░░░░░░
░█▀░░▀▀▄░▀█░░░░█▀▄░█▀▀░█▀▀░▀█▀░█▀█░█▀▄░▀█▀░░░░░░░░░░░░░░
░█░░░▄▀░░░█░░░░█▀▄░█▀▀░▀▀█░░█░░█▀█░█▀▄░░█░░░░░░░░░░░░░░░
░▀▀░░▀▀▀░▀▀░░░░▀░▀░▀▀▀░▀▀▀░░▀░░▀░▀░▀░▀░░▀░░░░░░░░░░░░░░░
░█▀░░▀▀█░▀█░░░░█░░░█▀█░█▀▀░░░░░█▀█░█░█░▀█▀░░░░░░░░░░░░░░
░█░░░░▀▄░░█░░░░█░░░█░█░█░█░▄▄▄░█░█░█░█░░█░░░░░░░░░░░░░░░
░▀▀░░▀▀░░▀▀░░░░▀▀▀░▀▀▀░▀▀▀░░░░░▀▀▀░▀▀▀░░▀░░░░░░░░░░░░░░░"""

def align(*p):
    l = [x.split('\n') for x in p]
    return '\n'.join(''.join(l[j][i] for j in range(len(l))) for i in range(len(l[0])))

timestamp = int(getDB.TIMESTAMP(getDB.UUID(checkAuth.get())))
auth = checkAuth.get()
uuid = getDB.UUID(auth)

def getclockstr():
    s = int(time.time() - timestamp)
    y = s // 31536000
    d = (s % 31536000) // 86400
    h = (s % 86400) // 3600
    m = (s % 3600) // 60
    s = s % 60
    return f'{y:01}:{d:03}:{h:02}:{m:02}:{s:02}'

nums = {
    '0': num0, '1': num1, '2': num2, '3': num3, '4': num4,
    '5': num5, '6': num6, '7': num7, '8': num8, '9': num9, ':': colon
}

def uimain():
    global timestamp
    global uuid
    timestamp = int(getDB.TIMESTAMP(uuid))

    clockstr = getclockstr()
    clock = align(*(nums[c] for c in clockstr))
    
    print(mainmenuui1)
    print(clock)
    print(mainmenuui2)
    
    inputtxt = "   >"
    
    try:
        ch = inputimeout(prompt=f"{inputtxt} ", timeout=3)
    except TimeoutOccurred:
        os.system('cls')
        uimain()
        return
    
    os.system('cls')
    
    if ch == "1":
        uimain()
        return

    elif ch == "2":
        timestamp = int(time.time())

        if uuid:
            postDB.edit(uuid, timestamp)
            
            uimain()
            return

    elif ch == "3":
        setAuth.clear()
        subprocess.run(["python", os.path.abspath(os.path.join(os.path.dirname(__file__), './login.py'))])
        return

    else:
        uimain()
        return

def guiMain():
    uimain()

def main():
    os.system('cls')
    gui = guis.get(opengui)
    globals()[gui]()
    return

if __name__ == "__main__":
    main()
