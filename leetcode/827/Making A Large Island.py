# solution 1 - bfs, not TLE
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        # 상 우 하 좌
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        island_sizes = {}  # {island_id : 섬의 크기}
        island_id = 2

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q = deque([(i, j)])
                    grid[i][j] = island_id  # 새로운 id 할당
                    size = 1  # 섬 크기 초기화
                    while q:
                        r, c = q.popleft()
                        for d in range(4):
                            nr = r + dr[d]
                            nc = c + dc[d]
                            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                                grid[nr][nc] = island_id
                                q.append((nr, nc))
                                size += 1

                    island_sizes[island_id] = size  # 해당 섬 크기 저장
                    island_id += 1

        # 만약 이미 모든 칸이 1이라면 바로 전체 크기 반환
        if not any(0 in row for row in grid):
            return n * m

        # 각 0을 1로 바꿀 때 최대 섬 크기를 구하기
        max_area = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:  # 0을 1로 변경할 후보
                    seen = set()  # 이미 확인한 섬 id 저장
                    area = 1  # 0 을 1로 바꿨을 때 영역 초기화
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > 1:
                            island_id = grid[nr][nc]
                            if island_id not in seen:
                                seen.add(island_id)
                                area += island_sizes[island_id]  # 미리 구한 섬 크기 활용

                    max_area = max(max_area, area)

        return max_area

# solution 2 - TLE
from collections import deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        def bfs(r, c, tmp):

            q = deque([(r, c)])
            visited = {(r, c)}
            area = 1

            while q:

                r, c = q.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and tmp[nr][nc] == 1:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1

            return area

        n = len(grid)
        m = len(grid[0])
        zero = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zero.add((i, j))

        dr = [-1, 0, 1, 0]  # 상,우,하,좌
        dc = [0, 1, 0, -1]
        max_area = 0

        if len(zero) == 0:
            return n * m

        for r, c in zero:
            tmp = grid
            tmp[r][c] = 1
            for i in range(n):
                for j in range(m):
                    if tmp[i][j] == 1:
                        max_area = max(bfs(r, c, tmp), max_area)
            tmp[r][c] = 0

        return max_area