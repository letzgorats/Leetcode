# solution 1 - (binary search) - (1495ms) - (2025.10.15)
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:

        def is_valid(window):

            for i in range(0, n - 2 * window + 1):

                if inc[i + window - 1] >= window and inc[i + 2 * window - 1] >= window:
                    return True

            return False

        n = len(nums)
        inc = [1] * n
        for i in range(1, n):
            inc[i] = inc[i - 1] + 1 if nums[i - 1] < nums[i] else 1

        # print(inc)

        left = 0
        right = n // 2
        ans = 0
        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                left = mid + 1
                ans = max(ans, mid)
            else:
                right = mid - 1

        return ans