# solution 1 - bfs,heapq
import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        answer = 0
        dr = [0, 0, 1, -1]  # 우,좌,하,상
        dc = [1, -1, 0, 0]
        visited = [[float('inf')] * m for _ in range(n)]
        q = []
        heapq.heappush(q, (0, 0, 0))
        while q:
            cnt, curr, curc = heapq.heappop(q)

            if (curr, curc) == (n - 1, m - 1):
                return cnt

            if cnt >= visited[curr][curc]:
                continue

            visited[curr][curc] = cnt

            for i in range(4):
                nr = curr + dr[i]
                nc = curc + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    new_cnt = cnt if i + 1 == grid[curr][curc] else cnt + 1
                    if new_cnt < visited[nr][nc]:
                        heapq.heappush(q, (new_cnt, nr, nc))

from collections import defaultdict,deque
# solution 2 - bfs,defaultdict,deque
from collections import defaultdict
import heapq


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        direction = {
            1: [0, 1],  # [r,c]
            2: [0, -1],  # [r,c]
            3: [1, 0],  # [r,c]
            4: [-1, 0],  # [r,c]
        }

        ROWS, COLS = len(grid), len(grid[0])
        q = deque([(0, 0, 0)])  # r,c,cost
        min_cost = {(0, 0): 0}  # (r,c) -> min cost

        while q:

            r, c, cost = q.popleft()
            if (r, c) == (ROWS - 1, COLS - 1):
                return cost

            for d in direction:
                dr, dc = direction[d]
                nr, nc = r + dr, c + dc
                n_cost = cost if d == grid[r][c] else cost + 1
                if (
                        nr < 0 or nc < 0 or
                        nr == ROWS or nc == COLS or
                        n_cost >= min_cost.get((nr, nc), float("inf"))
                ):
                    continue

                min_cost[(nr, nc)] = n_cost
                if d == grid[r][c]:
                    q.appendleft((nr, nc, n_cost))
                else:
                    q.append((nr, nc, n_cost))