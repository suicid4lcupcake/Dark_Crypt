from cryptography.fernet import Fernet 
from colorama import Fore
import os 
def mass_encrypt(folder_path , password):
    try:
        actual_dir = os.getcwd()
        print(folder_path)
        files = os.listdir(folder_path)
        os.chdir(folder_path)
        print(files)
        for file in files:
            encrypt(file , password)
        os.chdir(actual_dir)
        print(Fore.GREEN + f'You SuccessFully Encrypted ==> {folder_path}')
    except FileNotFoundError:
        print(Fore.RED + 'Folder Not Found ?!')
def encrypt(filename , password):
    try:
        with open(filename , 'rb') as file:
            data = file.read()
            file.close()
        encrypted_data = Fernet(password).encrypt(data)
        with open(filename , 'w') as file:
            file.write(encrypted_data.decode())
            file.close()
        print(Fore.GREEN + f'You Successfully Encrypted ==> {filename}')
    except FileNotFoundError:
        print(Fore.RED + f'{filename} Not Found ?!')
    except PermissionError:
        print(Fore.RED + f'You Need Root To Encrypt ==> {filename}')
    except:
        print(Fore.RED + f'Failed To Encrypt ==> {filename}')
