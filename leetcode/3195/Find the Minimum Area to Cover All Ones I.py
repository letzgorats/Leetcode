# solution 1 - (matrix,greedy,array) - (2703ms) - (2025.08.22)
from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        top, down = 0, n - 1
        left, right = 0, m - 1
        for i in range(n):
            if sum(grid[i]) != 0:
                top = i
                break
        for i in range(n - 1, -1, -1):
            if sum(grid[i]) != 0:
                down = i
                break

        # transpose
        col_grid = list(map(list, zip(*grid)))

        for j in range(m):
            if sum(col_grid[j]) != 0:
                left = j
                break

        for j in range(m - 1, -1, -1):
            if sum(col_grid[j]) != 0:
                right = j
                break

        return (down - top + 1) * (right - left + 1)

# solution 2 - (min,max) - (2972ms) - (2025.08.22)
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        top, down = n - 1, 0
        left, right = m - 1, 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    top = min(i, top)
                    left = min(j, left)
                    right = max(j, right)
                    down = max(i, down)

        return (down - top + 1) * (right - left + 1)