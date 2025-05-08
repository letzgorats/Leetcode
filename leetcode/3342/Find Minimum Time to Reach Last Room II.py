# solution 1 - (bfs,heapq,dist,queue) - (1869ms) - (2025.05.08)
import heapq
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        n = len(moveTime)
        m = len(moveTime[0])

        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0
        pq = []
        heapq.heappush(pq, (0, 0, 0, 0))  # time, r, c, step()
        dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]  # up, right, down, left

        while pq:

            t, r, c, step = heapq.heappop(pq)

            if (r, c) == (n - 1, m - 1):
                return t

            if t == dist[r][c]:

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m:
                        if step % 2 == 0:
                            next_step = 1
                            # 현재 +2초로 이동했었다면, 다음은 + 1
                            new_time = max(t, moveTime[nr][nc]) + 1
                        else:
                            next_step = 0
                            # 현재 +1초로 이동했었다면, 다음은 + 2
                            new_time = max(t, moveTime[nr][nc]) + 2

                        if new_time < dist[nr][nc]:
                            dist[nr][nc] = new_time
                            heapq.heappush(pq, (new_time, nr, nc, next_step))

        return -1

'''
1초 -> 2초 -> 1초 -> 2초 ... 번갈아 이동하는 차례를 정확히 하기 위해, step 변수도 queue에 추가
+1초로 이동했는지,
+2초로 이동했는지, 
정확히 파악이 가능하다.
'''