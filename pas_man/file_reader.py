import json

from rich import print
from rich.panel import Panel 

from decoder import decode

"""
Function is run if there is 2 or more account for the websites.
"""
def choice_pass():
    print("You have Multipla Account on this service ! ")
    return input("<Pas-Man> Enter the Email? ").strip()

def show_req(name):
    email = ""
    password = ""
    encoded_pass= ""
    requested_item = {}
    with open("vault.json", "r") as r:
        data = json.load(r)
        if name in data:
            requested_item = data[name]

    if len(requested_item) > 1:
        email_req = choice_pass()

        for r in requested_item:
            if r["email"] == email_req:
                email = r["email"]
                encoded_pass = r["password"]
    else:
        for r in requested_item:
            email = r["email"]
            encoded_pass = r["password"]
            
    password = decode(encoded_pass)

    return email, password


def display_formater(name):
    email, password = show_req(name)

    print(Panel(f"Email: [green]{email}\nPassword: [green]{password}", title="Pas Man"))
    