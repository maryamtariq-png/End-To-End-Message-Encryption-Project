# End-To-End-Message-Encryption-Project:
A real-time messaging application built with Python and FastAPI that implements secure user authentication and encrypted message storage using End-to-End Encryption (E2EE).
This project demonstrates how to build a secure backend system with JWT authentication, password hashing, WebSocket-based real-time communication, and AES-based message encryption.

# Features:

User Registration & Login (JWT Authentication)

Password Hashing with bcrypt

Role-Based Access Control

Real-Time Messaging using WebSockets

Encrypted Message Storage (AES/Fernet)

SQLAlchemy ORM Integration

SQLite / PostgreSQL Database Support

# Security Highlights:

Passwords are never stored in plain text

Protected routes using JWT tokens

Messages encrypted before saving to the database

Only authorized users can access chat functionality

# How to run:

Clone the repo: git clone https://github.com/hasan-65-db/SpendWisely-API.git

Install dependencies: pip install -r requirements.txt 

Run the server: uvicorn main:app --reload

# Usage Notes:

Database: The system automatically creates a chat.db SQLite file upon startup.

Interactive Docs: Once the server is running, go to http://127.0.0.1:8000/docs to test registration, login, and encrypted messaging.

E2EE Logic: Message content is encrypted using Fernet (AES) before being stored in the database.
