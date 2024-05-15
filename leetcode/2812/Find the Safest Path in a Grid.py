from heapq import heappush, heappop


class Solution(object):
    def maximumSafenessFactor(self, grid):

        N, M = len(grid), len(grid[0])

        # Step 1. Find all thieves
        cells_to_check = []
        for i in range(N):
            for j in range(M):
                if grid[i][j]:
                    cells_to_check.append((i, j, 1))

        # Step 2. Use BFS to calculate safety factor for each cell (increased by 1 - that will be controlled later)
        while cells_to_check:
            x, y, w = cells_to_check.pop(0)
            for next_x, next_y in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
                if 0 <= next_x < N and 0 <= next_y < M and (grid[next_x][next_y] == 0 or grid[next_x][next_y] > w + 1):
                    grid[next_x][next_y] = w + 1
                    cells_to_check.append((next_x, next_y, w + 1))

        # Step 3. Traverse the grid, on each iteration pick the cell with the best metrics using Heap
        # (the one with the greatest safety factor)
        s_factor, x, y = grid[0][0], 0, 0
        heap = [(-s_factor, x, y)]

        while not (x == N - 1 and y == M - 1):
            s_factor, x, y = heappop(heap)
            s_factor *= -1
            for next_x, next_y in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
                if 0 <= next_x < N and 0 <= next_y < M and (grid[next_x][next_y] != -1):
                    heappush(heap, (-min(s_factor, grid[next_x][next_y]), next_x, next_y))
                    grid[next_x][next_y] = -1

        return s_factor - 1
