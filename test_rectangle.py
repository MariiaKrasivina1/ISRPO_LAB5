import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_val(self):
        res = area(31, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(11, 11)
        self.assertEqual(res, 121)

    def test_random_area(self):
        res = area(12, 4)
        self.assertEqual(res, 48)

    def test_square_perimeter(self ):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)

    def test_random_perimeter(self):
        res = perimeter(8, 4)
        self.assertEqual(res, 24)
