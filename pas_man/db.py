import sqlite3

def connection_pool():
    """
    Connect to the SQLite database and ensure the password table exists.

    Returns:
        tuple: SQLite connection and cursor if successful.
        str: Error message if something goes wrong.
    """
    try:
        # Open the database connection.
        session = sqlite3.connect("main.db", autocommit=True)
        cur = session.cursor()

        # Check if the password table already exists.
        cur.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type = 'table' AND name = 'password'
        """)

        result = cur.fetchone()

        # Table exists, so we're good to go.
        if result:
            return session, cur

        # No table? No problem, SQLite, build one. :)
        cur.execute("""
            CREATE TABLE password (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                website_name TEXT NOT NULL,
                email TEXT,
                user_name TEXT,
                password TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)

        # Return the connection and cursor for database operations.
        return session, cur

    except Exception as e:
        # Something went wrong while connecting or creating the table.
        # just like your last relationship, nothing works.
        return f"Something Went Wrong {e}"