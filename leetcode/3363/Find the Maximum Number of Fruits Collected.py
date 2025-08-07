# solution 1 - (dp,cache,zip,math) - (1214ms) - (2025.08.07)
from functools import lru_cache
from typing import List
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(row, col):

            if 0 <= col < row < n:
                return fruits[row][col] + max(
                    dp(row - 1, col + 1),
                    dp(row, col + 1),
                    dp(row + 1, col + 1)
                )
            return 0

        # n-1 steps limit !!
        n = len(fruits)
        child1 = 0
        for i in range(n):
            child1 += fruits[i][i]

        child2 = dp(n - 1, 0)

        dp.cache_clear()
        fruits = list(zip(*fruits))

        child3 = dp(n - 1, 0)

        return child1 + child2 + child3


