# solution1 - subarray,prefix - (127ms) - (2025.04.28)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        prefix = 0
        left = 0
        answer = 0

        for r in range(len(nums)):

            prefix += nums[r]

            while (r - left + 1) * prefix >= k:
                prefix -= nums[left]
                left += 1

            answer += (r - left + 10)

        return answer