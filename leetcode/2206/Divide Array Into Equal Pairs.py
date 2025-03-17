# solution 1 - hash table - (2ms) - (2025.03.17)
from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        nums_to_freq = Counter(nums)

        for k, v in nums_to_freq.items():

            if v % 2 != 0:
                return False

        return True