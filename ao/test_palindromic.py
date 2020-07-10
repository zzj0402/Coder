import unittest
from to.palindromic import Solution


class TestPalindromic(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
