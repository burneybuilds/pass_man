import re

from rich import print
from rich.panel import Panel

from .db_read import read_db
from .cipher import decrypt_pass

"""
Validate user email input.

Called by `writer_handler()`. Continuously prompts the user until the
entered email matches the required regular expression.

Returns:
    str: A valid email address.
"""
def validate_email():
    while True:
        # Takes input from the user. 
        email = input("<Pas-Man> Email: ").strip()

        # Check if the email matches the required pattern.
        # .+      -> One or more characters before the '@'.
        # @       -> The '@' symbol.
        # .+      -> One or more characters after the '@'.
        # \.com   -> The email must end with '.com'.
        if re.search(r".+@.+\.com", email):
            return email
        else:
            continue

"""
Prompt the user for a website name.

Continues prompting until a valid, non-empty input is provided.

Returns:
    str: The website name.
"""
def website_name_valid():
    while True:
        name = input("<Pas-Man> Web_Name: ").strip().lower()
        # An empty string evaluates to False, while any non-empty string
        # evaluates to True. Continue only if the user entered a value.
        if name:
            return name
        else:
            continue 

def valid_user_name():
    user_name =  input("<Pas-Man> User Name: ")

    # Checks if the input is empyt if yes then return None == Null
    if not user_name :
        return None

    return user_name

# def validate_password():
#     return input("<Pas-Man> PassWord: ")

def confirm_data(website_name, email, user_name, password) -> int:
    print(Panel.fit(f"Name: {website_name}\nEmail: {email}\nUser_Name: {user_name}\nPassword: {password}"))
    while True:
        user_input = input("Check if all the data is correct? Yes / No: ").lower().strip()
        if user_input in {"y", "yes"}:
            return 0
        if user_input in {"n", "no"}:
            return 1


def validate_password(old_password: str, website_name: str, email: str, master_key: str ) -> str:
    data = read_db(website_name, email)
    if data is None:
        return False

    salt = data[3]
    nonce = data[4]
    encrypted_password = data[2]

    password = decrypt_pass(master_key, encrypted_password, salt, nonce)

    if password == old_password:
        return True
    else:
        return False

def update_filed(field: str ) -> str:
    match field:
        case "website_name":
            return input("Update the website_name: ").strip().lower()
        case "email":
            return "Not Found"
        case "user_name":
            return "Unknown"
        case "password": 
            return ""
        case _ : 
            return None