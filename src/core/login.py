import sys
import os
import uuid
import secrets
import time
import subprocess
import json

modulePath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../modules'))
print(modulePath)
sys.path.append(modulePath)

from auth.checkauth import checkAuth
from auth.setauth import setAuth
from db.dbhandler.get import getDB
from db.dbhandler.post import postDB
from db.argon2.hasher import argonhasher
from other.log import log

os.system("title ")

opengui = "login"

guis = {
    "login": "guiLogin",
    "setup": "guiSetup",
}

inputtxt = "   >"

# asciiart.eu/text-to-ascii-art
# use font 'Pagga'

loginorsignuptxt = """
░█▀░░▀█░░▀█░░░░█▀▀░▀█▀░█▀▀░█▀█░█░█░█▀█
░█░░░░█░░░█░░░░▀▀█░░█░░█░█░█░█░█░█░█▀▀
░▀▀░░▀▀▀░▀▀░░░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░░
░█▀░░▀▀▄░▀█░░░░█░░░█▀█░█▀▀░░░░░▀█▀░█▀█
░█░░░▄▀░░░█░░░░█░░░█░█░█░█░▄▄▄░░█░░█░█
░▀▀░░▀▀▀░▀▀░░░░▀▀▀░▀▀▀░▀▀▀░░░░░▀▀▀░▀░▀
"""

usernametxt = """
░█░█░█▀▀░█▀▀░█▀▄░█▀█░█▀█░█▄█░█▀▀
░█░█░▀▀█░█▀▀░█▀▄░█░█░█▀█░█░█░█▀▀
░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀░▀░▀▀▀
"""
passwordtxt = """
░█▀█░█▀█░█▀▀░█▀▀░█░█░█▀█░█▀▄░█▀▄
░█▀▀░█▀█░▀▀█░▀▀█░█▄█░█░█░█▀▄░█░█
░▀░░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀▀░
"""

def guiLogin():
    global username
    global hash
    global token
    global genuuid

    print(loginorsignuptxt)
    choice = input(f"{inputtxt} ")
    os.system('cls')

    if choice == "1":
        print(usernametxt)
        username = input(f"{inputtxt} ")
        isUsernameAvailable = getDB.CHECKUSER(username)
        if not isUsernameAvailable:
            subprocess.run(["python", os.path.abspath(os.path.join(os.path.dirname(__file__), './login.py'))])
            return
        os.system('cls')

        print(passwordtxt)
        passkey = input(f"{inputtxt} ")
        os.system('cls')
        
    elif choice == "2":
        print(usernametxt)
        inp = input(f"{inputtxt} ")
        os.system('cls')

        print(passwordtxt)
        passkey = input(f"{inputtxt} ")
        os.system('cls')

        username = str(inp)
        hash = str(argonhasher.encrypt(passkey))
        check = getDB.VERIFYLOGIN(username, hash, passkey)
        if not check:
            os.system('cls')
            main()
            return
        setAuth.set(check)

        subprocess.run(["python", os.path.abspath(os.path.join(os.path.dirname(__file__), './main.py'))])
        return
    else:
        log.error(f"'{choice}' is not a valid input.")
        input()
        exit()

    hash = argonhasher.encrypt(passkey)
    token = secrets.token_hex(32)
    genuuid = uuid.uuid4()

    setAuth.set(token)
    global opengui
    opengui = "setup"
    main()

def guiSetup():
    global acctype
    global timestamp

    accsetuptxt = """
    ░█▀█░█▀▀░█▀▀░█▀█░█░█░█▀█░▀█▀░░░█▀▀░█▀▀░▀█▀░█░█░█▀█
    ░█▀█░█░░░█░░░█░█░█░█░█░█░░█░░░░▀▀█░█▀▀░░█░░█░█░█▀▀
    ░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀░░▀░░░░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░░
        What addiction are you trying to quit?     
    """

    print(accsetuptxt)
    acctype = input(f"{inputtxt} ")
    os.system('cls')

    timestamp = int(time.time())
    
    finalize()

def finalize():
    data = {
        str(genuuid): {
            'USERNAME': str(username),
            'HASH': str(hash),
            'TOKEN': str(token),
            'ACCTYPE': str(acctype),
            'TIMESTAMP': str(timestamp)
        }
    }

    postDB.post(data)

    subprocess.run(["python", os.path.abspath(os.path.join(os.path.dirname(__file__), './main.py'))])
    return

def main():
    os.system('cls')
    gui = guis.get(opengui)
    globals()[gui]()
    return

if __name__ == "__main__":
    main()
