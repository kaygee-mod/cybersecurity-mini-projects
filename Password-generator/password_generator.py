import random
import string

def generate_password(length):
    if length < 6:
        print("Password should be atleast 6 characters for security")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters)for i in range(length))
    return password

if __name__ == "__main__":
    print("=== Passwords Generator ===" )
    length = int(input("Enter the desired passwords length:"))
    new_password = generate_password(length)
    if new_password:
        print("Generated password:", new_password)