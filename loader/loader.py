import sys
import os
import subprocess

modulePath = os.path.abspath(os.path.join(os.path.dirname(__file__), './../src'))
sys.path.append(modulePath)

from modules.auth.checkauth import checkAuth
from modules.db.dbhandler.get import getDB

os.system("title ")

def main():
    TOKEN = "checkAuth.get()"
    if checkAuth.isAuthed():
        subprocess.run(["python", os.path.abspath(os.path.join(os.path.dirname(__file__), './../src/core/main.py'))])
        return
    subprocess.run(["python", os.path.abspath(os.path.join(os.path.dirname(__file__), './../src/core/login.py'))])
    return

if __name__ == "__main__":
    main()
