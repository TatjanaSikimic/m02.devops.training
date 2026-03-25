import unittest
from math_sum import add, subtract, multiply, divide, power, modulo


class TestMathUtils(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)

    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_add_floating_point(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=5)

    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract(3, 8), -5)

    def test_subtract_zero(self):
        self.assertEqual(subtract(7, 0), 7)

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply(7, 1), 7)

    def test_multiply_negative(self):
        self.assertEqual(multiply(-2, 4), -8)

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_one(self):
        self.assertEqual(divide(7, 1), 7)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)
    
    def test_power_positive(self):
        self.assertEqual(power(2,5),32)
    
    def test_power_negative_base(self):
        self.assertEqual(power(-2, 5), -32)
    
    def test_power_negative_exp(self):
        with self.assertRaises(ValueError):
            power(4, -2)

    def test_power_negative_exp_negative_base(self):
        with self.assertRaises(ValueError):
            power(-4, -1)
    
    def test_floating_power(self):
        self.assertEqual(power(9, 0.5), 3)
    
    def test_power_zero_exp(self):
        self.assertEqual(power(9, 0), 1)
    
    def test_modulo_positive(self):
        self.assertEqual(modulo(3, 2), 1)
    
    def test_modulo_zero(self):
        with self.assertRaises(ValueError):
            modulo(3, 0)
    
    def test_modulo_negative(self):
        self.assertEqual(modulo(3, -2), -1)
    
    def test_modulo_negative_negative_num(self):
        self.assertEqual(modulo(-3, -2), -1)

if __name__ == "__main__":
    unittest.main()
