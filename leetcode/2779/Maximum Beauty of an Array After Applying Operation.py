class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

        nums.sort()  # [1,2,4,6]

        max_beauty = 0
        start = 0
        for end in range(len(nums)):

            # while nums[end] - k > nums[start] + k:
            while nums[end] - nums[start] > 2 * k:
                start += 1

            max_beauty = max(max_beauty, end - start + 1)

        return max_beauty