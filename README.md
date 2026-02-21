# End-To-End-Message-Encryption-Project
A real-time messaging application built with Python and FastAPI that implements secure user authentication and encrypted message storage using End-to-End Encryption (E2EE).
This project demonstrates how to build a secure backend system with JWT authentication, password hashing, WebSocket-based real-time communication, and AES-based message encryption.

# Features

User Registration & Login (JWT Authentication)

Password Hashing with bcrypt

Role-Based Access Control

Real-Time Messaging using WebSockets

Encrypted Message Storage (AES/Fernet)

SQLAlchemy ORM Integration

SQLite / PostgreSQL Database Support

# Security Highlights

Passwords are never stored in plain text

Protected routes using JWT tokens

Messages encrypted before saving to the database

Only authorized users can access chat functionality
