import json

from encoder import encode
from file_reader import read_password

def validate_website_name():
    while True:
        name = input("<Pas-Man> Name : ").strip()
        if not name.isalpha():
            print("Name != Numbers.")
            continue
        return name

def new_entry():
    website_name = validate_website_name()
    email = input("<Pas-Man> Email : ")
    user_name = input("<Pas-Man> User_name : (Can be left empty if N/A)")
    password = input("<Pas-Man> PassWord : ")

    encodede_pass = encode(password)

    if user_name == "":
        user_name = "N.A"

    data = {
        "name" : website_name,
        "Email" :  email,
        "User Name": user_name,
        "Password" : encodede_pass,
    }
    return data

def acc_name():
    data = new_entry()

    name = data["name"]

    name = {
        name : [data]
    }
    return name


def file_entry():
    data = acc_name()
    with open("valut.json", "a") as w:
        json.dump(data, w, indent=4, ensure_ascii=False)

file_entry()