#importing the library
from cryptography.fernet import Fernet

#opening the file which has the key
with open('filekey','rb') as filekey:
    key = filekey.read()

#using the key
f = Fernet(key)

#reading the ciphertext
with open('ciphertext','rb') as ciphertext:
    text = ciphertext.read()

#decrypting the ciphertext
decrypted_text = f.decrypt(text)

#writing the decrypted text back into a file
with open('original_text','wb') as original_text:
    original_text.write(decrypted_text)
