# solution 1 - (sorting,two pointers) - (487ms) - (2025.09.26)
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        ans = 0
        nums.sort()
        n = len(nums)

        for i in range(n - 1, -1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans