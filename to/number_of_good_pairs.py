class Solution:
    def numIdenticalPairs(self, nums) -> int:
        result = 0
        for i, val in enumerate(nums):
            for j in range(0, i):
                if nums[i] == nums[j]:
                    result += 1
        return result
