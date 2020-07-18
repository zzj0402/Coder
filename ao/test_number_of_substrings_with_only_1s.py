import unittest
from to.number_of_substrings_with_only_1s import Solution

SOLUTION = Solution()


class TestStringMethods(unittest.TestCase):

    def test_always_true(self):
        self.assertEqual(True, True)

    def test_eg1(self):
        self.assertEqual(SOLUTION.numSub('0110111'), 9)

    def test_eg2(self):
        self.assertEqual(SOLUTION.numSub('101'), 2)

    def test_eg3(self):
        self.assertEqual(SOLUTION.numSub('111111'), 21)

    def test_eg4(self):
        self.assertEqual(SOLUTION.numSub('000'), 0)


if __name__ == '__main__':
    unittest.main()
