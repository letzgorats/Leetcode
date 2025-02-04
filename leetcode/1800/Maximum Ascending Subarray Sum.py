class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        current = nums[0]
        max_sum = max(nums)

        for idx in range(1, len(nums)):

            if nums[idx - 1] < nums[idx]:
                current += nums[idx]

            else:
                current = nums[idx]

            max_sum = max(max_sum, current)

        return max_sum

