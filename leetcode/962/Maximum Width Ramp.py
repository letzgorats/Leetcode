class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        stack = []
        max_ramp = 0

        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)

        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_ramp = max(max_ramp, j - i)

        return max_ramp