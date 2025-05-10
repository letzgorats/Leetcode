# solution 1 - (array,max) - (865ms) - (2025.05.10)
from typing import List
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        total_nums1 = 0
        total_nums2 = 0

        zero_cnt1 = 0
        zero_cnt2 = 0

        for i in nums1:

            total_nums1 += i
            if i == 0:
                total_nums1 += 1
                zero_cnt1 += 1

        for i in nums2:

            total_nums2 += i
            if i == 0:
                total_nums2 += 1
                zero_cnt2 += 1

        if (zero_cnt1 == 0 and total_nums2 > total_nums1) or (zero_cnt2 == 0 and total_nums2 < total_nums1):
            return -1

        return max(total_nums1, total_nums2)

