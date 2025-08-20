# solution 1 - dfs, cache - 206ms, 37.4mb
from typing import List
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


# solution 5 - (dp,dfs) - (276ms) - (2025.08.20)
'''
기준이 현재 cell 이 top-left 일 때
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        # maximal square 문제 먼저 풀고 이 문제 풀면 이해 잘됨.
        # https://youtu.be/6X7Ha2PrDmM?si=VLkUZbvXfJRGi5-X
        # -> 이해 완료

        rows = len(matrix)
        cols = len(matrix[0])
        cache = defaultdict(int)

        # 기준 : 현재 셀이 top-left-cell 일 때
        def helper(r, c):

            if r >= rows or c >= cols or matrix[r][c] == 0:
                return 0

            if (r, c) not in cache:

                cache[(r, c)] = 0
                if matrix[r][c] == 1:
                    cache[(r, c)] = 1 + min(
                        helper(r + 1, c),
                        helper(r + 1, c + 1),
                        helper(r, c + 1)
                    )
            return cache[(r, c)]

        answer = 0
        for r in range(rows):
            for c in range(cols):
                answer += helper(r, c)

        print(cache)

        return answer

# solution 5 - (dp,dfs) - (66ms) - (2025.08.20)
'''
기준이 현재 cell 이 bottom-right 일 때
'''
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:

        # maximal square 문제 먼저 풀고 이 문제 풀면 이해 잘됨.
        # https://youtu.be/6X7Ha2PrDmM?si=VLkUZbvXfJRGi5-X
        # -> 이해 완료

        # 기준 : 현재 셀이 down-bottom-cell 일 때
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        # print(dp)

        answer = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] > 0:
                    dp[i + 1][j + 1] = 1 + min(dp[i + 1][j], dp[i][j], dp[i][j + 1])
                    answer += dp[i + 1][j + 1]

        print(dp)
        return answer
