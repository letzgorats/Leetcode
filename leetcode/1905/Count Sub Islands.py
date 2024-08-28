from collections import deque


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        n, m = len(grid2), len(grid2[0])
        answer = 0

        def bfs(r, c):

            grid2[r][c] = 0
            q = deque([(r, c)])

            while q:
                r, c = q.popleft()
                grid2[r][c] = 0
                for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in tmp and grid2[nr][nc] == 1:
                        tmp.add((nr, nc))
                        q.append((nr, nc))

            return tmp

        def check(candi):

            while candi:
                r, c = candi.pop()
                if grid1[r][c] == 0:
                    return False

            return True

        for i in range(n):
            for j in range(m):
                tmp = set()
                if grid2[i][j] == 1:
                    tmp.add((i, j))
                    tmp = bfs(i, j)
                    if check(tmp):
                        answer += 1

        return answer
