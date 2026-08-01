import os
import sys

import file_writer
import file_reader

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
                print("\n[-] Error: sh, add , rm , update Only.\n")
                continue
            return user_choice

        except ValueError:
            clear_screen()
            banner()
            print("\n[-] Error: Recheck your dicison.\n")
            continue  

def command_decidion():
    command  = validate_input()

    if command == "show":
        output = show_record()
        if output == 0:
            return "✅ Done."
        else:
            return "🔴 Opps Something went Wrong."
    elif command == "add":
        output = enter_record()
        if output == 0:
            return "✅ Done."
        else:
            return "🔴 Opps Something went Wrong."
    elif command == "del":
        ...
    elif command == "edit":
        ...
    elif command == "exit":
        clear_screen()
        sys.exit("Seen Yaa..")

def enter_record():

    website_name = input("<Pas-Man> Web_Name: ").strip()
    email = input("<Pas-Man> Email: ").strip()
    user_name = input("<Pas-Man> User Name: (Can be left empty if None)").strip()
    password = input("<Pas-Man> PassWord: ").strip()

    data = file_writer.writer_handler(website_name, email, user_name, password)
    
    return data

def show_record():
    requested_pass = input("<Pas-Man> Name: ")
    clear_screen()
    file_reader.display_formater(requested_pass)
    return 0

def main():
    clear_screen()
    banner()
    print(command_decidion())

if __name__ == "__main__":
    main()