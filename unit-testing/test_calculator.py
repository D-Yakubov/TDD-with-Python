import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(-6, 2), -3)
        self.assertEqual(calculator.divide(0, 2), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.multiply(-3, 2), -6)
        self.assertEqual(calculator.multiply(0, 3), 0)
        self.assertEqual(calculator.multiply(5, 3), 15)
        self.assertEqual(calculator.multiply(9, -1), -9)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 2), 0)
        self.assertEqual(calculator.subtract(-2, -9), 7)
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(9, 2), 7)
        self.assertEqual(calculator.subtract(0, 9), -9)

if __name__ == "__main__":
    unittest.main()