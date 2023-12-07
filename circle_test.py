from circle import area, perimeter

import math

import unittest

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)
    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_circle_area_minus(self):
        with self.assertRaises(Exception):
            area(-1)
    def test_circle_area_float(self):
        res = area(1.5)
        self.assertEqual(res, 7.0685834705770345)
    def test_circle_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)
    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_circle_perimeter_minus(self):
        with self.assertRaises(Exception):
            perimeter(-1)
    def test_circle_perimeter_float(self):
        res = perimeter(1.5)
        self.assertEqual(res, 9.42477796076938)

if __name__ == '__main__':
    unittest.main()