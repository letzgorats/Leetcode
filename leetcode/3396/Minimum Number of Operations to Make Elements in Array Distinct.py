# solution 1 - brute force, O(n^2) - 3ms - (2025.04.08)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        while len(set(nums)) != len(nums):
            nums = nums[3:]
            answer += 1

        return answer

# solution 2 - hash table, greedy, bottom up, index, O(n) - 0ms - (2025.04.08)
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0

