from cryptography.fernet import Fernet
from password_utilize import encrypt_password
#writ the key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:#it wil ggenerated key tha save secret.key
        f.write(key)

if __name__ == "__main__":
    #use only one tym when need password binary the remove comment
    
    #generate_key()
    encrypted=encrypt_password(input("Enter The Password :"))

    #its mix of password + and randmoly generated key
    print(encrypted) #copy this 