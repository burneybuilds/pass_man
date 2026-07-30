import os
import sys


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
        ...
    elif command == "add":
        ...
    elif command == "del":
        ...
    elif command == "edit":
        ...
    elif command == "exit":
        clear_screen()
        sys.exit("Seen Yaa..")

def main():
    clear_screen()
    banner()
    command_decidion()

if __name__ == "__main__":
    main()