# solution 1 - O(n)
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        total_ones = nums.count(1)
        nums = nums + nums

        current_ones = nums[:total_ones].count(1)
        max_ones_in_window = current_ones

        for i in range(1, n):

            if nums[i - 1] == 1:
                current_ones -= 1
            if nums[i + total_ones - 1] == 1:
                current_ones += 1
            max_ones_in_window = max(max_ones_in_window, current_ones)

        return total_ones - max_ones_in_window

# solution 2 - O(n)
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n = len(nums)
        total_ones = nums.count(1)
        l = 0
        window_ones = max_window_ones = 0

        for r in range(2 * n):
            if nums[r % n] == 1:
                window_ones += 1
            if r - l + 1 > total_ones:
                window_ones -= nums[l % n]
                l += 1
            max_window_ones = max(max_window_ones, window_ones)

        return total_ones - max_window_ones




