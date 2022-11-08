from cryptography.fernet import Fernet

with open('filekey','rb') as filekey:
    key = filekey.read()

f = Fernet(key)

with open('ciphertext','rb') as ciphertext:
    text = ciphertext.read()

decrypted_text = f.decrypt(text)

with open('original_text','wb') as original_text:
    original_text.write(decrypted_text)
