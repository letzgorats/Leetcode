# solution 1 - dfs, cache - 206ms, 37.4mb
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        cache = {}

        def dfs(r, c):
            if r == rows or c == cols or not matrix[r][c]:
                return 0

            if (r, c) in cache:
                return cache[(r, c)]

            cache[(r, c)] = 1 + min(
                dfs(r + 1, c),
                dfs(r, c + 1),
                dfs(r + 1, c + 1)
            )

            return cache[(r, c)]

        res = 0
        for r in range(rows):
            for c in range(cols):
                res += dfs(r, c)

        return res

# solution 2 - dp, dict - 156ms, 28.60mb
from collections import defaultdict
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        dp = defaultdict(int)

        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    dp[(r, c)] = 1 + min(
                        dp[(r - 1, c)],
                        dp[(r, c - 1)],
                        dp[(r - 1, c - 1)]
                    )
                cnt += dp[(r, c)]

        return cnt

# solution 3 - dp - 52ms,19.4mb
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                    cnt += dp[r][c]

        return cnt

# solution 4 - dp, cache - 71ms, 19.24mb
from collections import defaultdict
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        dp = defaultdict(int)

        cnt = 0
        for r in range(rows):
            cur_dp = defaultdict(int)
            for c in range(cols):
                if matrix[r][c] == 1:
                    cur_dp[c] = 1 + min(
                        dp[c],
                        cur_dp[c - 1],
                        dp[c - 1]
                    )
                    cnt += cur_dp[c]
            dp = cur_dp

        return cnt
