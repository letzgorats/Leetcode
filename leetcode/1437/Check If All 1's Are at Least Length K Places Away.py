# solution 1 - (greedy) - (11ms) - (2025.11.17)
from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        pre = -1
        diff = 0
        for idx, num in enumerate(nums):

            if num == 1:
                if pre != -1:
                    diff = idx - pre - 1
                    if diff < k:
                        return False
                pre = idx

        return True