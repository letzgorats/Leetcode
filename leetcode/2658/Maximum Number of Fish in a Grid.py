# solution 1 - bfs, global, land
from collections import deque
from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        land = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    land.add((i, j))

        dr = [0, 1, 0, -1]  # 우, 하, 좌, 상
        dc = [1, 0, -1, 0]
        global answer
        answer = 0

        def traversal(r, c):
           global answer

            q = deque([(r, c)])
            tmp = grid[r][c]
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] > 0:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        tmp += grid[nr][nc]

            answer = max(answer, tmp)

        visited = set()
        for r, c in land:
            # print("r,c=",r,c)
            if (r, c) not in visited:
                traversal(r, c)
            # print(answer)

        return answer


# solution 2 - bfs, nonlocal, land x
from collections import deque
from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        dr = [0, 1, 0, -1]  # 우, 하, 좌, 상
        dc = [1, 0, -1, 0]
        visited = set()
        answer = 0


        def traversal(r, c):
            nonlocal answer
            q = deque([(r, c)])
            tmp = grid[r][c]
            visited.add((r, c))

            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] > 0:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        tmp += grid[nr][nc]

            answer = max(answer, tmp)

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and (i,j) not in visited:
                    traversal(i,j)

        return answer


