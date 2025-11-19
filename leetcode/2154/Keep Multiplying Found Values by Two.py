# solution 1 - (greedy) - (0ms) - (2025.11.19)
class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """

        while original in nums:
            original *= 2

        return original
