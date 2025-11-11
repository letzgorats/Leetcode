# solution 1 - (backtracking,lru_cache) - (1162ms) - (2025.11.11)
from functools import lru_cache
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        zeros_ones = [(s.count('0'), s.count('1')) for s in strs]

        @lru_cache(None)
        def backtrack(mcnt, ncnt, idx):

            if idx == len(strs):
                return 0

            zeros, ones = zeros_ones[idx]

            # skip
            skip = backtrack(mcnt, ncnt, idx + 1)

            # select
            select = 0
            if mcnt >= zeros and ncnt >= ones:
                select = 1 + backtrack(mcnt - zeros, ncnt - ones, idx + 1)

            return max(skip, select)

        return backtrack(m, n, 0)

# solution 2 - (knapsack) - (1565ms) - (2025.11.11)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            # 뒤에서부터 업데이트해야 중복 계산 안 생김
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]


'''
dp[i][j] : 0 이 i개, 1이 j개까지 사용할 수 있을 때 만들 수 있는 최대 문자열 수
각 문자열을 한 번씩만 사용해야 하므로 (0/1 knapsack 처럼)
'''

# TLE
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        max_val = 0

        def backtrack(mcnt, ncnt, idx, tmp):
            nonlocal max_val
            if mcnt > m or ncnt > n:
                return

            if idx == len(strs):
                max_val = max(max_val, tmp)
                return

                # select
            backtrack(mcnt + strs[idx].count('0'), ncnt + strs[idx].count('1'), idx + 1, tmp + 1)
            # skip
            backtrack(mcnt, ncnt, idx + 1, tmp)

        backtrack(0, 0, 0, 0)

        return max_val