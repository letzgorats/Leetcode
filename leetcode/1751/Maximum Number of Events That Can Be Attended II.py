# solution 1 - (dp+binary search) - (1050ms) - (2025.07.08)
from functools import lru_cache
import bisect
from typing import List
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [e[0] for e in events]

        @lru_cache(None)
        def dp(i, remaining):
            if i == len(events) or remaining == 0:
                return 0

            # skip
            skip = dp(i + 1, remaining)
            # take
            j = bisect.bisect_right(starts, events[i][1])  # 다음 가능한 이벤트 인덱스
            take = events[i][2] + dp(j, remaining - 1)

            return max(skip, take)

        return dp(0, k)
