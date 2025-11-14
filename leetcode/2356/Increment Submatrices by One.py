# solution 1 - (2D Prefix Sum + Difference Array) - (184ms) - (2025.11.14)
from typing import List
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        grid = [[0] * (n + 1) for _ in range(n + 1)]

        for r1, c1, r2, c2 in queries:

            grid[r1][c1] += 1

            if c2 + 1 < n:
                grid[r1][c2 + 1] -= 1
            if r2 + 1 < n:
                grid[r2 + 1][c1] -= 1
            if r2 + 1 < n and c2 + 1 < n:
                grid[r2 + 1][c2 + 1] += 1

        # Prefix sum row-wise
        for r in range(n):
            for c in range(1, n):
                grid[r][c] += grid[r][c - 1]

        # Prefix sum col-wise
        for c in range(n):
            for r in range(1, n):
                grid[r][c] += grid[r - 1][c]

        # Trim to n x n
        return [row[:n] for row in grid[:n]]


# TLE
class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        grid = [[0] * n for _ in range(n)]

        def fill(topr, topc, bottomr, bottomc):

            for r in range(topr, bottomr + 1):
                for c in range(topc, bottomc + 1):
                    grid[r][c] += 1

        for q in queries:
            fill(q[0], q[1], q[2], q[3])

        # print(grid)

        return grid