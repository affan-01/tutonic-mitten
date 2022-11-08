#importing the library
from cryptography.fernet import Fernet

#generating the key
key = Fernet.generate_key()

#writing the key to a file for storage for decryption
with open('filekey','wb') as filekey:
    filekey.write(key)

#open the key
with open('filekey','rb') as filekey:
    key = filekey.read()

f = Fernet(key)

#opening the file that contains the plaintext
with open('plaintext','rb') as plaintext:
    original = plaintext.read()

#encrypting the file
token = f.encrypt(original)

#writing encrypted data to a file
with open('ciphertext','wb') as ciphertext:
    ciphertext.write(token)




