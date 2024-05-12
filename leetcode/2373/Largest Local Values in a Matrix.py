class Solution(object):
    def largestLocal(self, grid):

        n = len(grid)
        max_grid = [[0] * (n-2) for _ in range(n-2)]

        def check_max(r,c):
            max_val = 1
            for i in range(r,r+3):
                for j in range(c,c+3):
                    max_val = max(grid[i][j],max_val)

            return max_val

        for i in range(n-2):
            for j in range(n-2):
                max_grid[i][j] = check_max(i,j)

        return max_grid


class Solution(object):
    def largestLocal(self, grid):

        n = len(grid)
        max_grid = [[0] * (n-2) for _ in range(n-2)]
     
        for i in range(n-2):
            for j in range(n-2):
                max_grid[i][j] = max(grid[i][j:j+3] + grid[i+1][j:j+3]+grid[i+2][j:j+3])

        return max_grid
