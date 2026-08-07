import sqlite3

from rich import print
from rich.panel import Panel 


def read_db(website_name, email):
    session = sqlite3.connect("tutorial.db", autocommit=True)

    cur = session.cursor()

    cur.execute(
    """
    SELECT website_name, email, password
    FROM password
    WHERE website_name = ? AND email = ?
    """,
    (website_name, email)
    )

    result = cur.fetchone()

    return result


def check_master_pass():
    website = input("Website: ").lower()
    email = input("Email: ").lower()
    master_key= input("Key: ").lower()

    while True:
        if master_key != "123":
            print("Wrong Pass")
            continue 
        else:
            break

    resulte = read_db(website, email)
    website = resulte[0]
    email = resulte[1]
    password = resulte[2]

    print(Panel.fit(f"Name: {website}\nEmail: {email}\nPassword: {password}"))

