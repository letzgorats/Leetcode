# solution 1 - (max,diff) - (2ms) - (2025.06.12)
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        ans = abs(nums[0] - nums[-1])
        for i in range(1, len(nums)):
            ans = max(abs(nums[i] - nums[i - 1]), ans)

        return ans

