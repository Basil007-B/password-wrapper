
from cryptography.fernet import Fernet

class Fake_str(str):#it hlp th mask the password using print or return
     def __str__(self):
      return "*********"
     def __repr__(self):
         return "*********"

#it read   randomly generated key in secret binary key
def load_key():
    return open("secret.key", "rb").read()

#encrypyt plain password
#encrypt/decrypted encode/decode is methodd of fernet
def encrypt_password(password):
    key = load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())


def decrypt_password(encrypted_password):
    key = load_key()
    f=Fernet(key)
    decrypted=f.decrypt(encrypted_password).decode()

    return Fake_str(decrypted)


def get_decrypt_password():
    #passting rangenrated key
    encrypted_password =""#once genrated paste here remoe qoutos
    return decrypt_password(encrypted_password)


