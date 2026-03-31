import sqlite3
import os

DB_NAME = "test_users.db"


def get_connection():
    try:
        with sqlite3.connect(DB_NAME) as connection:
            return connection
    except sqlite3.Error as e:
        print(f"Error while connecting to database: {e}")
        return None


def init_database():
    connection = get_connection()

    try:
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL UNIQUE,
                       email TEXT NOT NULL UNIQUE,
                       age   INTEGER,
                       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
            ''')
        connection.commit()
        print("Table 'users' is ready!")
    except sqlite3.Error as e:
        print(f"Error while initialization: {e}")
    finally:
        connection.close()


def create_user(name, email, age=None):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute('''
                INSERT INTO users (name, email, age)
                VALUES (?, ?, ?)
                       ''', (name, email.lower(), age))
        connection.commit()
        print(f"User '{name}' was successfully created!")
    except sqlite3.IntegrityError:
        print(f"Error: Email already exists.")
        raise
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def get_user_by_id(user_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, email, age FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        connection.close()


def get_user_by_email(email):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, email, age, id FROM users WHERE email=?", (email,))
        result = cursor.fetchone()
        print(f"User with email'{result[1]}' fetched")
        return result
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        connection.close()


def get_all_users():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT name, email, age FROM users")
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        connection.close()


def update_user(user_id, name=None, email=None, age=None):
    connection = get_connection()
    
    cursor = connection.cursor()
    fields = []
    values = []

    if name:
        fields.append("name = ?")
        values.append(name)
    if email:
        fields.append("email = ?")
        values.append(email.lower())
    if age:
        fields.append("age = ?")
        values.append(age)
    if not fields:
        return
    query = f"UPDATE users SET {', '.join(fields)} WHERE id = ?"
    values.append(user_id)

    try:
        cursor.execute(query, tuple(values))
        connection.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"User with ID {user_id} not found.")
        else:
            print(f"User with ID {user_id} was successfully updated.")
    except sqlite3.IntegrityError:
        print(f"Error: Email already exists.")
        raise
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()


def delete_user(user_id):
    connection = get_connection()
    try:
        cursor = connection.cursor()

        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

        connection.commit()

        if cursor.rowcount == 0:
            raise ValueError(f"User with ID {user_id} not found.")
        print(f"User with ID {user_id} was successfully deleted.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        connection.close()




def delete_all_users():
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM users")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")
        connection.commit()
        print(f"Deleted {cursor.rowcount} rows")
        connection.close()
    except sqlite3.Error as e:
        print(f"Error while feleting all users: {e}")


def drop_database():
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
