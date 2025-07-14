# 🔐 AES-FileVault

A local file encryption-decryption system built using AES-256 to securely store and retrieve sensitive files. It features random key and IV generation, metadata logging, and strong confidentiality via AES cryptography.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📁 Folder Structure

AES-FileVault/
├── main.py              
├── metadata.json        
├── requirements.txt     
├── README.md            
├── test files/         
└── vaulted/            

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 


## ⚙️ Technologies Used

Python 3.12

cryptography library

AES-256 encryption in CBC mode

Secure random key and IV generation

SHA-256 hashing

JSON for metadata logging


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Features

AES-256 strong file encryption

Unique random IV and key for every file

Tracks encryption history using metadata.json

Verifies integrity with SHA-256

Simple and interactive CLI for usage

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📦 Usage

### ▶ Encrypt a File

Place the file to encrypt in the test files/ folder

Run the program:

python main.py

Choose option 1. Encrypt a file

Enter the file path, e.g.,

test files/mysecret.pdf

Output includes:

AES key and IV (displayed to user)

Encrypted file saved in vaulted/

A new entry logged in metadata.json


### 🔓 Decrypt a File

Choose option 2. Decrypt a file

Enter:

Path to encrypted .enc file

AES key

IV

Output:

Decrypted file saved with .decrypted.txt extension inside vaulted/


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔍 metadata.json Explained

This file logs each encryption operation:

{
  "original": "testfile.webp",
  "encrypted": "testfile.webp.enc",
  "hash": "abc123...",
  "time": "2025-07-14T22:30:12",
  "key": "187e90ed...",
  "iv": "3e49fccb..."
}

This ensures traceability and auditability.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📆 requirements.txt

cryptography==42.0.5

Install dependencies using:

pip install -r requirements.txt

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🔐 How It Works Internally

### 🔄 Encryption Flow

Random Key Generation: 32-byte key for AES-256

IV Generation: 16-byte random initialization vector

File Block Division: Split file into 16-byte blocks

AES Encryption: Each block encrypted using key + IV

Encrypted Output: File saved in vaulted/

Key + IV: Displayed to user for secure storage

Logging: Metadata saved to metadata.json




### 🔑 Password Verification Mechanism

During decryption, entered password is hashed

System compares it with stored hash

If hashes match, access is granted

Else, access is denied


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🌐 Secure Random Password Hashing Technique

🔐 Modern Industry Standard: PBKDF2 + AES + SHA-256

Step-by-step Process:

User creates a secure password (random string)

Generate a unique salt value

Use PBKDF2 with SHA-256 to hash password + salt

Derive AES key from the hash output

Encrypt file data using AES and store securely

Save salt and hash securely in password vault (not the key)

This protects against brute-force attacks and rainbow tables.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🧠 Quick Recap

AES-256 encrypts data using secure keys & IVs

Files are split into 16-byte blocks and encrypted

Random key + IV generated per session

Passwords hashed and verified (not stored as plain text)

All logs written to metadata.json

Uses secure PBKDF2 hashing technique for deriving AES keys

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 👨‍💻 Author

Abhisek PandaCybersecurity InternAES-FileVault Project – Secure File Encryption & Storage
