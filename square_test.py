from square import area, perimeter

import math

import unittest

class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100)
    def test_square_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_square_area_minus(self):
        with self.assertRaises(Exception):
            area(-1)
    def test_square_area_float(self):
        res = area(1.5)
        self.assertEqual(res, 2.25)
    def test_square_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
    def test_square_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_square_perimeter_minus(self):
        with self.assertRaises(Exception):
            perimeter(-1)
    def test_square_perimeter_float(self):
        res = perimeter(1.5)
        self.assertEqual(res, 6)

if __name__ == '__main__':
    unittest.main()