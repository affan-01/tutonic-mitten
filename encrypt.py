#importing the library
from cryptography.fernet import Fernet

#generating the key
def encrypt_file(file):
    key = Fernet.generate_key()

    #writing the key to a file for storage for decryption
    with open('static/filekey','wb') as filekey:
        filekey.write(key)

    #open the key
    with open('static/filekey','rb') as filekey:
        key = filekey.read()

    f = Fernet(key)

    #opening the file that contains the plaintext
    with open(f"static/{file}",'rb') as file:
        original = file.read()

    #encrypting the file
    token = f.encrypt(original)

    #writing encrypted data to a file
    with open('static/ciphertext','wb') as ciphertext:
        ciphertext.write(token)




