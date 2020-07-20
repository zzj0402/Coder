import math


class Solution:
    def getMinDistSum(self, positions) -> float:
        result = 0
        x = 0
        y = 0
        # list formula then calc the min val of it
        for i in range(len(positions)):
            result += (positions[i][0] - x) ** 2 + (positions[i][1] - y) ** 2

        return math.sqrt(result)
