import unittest
from to.number_of_good_pairs import Solution

SOLUTION = Solution()


class TestStringMethods(unittest.TestCase):

    def test_always_true(self):
        self.assertEqual(True, True)

    def test_eg1(self):
        self.assertEqual(SOLUTION.find_num_of_good_pairs([1, 2, 3, 1, 1, 3]), 4)

    def test_eg2(self):
        self.assertEqual(SOLUTION.find_num_of_good_pairs([1, 1, 1, 1]), 6)

    def test_eg3(self):
        self.assertEqual(SOLUTION.find_num_of_good_pairs([1, 2, 3]), 0)

    def test_eg_empty(self):
        self.assertEqual(SOLUTION.find_num_of_good_pairs([]), 0)

    def test_eg_one(self):
        self.assertEqual(SOLUTION.find_num_of_good_pairs([1]), 0)


if __name__ == '__main__':
    unittest.main()
