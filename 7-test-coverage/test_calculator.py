import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(4, 0)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
    
    def test_power_negativ_exp(self):
        with self.assertRaises(ValueError):
            calculator.power(2, -2)
    
    def test_is_even(self):
        self.assertTrue(calculator.is_even(2))
        self.assertFalse(calculator.is_even(3))
        self.assertTrue(calculator.is_even(0))
        self.assertFalse(calculator.is_even(-3))
    
    def test_is_positive(self):
        self.assertTrue(calculator.is_positive(2))
        self.assertFalse(calculator.is_positive(-2))
        self.assertFalse(calculator.is_positive(0))

    def test_square_root(self):
        self.assertEqual(calculator.square_root(16), 4)
    
    def test_modulo(self):
        self.assertEqual(calculator.modulo(3, 2), 1)
    
    def test_modulo_with_zero(self):
        with self.assertRaises(ValueError):
            calculator.modulo(3, 0)
    
    def test_factorial_of_0(self):
        self.assertEqual(calculator.factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(calculator.factorial(1), 1)

    def test_factorial_of_5(self):
        self.assertEqual(calculator.factorial(5), 120)

    def test_factorial_of_10(self):
        self.assertEqual(calculator.factorial(10), 3628800)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            calculator.factorial(-1)

    def test_factorial_of_3(self):
        self.assertEqual(calculator.factorial(3), 6)


if __name__ == "__main__":
    unittest.main()
