import unittest
from datastore import store_value, get_value, delete_value, list_keys, database

class TestDatabase(unittest.TestCase):

    def setUp(self):
        database.clear()
    
    def test_set_and_get_value(self):
        store_value("name", "Tatjana")
        self.assertEqual(database["name"], "Tatjana")
        self.assertEqual(get_value("name"), "Tatjana")        

    def test_get_nonexistent_key(self):
        self.assertEqual(get_value("non-existing-key"), None)
    
    def test_delete_existing_key(self):
        store_value("name", "Tatjana")
        self.assertTrue(delete_value("name"))
        self.assertNotIn("name", list_keys())

    def test_delete_nonexistent_key(self):
        self.assertFalse(delete_value("non-existing-key"))

    def test_list_keys(self):
        store_value("a", 1)
        store_value("b", 2)
        self.assertIn("a", list_keys())
        self.assertIn("b", list_keys())

if __name__ == "__main__":
    unittest.main()