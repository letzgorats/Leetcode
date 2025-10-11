# solution 1 - (dynamic programming) - (411ms) - (2025.10.11)
from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:

        freq = Counter(power)
        vals = sorted(freq)

        gain = [v * freq[v] for v in vals]  # 해당 데미지를 선택하면 얻는 총합

        n = len(vals)
        dp = [0] * n

        # 투포인터로 "같이 고를 수 있는 마지막 인덱스 p" 유지
        # "함께 선택 가능한 가장 오른쪽 인덱스 p"
        p = -1
        for i in range(n):

            while p + 1 < i and vals[i] - vals[p + 1] >= 3:
                p += 1
            # i를 고른 경우
            take = gain[i] + (dp[p] if p >= 0 else 0)
            # i를 스킵한 경우
            skip = dp[i - 1] if i > 0 else 0
            dp[i] = max(skip, take)

        return dp[-1]

