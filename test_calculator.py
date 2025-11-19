# https://github.com/pfeilhenry/lab11-HP
# Partner 1: Henry Pfeil
# Partner 2: Did not have partner

import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(6,4),10)
        self.assertEqual(calculator.add(-3,9),6)
        self.assertEqual(calculator.add(1,-1),0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10,7),3)
        self.assertEqual(calculator.subtract(5,12),-7)
        self.assertEqual(calculator.subtract(-6,-10),4)

    def test_multiply(self):
        self.assertEqual(calculator.mul(5,6),30)
        self.assertEqual(calculator.mul(-3,8),-24)
        self.assertEqual(calculator.mul(0,451),0)

    def test_divide(self):
        self.assertEqual(calculator.div(3,15),5)
        self.assertEqual(calculator.div(-5,20),-4)
        self.assertAlmostEqual(calculator.div(0.25,1),4)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0,12)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0,-7)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(4,64),3)
        self.assertAlmostEqual(calculator.logarithm(5,125),3)
        a,b=7,343
        self.assertAlmostEqual(
            calculator.logarithm(a,b),
            math.log(b,a)
        )

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(0,25)
        with self.assertRaises(ValueError):
            calculator.logarithm(-3,9)
        with self.assertRaises(ValueError):
            calculator.logarithm(1,50)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(3,0)
        with self.assertRaises(ValueError):
            calculator.logarithm(4,-9)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(6,8),10)
        self.assertAlmostEqual(calculator.hypotenuse(7,24), 25)
        self.assertAlmostEqual(calculator.hypotenuse(-6,-8),10)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(16),4)
        self.assertEqual(calculator.square_root(49),7)
        self.assertAlmostEqual(calculator.square_root(5),math.sqrt(5))
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
