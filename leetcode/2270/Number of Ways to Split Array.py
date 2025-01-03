# solution 1 - prefix,suffix
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        n = len(nums)
        prefix = [0] * (n + 1)

        for i, num in enumerate(nums, 1):
            prefix[i] = prefix[i - 1] + num

        suffix = [0] * (n + 1)
        for i, num in enumerate(nums[::-1], 1):
            suffix[i] = suffix[i - 1] + num

        valid = 0
        for i in range(1, n):

            if prefix[i] >= suffix[n - i]:
                valid += 1

        return valid

# solution 2 - more concise solution
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        right_sum = sum(nums)
        left_sum = 0

        valid = 0
        for i in range(len(nums) - 1):
            right_sum -= nums[i]
            left_sum += nums[i]
            if right_sum <= left_sum:
                valid += 1

        return valid