import json

from encoder import encode
#from file_reader import read_password

def new_entry(website_name, email, user_name, password):
    encodede_pass = encode(password)

    if user_name == "":
        user_name = "N.A"

    data = {
        "name" : website_name,
        "email" :  email,
        "user_name": user_name,
        "password" : encodede_pass,
    }
    return data

def file_entry(record):
    # trys to opens a file if an error then returns a empty dict.
    try:
        with open("vault.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    # This is takes so we can have a list for each website.
    name = record["name"]

    # Formating data into a dict
    account = {
        "email": record["email"],
        "username": record["user_name"],
        "password": record["password"]
    }

    # Checks if the list / website is there or else creats a new list.
    if name not in data:
        data[name] = []

    data[name].append(account)

    with open("vault.json", "w") as f:
        json.dump(data, f, indent=4)
    
def writer_handler(website_name, email, user_name, password):
    data = new_entry(website_name, email, user_name, password)
    file_entry(data)
    return 0
    