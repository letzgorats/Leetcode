# solution 1 - binary search - (0ms) - (2025.03.12)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        def lower_bound(nums):

            start, end = 0, len(nums) - 1
            index = len(nums)

            while start <= end:

                mid = (start + end) // 2

                if nums[mid] < 0:
                    start = mid + 1
                else:
                    end = mid - 1
                    index = mid

            return index

        def upper_bound(nums):

            start, end = 0, len(nums) - 1
            index = len(nums)

            while start <= end:

                mid = (start + end) // 2

                if nums[mid] <= 0:
                    start = mid + 1
                else:
                    end = mid - 1
                    index = mid

            return index

        positiveCount = len(nums) - upper_bound(nums)
        negativeCount = lower_bound(nums)

        return max(positiveCount, negativeCount)

# solution 2 - binary search - (0ms) - (2025.03.12)
from bisect import bisect_right,bisect_left
class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        negativeCount = bisect_left(nums,0)
        positiveCount = len(nums) - bisect_left(nums,1)

        return max(negativeCount,positiveCount)


# solution 3 - greedy - (0ms) - (2025.03.12)
class Solution:
    def maximumCount(self, nums: List[int]) -> int:

        pos, neg = 0, 0
        for num in nums:

            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1

        return max(pos, neg)