import os
import time
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

debug = False

path = os.path.abspath(os.path.join(os.path.dirname(__file__), './../../../config/key.json'))
cred = credentials.Certificate(path)

class getDB:
    @staticmethod
    def VERIFYLOGIN(USERNAME: str, HASH: str, PASSKEY: str) -> str:
        ref = db.reference(f'/')
        data = ref.get()
        for i in data:
            userref = db.reference(f'/{i}/USERNAME').get()
            hashref = db.reference(f'/{i}/HASH').get()
            if userref == USERNAME:
                try:
                    verified = PasswordHasher().verify(hashref, PASSKEY)
                    if verified:
                        return db.reference(f'/{i}/TOKEN').get()
                    else:
                        return False
                except VerifyMismatchError:
                    if debug == False:
                        return False
                    os.system('cls')
                    print("Password verification failed: incorrect password.")
                    input()
                except Exception as e:
                    if debug == False:
                        return False
                    os.system('cls')
                    print(f"An error occurred: {e}")       
                    input()
        return False
        
    @staticmethod
    def CHECKUSER(USERNAME: str) -> str:
        ref = db.reference(f'/')
        data = ref.get()
        for i in data:
            userref = db.reference(f'/{i}/USERNAME').get()
            if userref == USERNAME:
                return False
        return True
        
    @staticmethod
    def UUID(TOKEN: str) -> str:
        ref = db.reference(f'/')
        data = ref.get()
        for i in data:
            ref = db.reference(f'/{i}/TOKEN')
            contents = ref.get()
            if contents == TOKEN:
                return i
        return
 
    @staticmethod
    def USERNAME(UUID: str) -> str:
        ref = db.reference(f'/{UUID}/USERNAME')
        data = ref.get()
        return data
        
    @staticmethod
    def HASH(UUID: str) -> str:
        ref = db.reference(f'/{UUID}/HASH')
        data = ref.get()
        return data
        
    @staticmethod   
    def TOKEN(UUID: str) -> str:
        ref = db.reference(f'/{UUID}/TOKEN')
        data = ref.get()
        return data
        
    @staticmethod
    def TIMESTAMP(UUID: str) -> str:
        ref = db.reference(f'/{UUID}/TIMESTAMP')
        data = ref.get()
        return data
        
    @staticmethod
    def ACCTYPE(UUID: str) -> str:
        ref = db.reference(f'/{UUID}/ACCTYPE')
        data = ref.get()
        return data
    
if __name__ == "__main__":
    exit()
