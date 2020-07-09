import unittest
from to.median_of_two_sorted_arrays import Solution

SOLUTION = Solution()


class TestMedianOfTwoSortedArrays(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(SOLUTION.findMedianSortedArrays([1, 3], [2]), 2.0,
                         "The median should be 2.0")

    def test_example_2(self):
        self.assertEqual(SOLUTION.findMedianSortedArrays([1, 2], [3, 4]), 2.5,
                         "The median should be 2.5")

    def test_example_long(self):
        self.assertEqual(SOLUTION.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 6, 7, 8, 9]), 5.0,
                         "The median should be 5.0")
        self.assertEqual(SOLUTION.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], [0]), 10.0,
                         "The median should be 11.0")
        self.assertEqual(SOLUTION.findMedianSortedArrays([0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 10.0,
                         "The median should be 5.0")

    def test_empty_array(self):
        self.assertEqual(SOLUTION.findMedianSortedArrays(
            [], [1, 2, 3, 4, 5, 6, 7]), 4.0, "Left empty array, result should be 4.0")


if __name__ == '__main__':
    unittest.main()
