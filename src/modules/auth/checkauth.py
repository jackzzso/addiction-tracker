import os

class checkAuth:
    @staticmethod
    def get() -> str:
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../.././auth/token')), 'r', encoding='utf-8') as file:
            return file.read()
        return "No authentication token."
        
    @staticmethod
    def isAuthed() -> bool:
        if checkAuth.get() == "":
            return False
        return True

if __name__ == "__main__":
    exit()
