from rectangle import area, perimeter

import math

import unittest

class SquareTestCase(unittest.TestCase):
    def test_rectangle_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_rectangle_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, "ERROR")

    def test_rectangle_area_minus(self):
        res = area(-1, -1)
        self.assertEqual(res, "ERROR")

    def test_rectangle_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_rectangle_perimeter_zero(self):
        res = perimeter(0, 0)
        self.assertEqual(res, "ERROR")

    def test_rectangle_perimeter_minus(self):
        res = perimeter(-1, -1)
        self.assertEqual(res, "ERROR")

if __name__ == '__main__':
    unittest.main()
