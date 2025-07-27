# solution 1 - (greedy) - (0ms) - (2025.07.27)
from typing import List
class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        hills = 0
        valleys = 0

        if len(nums) <= 2:
            return 0

        refined = []
        for i in range(len(nums)):
            if refined and refined[-1] == nums[i]:
                continue
            refined.append(nums[i])

        left = refined[0]
        for i in range(1, len(refined) - 1):
            if left < refined[i] and refined[i] > refined[i + 1]:
                hills += 1
                left = refined[i]
            elif left > refined[i] and refined[i] < refined[i + 1]:
                valleys += 1
                left = refined[i]

        return hills + valleys