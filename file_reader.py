import json

from file_writer import acc_name

def read_password():
    input_data = acc_name()

    name = input_data["name"]

    with open("valut.json", "r") as r:
        data = json.load(r)
        ex_name = data["github"]

    if name == ex_name:
        return True
    else:
        return False
            

