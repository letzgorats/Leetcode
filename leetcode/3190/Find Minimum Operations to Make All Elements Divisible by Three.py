# solution 1 - (array,math) - (0ms) - (2025.11.22)
from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        cnt = 0
        for num in nums:
            if num % 3 != 0:
                cnt += 1

        return cnt