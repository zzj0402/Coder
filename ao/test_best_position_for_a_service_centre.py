import unittest
from to.best_position_for_a_service_centre import Solution

SOLUTION = Solution()


class TestServiceCenter(unittest.TestCase):
    """
    testcases come from https://leetcode.com/problems/best-position-for-a-service-centre/description/
    """

    def assert_equal_with_precision(self, n1, n2):
        self.assertEqual(abs(n1 - n2) < 10 ** -5, True)

    def test_eg1(self):
        self.assert_equal_with_precision(SOLUTION.getMinDistSum([[0,1],[1,0],[1,2],[2,1]]), 4.00000)

    def test_eg2(self):
        self.assert_equal_with_precision(SOLUTION.getMinDistSum([[1,1],[3,3]]), 2.82843)

    def test_eg3(self):
        self.assert_equal_with_precision(SOLUTION.getMinDistSum([[1,1]]), 0.00000)

    def test_eg4(self):
        self.assert_equal_with_precision(SOLUTION.getMinDistSum([[1,1],[0,0],[2,0]]),  2.73205)

    def test_eg5(self):
        self.assert_equal_with_precision(SOLUTION.getMinDistSum([[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]), 32.94036)

    def test_complement1(self):
        self.assert_equal_with_precision(SOLUTION.getMinDistSum([[4,4],[52,89],[76,60],[4,4],[4,4],[93,59],[50,92],[4,4],[76,14],[4,4],[46,41],[4,4],[4,4],[4,4],[4,4],[67,14],[73,71],[83,44],[4,4],[4,4],[4,4],[4,4],[30,29],[74,77],[4,4],[4,4],[4,4],[26,62],[4,4],[4,4],[50,30],[44,93]]), 1119.58582)


if __name__ == '__main__':
    unittest.main()
