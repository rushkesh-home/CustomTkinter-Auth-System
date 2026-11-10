import mysql.connector

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
def verify_user(email, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))
        user = cursor.fetchone()
        
        cursor.close()
        conn.close()
        return user is not None
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False