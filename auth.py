import bcrypt
from database import connect_db


def signup(username, email, password):

    connection = connect_db()
    cursor = connection.cursor()

    # Check whether email already exists
    cursor.execute(
        "SELECT id FROM users WHERE email = %s",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        print("Email already registered!")
        cursor.close()
        connection.close()
        return False

    # Hash the password
    password_hash = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    # Store user information
    query = """
        INSERT INTO users (username, email, password_hash)
        VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (username, email, password_hash.decode("utf-8"))
    )

    connection.commit()

    cursor.close()
    connection.close()

    print("Registration successful!")
    return True