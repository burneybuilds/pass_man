import re
from datetime import datetime
import sqlite3
from encoder import encode
from rich import print
from rich.panel import Panel

# cur.execute("CREATE TABLE password(website_name, email, user_name, password, created_at)")


"""
Insert a new password entry into the SQLite database.

This function is called by `writer_handler()` after validating the
user's input. 

Args:
    website_name (str): Name of the website or service.
    email (str): Email address associated with the account.
    user_name (str): Username for the account.
    password (str): Encrypted password to store.
    time (str): Timestamp indicating when the entry was created.

Returns:
    int:
        0 if the entry was successfully inserted.
        1 if an error occurred while inserting the entry.
"""
def db_connection(website_name, email, user_name, password, created_at, updated_at):
    try:
        # Creates a connection with the sqllite db.
        session = sqlite3.connect("tutorial.db", autocommit=True)

        # This is for running command and communicating with the db.
        cur = session.cursor()
        
        # check if the tabel is there else create one.
        cur.execute("""
        CREATE TABLE IF NOT EXISTS password (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            website_name TEXT NOT NULL,
            email TEXT,
            user_name TEXT,
            password TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """)

        cur.execute(
            """
            INSERT INTO password
            (website_name, email, user_name, password, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (website_name, email, user_name, password, created_at, updated_at)
        )
        # Updates the db with the data.
        # session.commit()

        # Closes the connection to the db.
        session.close()

        # If eveything goes right it will => 0 == OK 
        return 0
    except :
        # Else 1 => !OK
        return 1

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

def validate_password():
    return input("<Pas-Man> PassWord: ")

def confirm_data(website_name, email, user_name, password):
    print(Panel.fit(f"Name: {website_name}\nEmail: {email}\nUser_Name: {user_name}\nPassword: {password}"))
    print("Check if all the data is correct? ")

    while True:
        try:
            master_key = int(input("Enter the Master Key: "))
            return master_key
        except ValueError:
            continue

def writer_handler():
    website_name = website_name_valid()
    email = validate_email()
    user_name = valid_user_name()
    password = validate_password()
    time = str(datetime.now().strftime("%Y-%m-%d"))
    key = confirm_data(website_name, email, user_name, password)

    if key != 123:
        return "Wrong Password"
    
    data = db_connection(website_name, email, user_name, password, time, time)
    return data

def main():
    writer_handler()

if __name__ == "__main__":
    main() 