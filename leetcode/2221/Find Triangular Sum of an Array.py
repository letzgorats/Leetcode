# solution 1 - (array,math,simulation,copy) - (1267ms) - (2025.09.30)
from typing import List
class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        while len(nums) != 1:

            new_nums = []
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)

            nums = new_nums[:]

        return nums[0]