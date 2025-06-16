# solution 1 - (O(n),min,max) - (1ms) - (2025.06.16)
from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        diff = -1
        n = len(nums)
        minimum_value = nums[0]
        for i in range(1, n):

            if minimum_value < nums[i]:
                diff = max(diff, nums[i] - minimum_value)

            if minimum_value > nums[i]:
                minimum_value = nums[i]

        return diff

# solution 2 - (O(n^2)) - (286ms) - (2025.06.16)
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                ans = max(nums[j] - nums[i], ans)

        return -1 if ans == 0 else ans


