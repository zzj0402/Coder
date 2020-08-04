import unittest
from to.longest_common_prefix import Solution

SOLUTION = Solution()


class TestLongestCommonPrefix(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(SOLUTION.longestCommonPrefix(
            ['flower', 'flow', 'flight']), "fl", 'Example 1 should work!')

    def test_example_2(self):
        self.assertEqual(SOLUTION.longestCommonPrefix(
            ['dog', 'racecar', 'car']), "", 'Example 2 should work!')

    def test_example_empty_array(self):
        self.assertEqual(SOLUTION.longestCommonPrefix(
            []), "", 'Empty array should return empty string!')

    def test_example_empty_strings(self):
        self.assertEqual(SOLUTION.longestCommonPrefix(
            ['', '', '', '', '']), "", 'Array of empty strings should return empty string!')

    def test_one_string(self):
        self.assertEqual(SOLUTION.longestCommonPrefix(
            ['a']), 'a', "One string should return the string")


if __name__ == '__main__':
    unittest.main()
