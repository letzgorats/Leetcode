class Solution:
    def minDays(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        def dfs(r, c, visit):

            if r < 0 or c < 0 or r >= n or c >= m or grid[r][c] == 0 or (r, c) in visit:
                return

            visit.add((r, c))
            dfs(r - 1, c, visit)
            dfs(r + 1, c, visit)
            dfs(r, c - 1, visit)
            dfs(r, c + 1, visit)

        def count_islands():

            visit = set()
            count = 0
            for i in range(n):
                for j in range(m):
                    if grid[i][j] and (i, j) not in visit:
                        dfs(i, j, visit)
                        count += 1

            return count

        if count_islands() != 1:
            return 0

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    if count_islands() != 1:
                        return 1
                    grid[r][c] = 1

        return 2