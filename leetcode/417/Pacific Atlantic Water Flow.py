# solution 1 - (bfs) - (2609ms) - (2025.10.05)
from collections import deque
from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def flow_both(r, c):

            q = deque([(r, c)])
            visited = set()
            visited.add((r, c))
            pacific = False
            atlantic = False
            while q:
                r, c = q.popleft()
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if 0 <= nr < n and 0 <= nc < m:
                        if heights[nr][nc] <= heights[r][c] and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                    elif nr == -1 or nc == -1:
                        pacific = True
                    elif nr == n or nc == m:
                        atlantic = True

            if pacific and atlantic:
                return True
            return False

        n = len(heights)
        m = len(heights[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up,right,down,left
        ans = []
        for i in range(n):
            for j in range(m):
                if flow_both(i, j):
                    ans.append([i, j])

        return ans

# solution 2 - (bfs) - (27ms) - (2025.10.05)
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def flow_check(starts):

            q = deque()
            visited = [[False] * m for _ in range(n)]
            for r, c in starts:
                visited[r][c] = True
                q.append((r, c))
            while q:
                r, c = q.popleft()
                h = heights[r][c]
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if 0 <= nr < n and 0 <= nc < m:
                        if heights[nr][nc] >= h and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))

            return visited

        n = len(heights)
        m = len(heights[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up,right,down,left

        # pacific, atl border
        pac_starts = [(0, c) for c in range(m)] + [(r, 0) for r in range(n)]
        atl_starts = [(n - 1, c) for c in range(m)] + [(r, m - 1) for r in range(n)]

        pac = flow_check(pac_starts)
        atl = flow_check(atl_starts)

        return [[r, c] for r in range(n) for c in range(m) if pac[r][c] and atl[r][c]]

'''
역방향으로 하니까 훨씬 시간복잡도가 좋아졌다.
1번 solution은 각 칸에서 bfs를 돌려서 모든 칸을 다 bfs해야 했다.

2번 solution은 역방향으로 바다에 도달하는 경계로부터 출발하면서 도달할 수 있는 지점을 찾으니 훨씬 빨라졌다.
이 때는 기준점이 도달경계이니까, 탐색하는 위치의 높이가 현재 위치보다 높아야 하는 것만 주의해주면 된다.(역방향이니까)
'''
