import os
from datetime import datetime
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import hashlib
import json

# === Configuration ===
VAULT_DIR = "vaulted"
META_FILE = "metadata.json"

# === Utility ===
def pad_data(data):
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()

def unpad_data(padded_data):
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded_data) + unpadder.finalize()

def hash_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

# === Encryption ===
def encrypt_file(input_file):
    if not os.path.exists(input_file):
        print("❌ File not found! Check the path.")
        return

    key = os.urandom(32)
    iv = os.urandom(16)

    with open(input_file, 'rb') as f:
        original_data = f.read()

    padded_data = pad_data(original_data)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    os.makedirs(VAULT_DIR, exist_ok=True)
    output_filename = os.path.basename(input_file) + ".enc"
    output_path = os.path.join(VAULT_DIR, output_filename)

    with open(output_path, 'wb') as f:
        f.write(iv + ciphertext)

    file_hash = hash_file(input_file)
    timestamp = datetime.now().isoformat()

    metadata_entry = {
        "original": os.path.basename(input_file),
        "encrypted": output_filename,
        "hash": file_hash,
        "time": timestamp,
        "key": key.hex(),
        "iv": iv.hex()
    }

    if os.path.exists(META_FILE):
        with open(META_FILE, 'r') as f:
            metadata = json.load(f)
    else:
        metadata = []

    metadata.append(metadata_entry)

    with open(META_FILE, 'w') as f:
        json.dump(metadata, f, indent=4)

    print("\n✅ File encrypted successfully!")
    print(f"🔐 Key (save securely): {key.hex()}")
    print(f"🧩 IV: {iv.hex()}")
    print(f"📁 Saved as: {output_path}\n")

# === Decryption ===
def decrypt_file(enc_path, key_hex, iv_hex):
    if not os.path.exists(enc_path):
        print("❌ Encrypted file not found!")
        return

    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)

    with open(enc_path, 'rb') as f:
        data = f.read()

    ciphertext = data[16:]  # skip IV (already passed)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    try:
        plaintext = unpad_data(padded_plaintext)
    except Exception as e:
        print("❌ Unpadding failed. Possibly wrong key or IV.")
        return

    output_file = enc_path.replace(".enc", ".decrypted.txt")

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"\n🔓 Decryption complete. File saved as: {output_file}\n")

# === CLI ===
if __name__ == "__main__":
    while True:
        print("=== AES FileVault ===")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Choose (1/2/3): ")

        if choice == '1':
            path = input("Enter path of file to encrypt (e.g., testfiles/secret.txt): ")
            encrypt_file(path)
        elif choice == '2':
            enc_file = input("Enter encrypted file path (e.g., vaulted/secret.txt.enc): ")
            key = input("Enter AES key (hex): ")
            iv = input("Enter IV (hex): ")
            decrypt_file(enc_file, key, iv)
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice\n")
