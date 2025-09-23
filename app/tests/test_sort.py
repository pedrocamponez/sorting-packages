import unittest

from app.core.sort import sort
from app.core.consts import STANDARD, SPECIAL, REJECTED


class TestSortFunction(unittest.TestCase):
    def test_standard_package(self):
        self.assertEqual(sort(50, 50, 50, 10), STANDARD)

    def test_bulky_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), SPECIAL)

    def test_bulky_by_dimension(self):
        self.assertEqual(sort(200, 10, 10, 10), SPECIAL)

    def test_heavy_package(self):
        self.assertEqual(sort(50, 50, 50, 25), SPECIAL)

    def test_rejected_package(self):
        self.assertEqual(sort(200, 200, 200, 30), REJECTED)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sort("a", 10, 10, 10)
        with self.assertRaises(ValueError):
            sort(0, 10, 10, 10)


if __name__ == "__main__":
    unittest.main()
