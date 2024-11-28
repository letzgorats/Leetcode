import heapq
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        def dijkstra(r, c, obstacle):

            q = []
            heapq.heappush(q, (0, r, c))  # obstacle,pos
            dr = [-1, 0, 1, 0]  # up, right, down, left
            dc = [0, 1, 0, -1]
            visit = set()
            visit.add((r, c))
            while q:

                obstacle, r, c = heapq.heappop(q)
                if (r, c) == (n - 1, m - 1):
                    return obstacle
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m:
                        if (nr, nc) not in visit:
                            if grid[nr][nc] == 1:
                                heapq.heappush(q, (obstacle + 1, nr, nc))
                            else:
                                heapq.heappush(q, (obstacle, nr, nc))

                            visit.add((nr, nc))

        return dijkstra(0, 0, 0)
