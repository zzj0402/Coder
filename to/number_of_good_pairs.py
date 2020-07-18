class Solution:
    @staticmethod
    def find_num_of_good_pairs(nums_list) -> int:
        result = 0
        for i, val in enumerate(nums_list):
            for j in range(0, i):
                if nums_list[i] == nums_list[j]:
                    result += 1
        return result
