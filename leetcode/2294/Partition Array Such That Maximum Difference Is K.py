# solution 1 - (greedy,sorting) - (133ms) - (2025.06.20)
from typing import List
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        # print(nums)
        min_val = nums[0]
        ans = 1
        for i in range(1, len(nums)):

            if nums[i] - min_val <= k:
                min_val = min(nums[i], min_val)
            else:
                ans += 1
                min_val = nums[i]

        return ans
