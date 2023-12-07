from circle import area, perimeter

import math

import unittest

class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.159, delta=0.001)
    def test_circle_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_circle_area_minus(self):
        with self.assertRaises(Exception):
            area(-1)
    def test_circle_area_float(self):
        res = area(1.5)
        self.assertAlmostEqual(res, 7.06, delta=0.01)
    def test_circle_perimeter(self):
        res = perimeter(10)
        self.assertAlmostEqual(res, 62.83, delta = 0.01)
    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_circle_perimeter_minus(self):
        with self.assertRaises(Exception):
            perimeter(-1)
    def test_circle_perimeter_float(self):
        res = perimeter(1.5)
        self.assertAlmostEqual(res, 9.42, delta = 0.01)

if __name__ == '__main__':
    unittest.main()