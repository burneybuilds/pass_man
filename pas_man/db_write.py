from .db import connection_pool

def db_connection(website_name: str, email: str, user_name: str, password: str, salt: str, nonce: str, created_at: str, updated_at: str) -> int:
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
    try:
        # make a connection using the connection pool located in the db.py file.
        session, cur = connection_pool()

        cur.execute(
            """
            INSERT INTO password
            (website_name, email, user_name, password, salt, nonce, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                website_name,
                email,
                user_name,
                password,
                salt,
                nonce,
                created_at,
                updated_at
            )
        )

        session.commit()
        # Closes the connection to the db.
        session.close()

        # If eveything goes right it will => 0 == OK 
        return 0
    except :
        # Else 1 => !OK
        return 1

def db_update(new_password: str, updated_at: str, salt: str, nonce: str, website_name: str, email: str) -> int:
    session, cur = connection_pool()

    try:
        cur.execute(
        """
        UPDATE password
        SET password = ?, updated_at = ? , salt = ?, nonce = ?
        WHERE website_name = ? AND email = ?
        """,
        (new_password, updated_at, salt , nonce , website_name, email)
        )

        session.commit()
        session.close()
        return 0
    except Exception as e:
        return 1 
    
def db_delet(website_name: str , email: str) -> int:
    session, cur = connection_pool()
    try:
        cur.execute(
        """
        DELETE FROM password
        WHERE website_name = ? AND email = ?
        """,
        (website_name, email)
        )
        session.commit()
        session.close()
        return 0
    except Exception as e:
        return 1