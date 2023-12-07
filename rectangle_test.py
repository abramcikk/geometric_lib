from rectangle import area, perimeter

import math

import unittest

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    def test_rectangle_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_rectangle_area_minus(self):
        with self.assertRaises(Exception):
            area(-1, -1)
    def test_rectangle_area_float(self):
        res = area(1.5, 1.5)
        self.assertEqual(res, 2.25)
    def test_rectangle_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    def test_rectangle_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)
    def test_rectangle_perimeter_minus(self):
        with self.assertRaises(Exception):
            perimeter(-1, -1)
    def test_rectangle_perimeter_float(self):
        res = perimeter(1.5, 1.5)
        self.assertEqual(res, 6)
if __name__ == '__main__':
    unittest.main()
