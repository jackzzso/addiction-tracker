import os
import time
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

path = os.path.abspath(os.path.join(os.path.dirname(__file__), './../../../config/key.json'))
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred, {
    'databaseURL': '' # Add in a Firebase Real-Time Database URL.
})

class postDB:
    @staticmethod
    def post(data):
        ref = db.reference("")
        ref.update(data)
        return
    
    @staticmethod
    def edit(uuid, timestamp):
        tsref = db.reference(f'/{uuid}/TIMESTAMP')
        tsref.set(str(timestamp))
        return

if __name__ == "__main__":
    exit()
    pass
