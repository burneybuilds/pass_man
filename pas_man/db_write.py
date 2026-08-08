from db import connection_pool

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
        # session = sqlite3.connect("tutorial.db", autocommit=True)

        # This is for running command and communicating with the db.
        # cur = session.cursor()

        session, cur = connection_pool()

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

def db_update(new_password, updated_at, website_name, email):
    session, cur = connection_pool()

    cur.execute(
    """
    UPDATE password
    SET password = ?, updated_at = ?
    WHERE website_name = ? AND email = ?
    """,
    (new_password, updated_at, website_name, email)
    )

    session.close()
    return 0

def db_delet(website_name, email):
    session, cur = connection_pool()
    cur.execute(
    """
    DELETE FROM password
    WHERE website_name = ? AND email = ?
    """,
    (website_name, email)
    )
    session.close()
    return 0