class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums.sort()
        num_set = set(nums)
        max_length = 0
        for num in nums:
            length = 0
            while num in num_set:
                length += 1
                num = num ** 2

            max_length = max(max_length, length)

            if max_length == 5:
                return 5

        return max_length if max_length >= 2 else -1