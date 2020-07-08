import unittest
from to.median_of_two_sorted_arrays import Solution


class TestMedianOfTwoSortedArrays(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(Solution([1, 3], [2]), 2.0,
                         "The median should be 2.0")

    def test_example_2(self):
        self.assertEqual(Solution([1, 2], [3, 4]), 2.5,
                         "The median should be 2.5")


if __name__ == '__main__':
    unittest.main()
