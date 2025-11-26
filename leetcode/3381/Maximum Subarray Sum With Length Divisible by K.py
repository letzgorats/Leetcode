# solution 1 - (prefix sum,) - (320ms) - (2025.11.27)
from collections import defaultdict
from typing import List
import math
class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        hash_table = defaultdict(int)

        min_sum = [math.inf] * (k - 1) + [0]
        prefix, ans = 0, -math.inf
        for i, x in enumerate(nums):
            prefix += x
            ik = i % k
            ans = max(ans, prefix - min_sum[ik])
            min_sum[ik] = min(prefix, min_sum[ik])
            # print(min_sum,ans)

        return ans

