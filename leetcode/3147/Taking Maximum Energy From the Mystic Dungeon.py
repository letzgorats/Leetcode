# solution 1 - (prefix sum,dp) - (1138ms) - (2025.10.10)
from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        dp = [e for e in energy]

        for i in range(len(dp) - 1, -1, -1):

            if 0 <= i + k < len(dp):
                dp[i] += dp[i + k]

                # print(dp)

        return max(dp)