class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:

        n = len(grid)
        cnt = 0

        scale_grid = [[0] * 3 * n for i in range(3 * n)]

        for i in range(n):
            for j in range(n):

                if grid[i][j] == '/':
                    scale_grid[i * 3][j * 3 + 2] = 1
                    scale_grid[i * 3 + 1][j * 3 + 1] = 1
                    scale_grid[i * 3 + 2][j * 3] = 1

                elif grid[i][j] == '\\':
                    scale_grid[i * 3][j * 3] = 1
                    scale_grid[i * 3 + 1][j * 3 + 1] = 1
                    scale_grid[i * 3 + 2][j * 3 + 2] = 1

        # print(scale_grid)
        def dfs(i, j):
            if 0 > i or i >= len(scale_grid) or j < 0 or j >= len(scale_grid) or scale_grid[i][j] != 0:
                return 0

            scale_grid[i][j] = 1
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            return 1

        for i in range(3 * n):
            for j in range(3 * n):
                if scale_grid[i][j] == 0:
                    cnt += dfs(i, j)

        return cnt
