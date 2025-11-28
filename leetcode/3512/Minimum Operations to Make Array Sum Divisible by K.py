# soluition 1 - (array,math) - (4ms) - (2025.11.29)
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        S = sum(nums)
        return 0 if S % k == 0 else S % k