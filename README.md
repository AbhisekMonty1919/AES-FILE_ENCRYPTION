🔐 AES-FileVault

A local file encryption-decryption system using AES-256 to securely store and retrieve sensitive files. It uses random key + IV generation, logs metadata, and ensures confidentiality through AES cryptography.


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


📁 Folder Structure

AES-FileVault/
├── main.py                  # CLI-based encryption/decryption
├── metadata.json            # Stores logs of all encrypted files
├── requirements.txt         # Required Python packages
├── README.md                # Project Documentation
├── test files/              # Place input files here
└── vaulted/                 # Encrypted/Decrypted output files


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Technologies Used

Python 3.12

cryptography library

AES-256 (CBC mode)

Random key & IV generation

SHA-256 hashing

JSON for metadata logging


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


🚀 Features

🔐 AES-256 Encryption

🧩 Random IV + Key for every file

📟 metadata.json tracks encryption history

✅ Integrity with SHA-256 hash

⟲ Easy file decryption using CLI


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


📦 Usage

▶ Encrypt a File

Put your file in test files/ folder

Run:

python main.py

Choose:

1. Encrypt a file

Input path like:

test files/mysecret.pdf

Get:

AES key

IV

Encrypted file inside vaulted/

Entry in metadata.json

🔓 Decrypt a File

Choose:

2. Decrypt a file

Then enter:

Path to .enc file

AES key (from encryption)

IV

Get:

Decrypted file saved with .decrypted.txt extension


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


🔍 metadata.json Explained

This file stores info like:

{
  "original": "testfile.webp",
  "encrypted": "testfile.webp.enc",
  "hash": "abc123...",
  "time": "2025-07-14T22:30:12",
  "key": "187e90ed...",
  "iv": "3e49fccb..."
}

So you don’t lose any record of what was encrypted.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


📆 requirements.txt

cryptography==42.0.5

Install using:

pip install -r requirements.txt


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


📚 Cryptography + Password Storage Insight

What Happens Under the Hood

Random Key Generation: 32 bytes for AES-256

Random IV Generation: 16 bytes (CBC mode)

File is broken into blocks of 16 bytes

AES encrypts each block using key + IV

Encrypted file saved in vaulted/

Key + IV are shown for decryption (user saves)

metadata.json stores all necessary info to log

How System Verifies Password

On decryption, input password is hashed

It matches the hash stored in system

If match, access granted; else denied


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


🌐 Modern Org Practice: Secure Random Password Hashing

Technique: PBKDF2 with AES & SHA256 (Industry Standard)

Steps:

Generate a secure random string (user password)

Create a salt (random bits for uniqueness)

Hash password using PBKDF2 + SHA256

Use hashed password as AES key

Encrypt data, save only encrypted file

Store salt + hash in protected password vault


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


👥 Author

Abhisek PandaCybersecurity InternAES-FileVault Project - Secure File Encryption & Storage

