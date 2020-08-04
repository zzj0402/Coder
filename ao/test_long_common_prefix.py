import unittest
from to.longest_common_prefix import Solution

SOLUTION = Solution()


class TestLongestCommonPrefix(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(SOLUTION.longestCommonPrefix(
            ['flower', 'flow', 'flight']), "fl", 'Example 1 should work!')


if __name__ == '__main__':
    unittest.main()
