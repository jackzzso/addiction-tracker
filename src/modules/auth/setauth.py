import os

class setAuth:
    @staticmethod
    def set(TOKEN: str):
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../.././auth/token')), "w") as file:
            file.write(TOKEN)
        return
        
    @staticmethod
    def clear():
        with open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../.././auth/token')), "w") as file:
            file.write("")
        return

if __name__ == "__main__":
    exit()
