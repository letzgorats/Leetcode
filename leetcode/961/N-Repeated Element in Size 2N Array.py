# solution 1 - (counter,hash table) - (0ms) - (2026.01.02)
from typing import List
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)

        return nums[-1]

# solution 2 - (counter,hash table) - (4ms) - (2026.01.02)
from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        cnt = Counter(nums)
        for k, v in cnt.items():
            if v != 1:
                return k