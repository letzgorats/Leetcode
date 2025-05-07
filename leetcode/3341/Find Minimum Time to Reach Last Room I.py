# solution 1 - (dist,dijkstra,shortest path,heapq) - (139ms) -(2025.05.07)
from collections import deque
import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]  # up, right, down, left
        n = len(moveTime)
        m = len(moveTime[0])

        pq = [(0, 0, 0)]  # time, r, c
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        while pq:

            t, r, c = heapq.heappop(pq)

            if (r, c) == (n - 1, m - 1):
                return t

            if t == dist[r][c]:

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m:
                        new_time = max(t, moveTime[nr][nc]) + 1
                        if new_time < dist[nr][nc]:
                            dist[nr][nc] = new_time
                            heapq.heappush(pq, (new_time, nr, nc))

        return -1

# TLE 1
from collections import deque


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        q = deque([(0, 0, 0)])  # time, r, c
        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]  # up, right, down, left

        n = len(moveTime)
        m = len(moveTime[0])
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True

        while q:

            # print(q)
            t, r, c = q.popleft()

            if r == n - 1 and c == m - 1:
                return t

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    if moveTime[nr][nc] <= t:
                        q.append((t + 1, nr, nc))
                        visited[nr][nc] = True
                    elif (t + 1, r, c) not in q:
                        q.append((t + 1, r, c))

        return t


# TLE 2
from collections import deque
import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]  # up, right, down, left
        n = len(moveTime)
        m = len(moveTime[0])

        pq = [(0, 0, 0)]  # time, r, c

        while pq:

            t, r, c = heapq.heappop(pq)

            if (r, c) == (n - 1, m - 1):
                return t

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m:
                    new_time = max(t, moveTime[nr][nc]) + 1
                    if new_time >= moveTime[nr][nc]:
                        moveTime[nr][nc] = new_time
                        heapq.heappush(pq, (new_time, nr, nc))

        return -1


'''
1. moveTime을 직접 업데이트하면 거리 정보가 깨지기 때문에 무한 탐색이 발생할 수 있다.
    - moveTime을 거리 배열로 사용하지 말고, 별도의 dist 배열을 사용해야 한다.
        - dist[r][c]에 "해당 위치에 도달한 최단 시간"을 기록한다.
    - 더 짧은 시간에 도착할 때만 큐에 넣어야 한다.
        -현재 코드는 더 긴 시간에도 큐에 넣기 때문에 무한히 반복한다.
        
2. dist 배열을 별도로 관리하면, 최소 시간만 기록되므로 탐색이 종료된다.
    
3. Dijkstra 알고리즘에 맞게 최적화가 가능하다.
'''