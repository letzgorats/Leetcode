# solution 1 - (greedy) - (0ms) - (2025.12.05)
from typing import List
class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        right = sum(nums)
        left = 0
        ans = 0
        for i in range(len(nums) - 1):

            right -= nums[i]
            left += nums[i]
            # print(left,right)
            if (right - left) % 2 == 0:
                ans += 1

        return ans

# solution 2 - (math) - (0ms) - (2025.12.05)
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0

# odd +- odd = odd
# even += even = even