import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"


class TestSecurity(unittest.TestCase):
    def test_missing_field_a(self):
        response = requests.post(f"{BASE_URL}/add", json={"b": 5})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Missing required fields 'a' and 'b'")

    def test_missing_field_b(self):
        response = requests.post(f"{BASE_URL}/add", json={"a": 4})
        self.assertEqual(response.status_code, 400)

    def test_invalid_data_type(self):
        response = requests.post(f"{BASE_URL}/subtract", json={"a": "invalid type", "b": 5})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Invalid data types. Numbers required")

    def test_empty_string_value(self):
        response = requests.post(f"{BASE_URL}/multiply", json={"a": "", "b": 5})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Invalid data types. Numbers required")

    def test_very_large_number(self):
        response = requests.post(f"{BASE_URL}/multiply", json={"a": 1e20, "b": 1e20})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Numbers too large")

    def test_malformed_json(self):
        response = requests.post(f"{BASE_URL}/add",
                                 data='{"a": 10, "b": 20',
                                 headers={"Content-Type": "application/json"}
                                )
        self.assertEqual(response.status_code, 400)

    def test_division_by_zero_returns_safe_error(self):
        response = requests.post(f"{BASE_URL}/divide", json={"a": 20, "b": 0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["error"], "Division by zero is not permitted")


if __name__ == "__main__":
    unittest.main()
