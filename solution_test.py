import unittest
from solution import generate_triangles, detect_triangle


class SolutionTestCase(unittest.TestCase):

    def test_create(self):
        test = list(generate_triangles())
        print(test)
        self.assertEqual(len(test), 72)

    def test_detect(self):
        self.assertEqual("A1", detect_triangle((0,10), (0,0), (10,10)))
        self.assertEqual("A2", detect_triangle((10, 0), (0, 0), (10, 10)))
        self.assertEqual("A12", detect_triangle((60, 0), (50, 0), (60, 10)))
        self.assertEqual("F1", detect_triangle((0, 60), (0, 50), (10, 60)))
        self.assertEqual("F12", detect_triangle((60, 50), (50, 50), (60, 60)))

        # out of bounds
        with self.assertRaises(ValueError):
            detect_triangle((60, 70), (60, 60), (70, 70))

        # Bad Order
        with self.assertRaises(ValueError):
            detect_triangle((10, 10), (0, 0), (10, 0))

        # Not a triangle
        with self.assertRaises(ValueError):
            detect_triangle((11, 10), (5, 0), (10, 0))

if __name__ == '__main__':
    unittest.main()
