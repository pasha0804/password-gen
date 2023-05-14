import json
import os
import string
import random

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    chars = chars.replace('\\', '').replace('"', '').replace("'", "")
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def save_password(website, username, password):
    data = {}
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as f:
            data = json.load(f)
    data[website] = {"username/email": username, "password": password}
    with open("passwords.json", "w") as f:
        json.dump(data, f, indent=4, default=str)

def main():
    website = input("Enter the website for which you want to generate a password: ")
    username = input("Enter the username/email for which you want to generate a password: ")
    
    password = generate_password()
    save_password(website, username, password)

    print(f"Generated password: {password}\n")
    print("Your details have been saved inside the passwords.json file!")

if __name__ == "__main__":
    main()