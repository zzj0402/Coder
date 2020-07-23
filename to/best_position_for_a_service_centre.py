import math

min_delta = 10 ** -5


class Solution:
    def getMinDistSum(self, positions) -> float:
        def get_dist(x, y):
            dist_result = 0
            for i, j in positions:
                dist_result += (x - i) ** 2 + (y - j) ** 2
            return math.sqrt(dist_result)

        def get_initial_x_y():
            y_init = x_init = 0
            for i, j in positions:
                x_init += i
                y_init += j
            return x_init / len(positions), y_init / len(positions)

        x, y = get_initial_x_y()
        step = 1
        curr_dist = get_dist(x, y)
        while step >= min_delta:
            flag_to_division = True
            for delta_x, delta_y in [(0, step), (0, -step), (step, 0), (-step, 0)]:
                tmp_x = x + delta_x
                tmp_y = y + delta_y
                tmp_dist = get_dist(tmp_x, tmp_y)
                if tmp_dist < curr_dist:
                    # if the result is getting closer to the answer, not necessary to shorten the step
                    flag_to_division = False
                    curr_dist = tmp_dist
                    x = tmp_x
                    y = tmp_y

            if flag_to_division:
                step /= 10  # division by 10
        return curr_dist
