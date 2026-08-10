import os
import sys
from datetime import datetime

from rich import print
from rich.panel import Panel 

import validate 
import db_write 
import db_read 

import cipher

def banner():
    passman_banner=rf"""
______             ___  ___            
| ___ \            |  \/  |            
| |_/ /_ _ ___ ___ | .  . | __ _ _ __  
|  __/ _` / __/ __|| |\/| |/ _` | '_ \ 
| | | (_| \__ \__ \| |  | | (_| | | | |
\_|  \__,_|___/___/\_|  |_/\__,_|_| |_|
"""
    print(passman_banner)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_input():
    user_options = ["show", "add" , "del" , "edit", "exit"]
    while True:

        try:
            user_choice = input("<Pas-Man> ").strip()

            if user_choice not in user_options:
                clear_screen()
                banner()
                print("\n[-] Error: show, add , rm, update.\n")
                continue
            return user_choice

        except ValueError:
            clear_screen()
            banner()
            print("\n[-] Error: Recheck your dicison.\n")
            continue  
        except KeyboardInterrupt:
            clear_screen()
            sys.exit("Seen Yaa..")

def command_decidion():
    while True:
        command  = validate_input()
    
        if command == "show":
            show_command_handler()
        elif command == "add":
            add_command_handler()
        elif command == "del":
            del_command_handler()
        elif command == "edit":
            edit_command_handler()
        elif command == "exit":
            clear_screen()
            sys.exit("Seen Yaa..")

def add_command_handler():
    """
    Handle the `add` command by validating the entry details,
    confirming the master key, and writing the new entry to the database.

    Returns:
        str: The result of the database operation or an error message
        if the master key is incorrect.
    """
    # Collect and validate the new entry details.
    website_name = validate.website_name_valid()
    email = validate.validate_email()
    user_name = validate.valid_user_name()
    plain_password = validate.validate_password()

    # Record when the entry was created.
    time = str(datetime.now().strftime("%Y-%m-%d"))

    # # Make sure the person adding the password is actually us. 👀
    # key = validate.confirm_data(website_name, email, user_name, p)
    key = input("<Pas_Man> Master Key: ")
    password , salt, nonce = cipher.encrypt_pass(key, plain_password)

    # Everything checks out — send the entry to SQLite.
    data = db_write.db_connection(
    website_name,
    email,
    user_name,
    password,
    salt,
    nonce,
    time,
    time,
    )

    return data

def edit_command_handler():
    website_name =  input("<Pas_Man> Website: ")
    email = input("<Pas_Man> Email: ")
    time = str(datetime.now().strftime("%Y-%m-%d"))

    old_password =  input("<Pas_Man> Old PassWord: ").strip()

    master_key= input("Key: ").lower()        

    flags = validate.validate_password(old_password, website_name, email, master_key)

    if flags:
        new_password = input("<Pas_Man> New PassWord: ").strip()
        password , salt, nonce = cipher.encrypt_pass(master_key, new_password)
        code = db_write.db_update(
            password, 
            time, 
            salt , 
            nonce, 
            website_name, 
            email)
        print("[green]Done")
    else:
        print("[red]Wrong Password or Master Key.")
    

def show_command_handler():
    website = input("Website: ").lower()
    email = input("Email: ").lower()
    master_key= input("Key: ").lower()

    result = db_read.read_db(website, email)
  
    website = result[0]
    email = result[1]
    encrypted_password = result[2]
    salt = result[3]
    nonce = result[4]

    password = cipher.decrypt_pass(master_key, encrypted_password, salt, nonce)
    clear_screen()
    banner()
    print(Panel.fit(f"Name: {website}\nEmail: {email}\nPassword: {password}"))

def del_command_handler():
    website_name =  input("<Pas_Man> Website: ")
    email = input("<Pas_Man> Email: ")
    password = input("<Pas_Man> Password: ")
    master_key= input("Key: ").lower()
    code = validate.validate_password(password, website_name, email, master_key)
    if code:
        db_write.db_delet(website_name, email)
        print("[green]Done")
    else:
        print("[red]Something Went Wrong.")

def main():
    clear_screen()
    banner()
    command_decidion()

if __name__ == "__main__":
    main()