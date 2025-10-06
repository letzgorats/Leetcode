# solution 1 - (heapq,dijkstra) - (38ms) - (2025.10.06)
import heapq
from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
        pq = [(grid[0][0], 0, 0)]
        seen = set()

        while pq:
            max_d, r, c = heapq.heappop(pq)
            if (r, c) in seen:
                continue

            seen.add((r, c))
            if r == n - 1 and c == n - 1:
                return max_d

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen:
                    new_d = max(max_d, grid[nr][nc])
                    heapq.heappush(pq, (new_d, nr, nc))

        return -1

# wrong answer
from collections import deque
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        def bfs(r, c):

            q = deque([(r, c)])
            visited = set()
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                moveTo = deque([])
                minVal = 2500
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if 0 <= nr < n and 0 <= nc < m and ((nr, nc) not in visited):
                        visited.add((nr, nc))
                        if minVal > grid[nr][nc]:
                            minVal = grid[nr][nc]
                            moveTo = deque([])
                            moveTo.append(d)
                        elif minVal == grid[nr][nc]:
                            moveTo.append(d)
                # print(moveTo)
                while moveTo:
                    dr, dc = moveTo.popleft()
                    q.append((r + dr, c + dc))
                    if grid[r][c] >= grid[r + dr][c + dc]:
                        grid[r + dr][c + dc] = grid[r][c]
                    else:
                        grid[r + dr][c + dc] = minVal

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up,right,down,left
        bfs(0, 0)
        # print(grid)

        return grid[n - 1][n - 1]
