from math import floor, ceil


class Solution:
    def getMean(self, nums):
        if len(nums) % 2 == 0:
            print("Even")
            print(len(nums))
            index_1 = floor(len(nums)/2)-1
            print("index_1")
            print(index_1)

            index_2 = ceil(len(nums)/2)-1
            mean = nums[index_1]/2+nums[index_2]/2
            print(mean)
        else:
            mean = nums[int(len(nums)/2)]
        return mean

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        print(self.getMean(nums1))
        return self.getMean(nums1)/2 + self.getMean(nums2)/2
