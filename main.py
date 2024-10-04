#!/usr/bin/env python
import getpass
import subprocess
from cryptography.fernet import Fernet
import os

def main():
    pwd = getpass.getpass()
    if pwd == "linux":
        menu()
    else:
        print("Wrong password")

def clear():
    subprocess.call("clear")

def menu():
    clear()
    print("Welcome to passy your password friend")
    print("Please select an option:")
    print("1 - Decrypt a password")
    print("2 - add a password")
    print("3 - List of passwords")
    opt = int(input())
    if opt == 2:
        add_password()
    elif opt == 3:
        get_password()

def add_password():
    clear()
    password = input("Please enter a password name: ")
    shadow = getpass.getpass()
    encrypt(password, shadow)

def get_password():
    clear()
    passar = []
    files = os.listdir("passwords/")
    for file in files:
        passar.append(file)
        print(file)
    y = input("Type name of password to decrypt: ")
    z = decrypt(y)
    print("The password for " + y + " is " + z)


        

    
def decrypt(password):
    f = open("key.key", "rb")
    key = f.read()
    f.close()

    f = open("passwords/" + password, "rb")
    pwd = f.read()
    f.close()

    fernet = Fernet(key)

    x = fernet.decrypt(pwd)
    x = str(x)
    x = x.split("'")
    return x[1]

def encrypt(name, password):
    f = open("key.key", "rb")
    key = f.read()
    f.close()

    fernet = Fernet(key)

    n = password.encode()

    x = fernet.encrypt(n)

    f = open("passwords/" + name, "wb")
    f.write(x)
    f.close()

if __name__ == "__main__":
    main()
