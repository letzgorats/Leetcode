# TLE - bfs, grid - (TLE) - (2025.03.28)
import heapq
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        answer = [0] * len(queries)
        m, n = len(grid[0]), len(grid)

        dr = [-1, 0, 1, 0]  # up, right, down, left
        dc = [0, 1, 0, -1]

        def bfs(startr, startc, val):
            q = []
            heapq.heappush(q, (val, (startr, startc)))  # threshold = val
            count = 0

            if grid[startr][startc] < val:
                visited[startr][startc] = True
                count += 1

            while q:

                val, (nowr, nowc) = heapq.heappop(q)
                if visited[nowr][nowc]:
                    for d in range(4):
                        nr, nc = nowr + dr[d], nowc + dc[d]
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                            if grid[nr][nc] < val:
                                visited[nr][nc] = True
                                count += 1
                                q.append((val, (nr, nc)))
            return count

        for i in range(len(queries)):
            visited = [[False] * m for _ in range(n)]
            answer[i] = bfs(0, 0, queries[i])

        return answer

# solution 2 - bfs - (473ms) - (2025.03.28)
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:

        def bfs(startr, startc, val, idx):

            heapq.heappush(q, (val, (startr, startc)))  # threshold = val
            count = 0

            if grid[startr][startc] < val:
                visited[startr][startc] = True
                count += 1

            while q and q[0][0] < val:

                val, (nowr, nowc) = heapq.heappop(q)
                count += 1
                if visited[nowr][nowc]:
                    for d in range(4):
                        nr, nc = nowr + dr[d], nowc + dc[d]
                        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                            if grid[nr][nc] < val:
                                visited[nr][nc] = True
                                heapq.heappush(q, (val, (nr, nc)))

            answer[idx] = count

        m, n = len(grid[0]), len(grid)
        dr = [-1, 0, 1, 0]  # up, right, down, left
        dc = [0, 1, 0, -1]

        # query 미리 정렬하고, visited 재사용하는게 효율적
        # 쿼리 정렬 - 원래 인덱스 보존
        idx_queries = sorted([(val, idx) for idx, val in enumerate(queries)])
        visited = [[False] * m for _ in range(n)]
        answer = [0] * len(queries)
        visited[0][0] = True

        # 최소힙(값이 작은 셀부터 탐색)
        q = [(grid[0][0], 0, 0)]
        count = 0

        # 각 쿼리에 대해 처리
        for val, idx in idx_queries:
            # 현재 쿼리보다 작은 grid 값을 가진 셀만 처리
            while q and q[0][0] < val:
                _, r, c = heapq.heappop(q)
                count += 1  # 처음 방문하므로 점수 +1

                # 4방향으로 확장
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                        # 일단 방문하지 않았다면, 방문하고, heapq 에 넣어놓는다.
                        # while 문 조건에 걸리지 않는다면, 다음 쿼리로 넘어가서 그 위치부터 다시 탐색할 수 있도록 하는
                        # 일종의 재활용할 수 있는 로직이다.
                        visited[nr][nc] = True
                        heapq.heappush(q, (grid[nr][nc], nr, nc))

            # 현재 쿼리 결과 저장
            answer[idx] = count

        return answer