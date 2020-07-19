import unittest
from to.reverse_integer import Solution

SOLUTION = Solution()


class TestReverseInteger(unittest.TestCase):

    def test_(self):
        self.assertEqual(SOLUTION.reverse(123), 321)


if __name__ == '__main__':
    unittest.main()
