from cryptography.fernet import fernet
#Generate a key
def generate_key():
    key= fernet.generate_key()
    with open ("secret.key", "wb") as key_file:
        key_file.write(key)

#Load the key
def load_key():
    return open("secret.key", "rb").read()

#Encrypt a file
def encrypyt_file(filename, key):
    f = fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
        encrypted = f.encrypt(data)
        with open(filename + ".enc", "wb") as file:
            file.writeline(encrypted)
            print(f"{filename} has been encrypted!")

#Decrypt File
def decrypt_file(filename, key):
    f = fernet(key)
    with open(filename, "rb")as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    original_name = filename.replace(".enc", "")
    with open(original_name, "wb")as file:
        file.write(decrypted)
        print(f"{filename} has been decrypted!")

if __name__ =="__main__":
    choice = input("Do you want to (E)ncrypt or (D)ecrypt?").lower()
    if choice == "e":
        generate_key()
        key= load_key()
        filename = input("enter the filename to encrypt")
        encrypyt_file(filename, key)
    elif choice=="d":
        key= load_key()
        filename = input ("Enter the file name to decrypt")
        decrypt_file(filename, key)
    else:
        print("Invalid choice")

    
    
                  

        
        
