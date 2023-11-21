from triangle import area, perimeter

import math

import unittest

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_triangle_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, "ERROR")

    def test_triangle_area_minus(self):
        res = area(-1, -1,)
        self.assertEqual(res, "ERROR")

    def test_triangle_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_triangle_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, "ERROR")

    def test_triangle_perimeter_minus(self):
        res = perimeter(-1, -1, -1)
        self.assertEqual(res, "ERROR")

if __name__ == '__main__':
    unittest.main()
