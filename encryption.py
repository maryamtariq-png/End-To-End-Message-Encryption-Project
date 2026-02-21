import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

SECRET_KEY = os.getenv("MESSAGE_ENCRYPTION_KEY")

if not SECRET_KEY:
    raise ValueError("MESSAGE_ENCRYPTION_KEY not found in .env file!")

cipher = Fernet(SECRET_KEY)

def encrypt_message(message: str) -> str:
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message: str) -> str:
    return cipher.decrypt(encrypted_message.encode()).decode()