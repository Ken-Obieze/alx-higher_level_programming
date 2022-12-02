""" unit test for 6-max_integer.py"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertAlmostEqual(max_integer([4, 5, 7]), 7)
        self.assertAlmostEqual(max_integer([8, 24, 32, 332]), 332)
        self.assertAlmostEqual(max_integer([-1, 4, 31]), 31)
        self.assertAlmostEqual(max_integer([222]), 222)
        self.assertAlmostEqual(max_integer([]), None)

    def test_non_int(self):
        self.assertRaises(TypeError, max_integer, True)
