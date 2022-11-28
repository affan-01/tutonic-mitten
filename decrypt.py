from cryptography.fernet import Fernet

def decrypt_file(key):
    #with open('filekey','rb') as filekey:
       # key = filekey.read()

    f = Fernet(key)

    #open encrypted text file and store it in a variable
    with open('static/ciphertext','rb') as ciphertext:
        text = ciphertext.read()

    #decrypt the text
    decrypted_text = f.decrypt(text)

    #write the decrypted text to the file
    with open('static/original_text','wb') as original_text:
        original_text.write(decrypted_text)
    
    return decrypted_text
