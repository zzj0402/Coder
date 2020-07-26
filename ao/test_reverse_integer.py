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

    def test_overflow(self):
        self.assertEqual(SOLUTION.reverse(1534236469), 0)

    def test_underflow(self):
        self.assertEqual(SOLUTION.reverse(-2147483648), 0)


if __name__ == '__main__':
    unittest.main()
