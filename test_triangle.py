import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_equal_sides_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_random_area(self):
        res = area(10, 2)
        self.assertEqual(res, 10)

    def test_equal_sides_perimeter(self):
        res = perimeter(11, 11, 11)
        self.assertEqual(res, 33)

    def test_random_perimeter(self):
        res = perimeter(2, 9, 12)
        self.assertEqual(res, 23)