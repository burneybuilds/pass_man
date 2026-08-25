from .db import connection_pool

def read_db(website_name: str, email: str) -> tuple:
    """
    Retrieve a password entry from the database using the website name
    and email address.

    Returns:
        tuple: The matching website, email, and password.
        None: If no matching entry is found.
    """
    # Get the database connection and cursor.
    session, cur = connection_pool()

    # Look for an entry matching the website and email.
    cur.execute(
        """
        SELECT website_name, email, password , salt, nonce
        FROM password
        WHERE website_name = ? AND email = ?
        """,
        (website_name, email)
    )

    # Get the first matching entry.
    result = cur.fetchone()

    # We're done here... just like your last relationship.
    session.close()

    return result
