from triangle import area, perimeter
import math
import unittest
class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)
    def test_triangle_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_triangle_area_minus(self):
        with self.assertRaises(Exception):
            area(-1, -1)
    def test_triangle_area_float(self):
        res = area(1.5, 1.5)
        self.assertEqual(res, 1.125)
    def test_triangle_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)
    def test_triangle_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    def test_triangle_perimeter_minus(self):
        with self.assertRaises(Exception):
            perimeter(-1, -1, -1)
    def test_triangle_perimeter_float(self):
        res = perimeter(1.5, 1.5, 1.5)
        self.assertEqual(res, 4.5)

if __name__ == '__main__':
    unittest.main()