from src import *
from colorama import Fore
from encrypt import *
from decrypt import *
from cryptography.fernet import Fernet
import os 
print(Fore.CYAN + icon)

option = input(Fore.YELLOW + '[1]-Encrypt\n[2]-Decrypt\n[99]-Exit\n==>')
if option == '1':
    option = input(Fore.BLUE + '[1]-Single File\n[2]-Mass Files\n==>')
    if option == '1':
        key = Fernet.generate_key()
        filename = input('Filename :')
        print(Fore.YELLOW + f'[+] Generating new key ==> secret.key')
        with open('secret.key' , 'wb') as file:
            file.write(key)
        encrypt(filename , key)
    elif option == '2':
        folder_path = input('Folder_Path :')
        password = input('Password :')
        if folder_path and password:
            mass_encrypt(folder_path , password)
elif option == '2':
    option = input(Fore.YELLOW + '[1]-Single File\n[2]-Mass Files\n==>')
    if option == '1':
        filename = input('Filename :')
        key_file = input('Key File :')
        if not  os.path.exists(key_file):
            print(Fore.RED + 'Key File Do Not Exists')
        else:
            with open(key_file , 'rb') as file:
                key = file.read()
            decrypt(filename , key)
    elif option == '2':
        folder_path = input('Folder_Path :')
        password = input('Password :')
        if folder_path and password:
            mass_decrypt(folder_path , password)
print(Fore.WHITE + '')
