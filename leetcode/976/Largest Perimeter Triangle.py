# solution 1 - (sort,greedy) - (15ms) - (2025.09.28)
from typing import List
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        # [2,3,3,4]
        largest = len(nums) - 1

        while largest >= 2:
            if nums[largest - 2] + nums[largest - 1] > nums[largest]:
                return nums[largest - 2] + nums[largest - 1] + nums[largest]
            largest -= 1

        return 0

# Wrong answer
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        # [1,1,2,10]
        ans = 0
        smallest = 0
        largest = len(nums) - 1

        while smallest < largest - 1:
            if nums[smallest + 1] + nums[smallest] > nums[largest]:
                ans = max(ans, nums[smallest + 1] + nums[smallest] + nums[largest])
                largest -= 1
            else:
                smallest += 1

        return ans