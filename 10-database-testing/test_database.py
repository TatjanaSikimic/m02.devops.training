import unittest
import database
import sqlite3


class TestDatabase(unittest.TestCase):
    def setUp(self):
        database.init_database()
        database.delete_all_users()

    def tearDown(self):
        database.delete_all_users()

    def test_create_user(self):
        test_name = "user1"
        test_email = "user1@mail.com"
        test_age = 20

        database.create_user(test_name, test_email, test_age)

        connection = database.get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT name, email, age FROM users WHERE email=?", (test_email,))
        result = cursor.fetchone()
        connection.close()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], test_name)
        self.assertEqual(result[1],test_email)
        self.assertEqual(result[2], test_age)

    def test_create_duplicate_user(self):
        user2_name = "user2"
        user1_name = "user1"
        user1_email = "user1@mail.com"
        age = 20

        database.create_user(user1_name, user1_email, age)
        with self.assertRaises(sqlite3.IntegrityError):
            database.create_user(user2_name, user1_email, age)

    def test_get_user_by_id(self):
        test_id = 1
        test_name = "user1"
        test_email = "user1@mail.com"
        test_age = 20
        database.create_user(test_name, test_email, test_age)
        result_user = database.get_user_by_id(1)
        self.assertIsNotNone(result_user)
        self.assertEqual(result_user[0], test_name)
        self.assertEqual(result_user[1],test_email)
        self.assertEqual(result_user[2], test_age)

    def test_get_user_by_email(self):
        test_name = "user1"
        test_email = "user1@mail.com"
        test_age = 20
        database.create_user(test_name, test_email, test_age)
        result_user = database.get_user_by_email(test_email)
        self.assertIsNotNone(result_user)
        self.assertEqual(result_user[1],test_email)

    def test_get_all_users(self):
        test_users = [
        ('user1', 'user1@mail.com', 20),
        ('user2', 'user2@mail.com', 22),
        ('user3', 'user3@mail.com', 23)]

        for entry in test_users:
            database.create_user(entry[0], entry[1], entry[2])

        all_users = database.get_all_users()

        self.assertEqual(len(all_users), 3)
        self.assertCountEqual(all_users, test_users)


    def test_update_user(self):
        old_name = "user1"
        old_email = "user1@mail.com"
        old_age = 20

        database.create_user(old_name, old_email, old_age)

        created_user = database.get_user_by_email(old_email)
        created_user_id = created_user[3]

        new_name = "new_name"
        database.update_user(created_user_id, name=new_name)
        updated_user = database.get_user_by_id(created_user_id)
        self.assertEqual(updated_user[0], new_name)
        self.assertEqual(updated_user[1], old_email)
        self.assertEqual(updated_user[2], old_age)

    def test_update_nonexistent(self):
        with self.assertRaises(ValueError):
            database.update_user(34, name="updated_name")

    def test_delete_user(self):
        name = "user1"
        email = "user1@mail.com"
        age = 20

        database.create_user(name, email, age)

        created_user = database.get_user_by_email(email)
        created_user_id = created_user[3]

        database.delete_user(created_user_id)
        deleted_user = database.get_user_by_id(created_user_id)
        self.assertIsNone(deleted_user)

    def test_delete_nonexistent(self):
        with self.assertRaises(ValueError):
            database.delete_user(1)


if __name__ == "__main__":
    unittest.main()
