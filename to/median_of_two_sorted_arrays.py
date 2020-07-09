from math import floor, ceil


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total_length = len(nums1)+len(nums2)
        mod = total_length % 2
        arranged_nums = []
        index_left = 0
        index_right = 0
        while index_left < len(nums1) and index_right < len(nums2):
            left = nums1[index_left]
            right = nums2[index_right]
            if left < right:
                arranged_nums.append(left)
                index_left += 1
                if index_left == len(nums1):
                    arranged_nums.append(right)
            else:
                arranged_nums.append(right)
                index_right += 1
            if mod == 0:
                print(arranged_nums)

                if len(arranged_nums) > total_length/2:
                    return arranged_nums[-1]/2+arranged_nums[-2]/2
            else:
                if len(arranged_nums) > total_length/2:
                    return arranged_nums[-1]
