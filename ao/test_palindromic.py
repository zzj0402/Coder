import unittest
from to.palindromic import Solution


class TestPalindromic(unittest.TestCase):

    def test_example_1(self):
        S=Solution()
        self.assertEqual(S.longestPalindrome("babad"),"bab","test case 1 should pass")

if __name__ == '__main__':
    unittest.main()
