import unittest
from to.median_of_two_sorted_arrays import Solution


class TestMedianOfTwoSortedArrays(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_example_2(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
