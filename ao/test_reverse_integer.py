import unittest
from to.reverse_integer import Solution

SOLUTION = Solution()


class TestReverseInteger(unittest.TestCase):

    def test_1(self):
        self.assertEqual(SOLUTION.reverse(123), 321)

    def test_2(self):
        self.assertEqual(SOLUTION.reverse(-123), -321)

    def test_3(self):
        self.assertEqual(SOLUTION.reverse(120), 21)


if __name__ == '__main__':
    unittest.main()
