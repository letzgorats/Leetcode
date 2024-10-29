# solution 1 - dp, memoization
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        dp = [[-1] * m for _ in range(n)]

        def traversal(r, c):

            # 이미 계산된 위치라면, dp 값 재활용
            if dp[r][c] != -1:
                return dp[r][c]

            res = 0
            if r - 1 >= 0 and c + 1 < m and grid[r - 1][c + 1] > grid[r][c]:
                res = max(res, traversal(r - 1, c + 1) + 1)
            if c + 1 < m and grid[r][c + 1] > grid[r][c]:
                res = max(res, traversal(r, c + 1) + 1)
            if r + 1 < n and c + 1 < m and grid[r + 1][c + 1] > grid[r][c]:
                res = max(res, traversal(r + 1, c + 1) + 1)

            dp[r][c] = res
            return res

        max_cnt = 0
        for i in range(n):
            max_cnt = max(max_cnt, traversal(i, 0))

        return max_cnt

# solution 2 - dfs, TLE
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        def traversal(r, c, cnt):
            cur_val = grid[r][c]
            curr, curc = r, c
            if r < 0 or r >= n or c < 0 or c >= m:
                return cnt

            res = cnt
            if 0 <= curr - 1 and curc + 1 < m and cur_val < grid[curr - 1][curc + 1]:
                res = max(res, traversal(curr - 1, curc + 1, cnt + 1))
            if curc + 1 < m and cur_val < grid[curr][curc + 1]:
                res = max(res, traversal(curr, curc + 1, cnt + 1))
            if curr + 1 < n and curc + 1 < m and cur_val < grid[r + 1][c + 1]:
                res = max(res, traversal(curr + 1, curc + 1, cnt + 1))

            return res

        max_cnt = 0
        for i in range(n):
            max_cnt = max(max_cnt, traversal(i, 0, 0))

        return max_cnt