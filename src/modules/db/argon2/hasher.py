from argon2 import PasswordHasher

class argonhasher:
    @staticmethod
    def encrypt(PASSWORD: str) -> str:
        PASSKEY = PasswordHasher().hash(PASSWORD)
        return PASSKEY

if __name__ == "__main__":
    exit()
