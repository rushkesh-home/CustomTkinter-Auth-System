import mysql.connector
import bcrypt

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",      # Your MySQL root password
        database="user_auth"       # Database name from your Databse.sql
    )

# 2. Alias defined AFTER connect_db so both names work everywhere
connect_db = get_connection

# 3. User verification function for signin.py
def verify_user(email, entered_password):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # 1. Fetch only the stored hash for this email
        query = "SELECT password_hash FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if not result:
            return False  # Email does not exist

        stored_hash = result[0]  # This is the string stored in the database

        # 2. Compare using bcrypt.checkpw
        # Both must be encoded to utf-8 bytes
        return bcrypt.checkpw(
            entered_password.encode("utf-8"),
            stored_hash.encode("utf-8")
        )

    except Exception as err:
        print(f"Auth error: {err}")
        return False
