import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        time = 0
        q = []
        heapq.heappush(q, (time, 0, 0))
        visit = set()
        dr = [-1, 0, 1, 0]  # up, right, down, left
        dc = [0, 1, 0, -1]

        while q:

            (t, r, c) = heapq.heappop(q)

            if (r, c) in visit:
                continue
            visit.add((r, c))

            if (r == n - 1) and (c == m - 1):
                return t

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and ((nr, nc) not in visit):
                    next_t = t + 1
                    if next_t < grid[nr][nc]:
                        wait_t = grid[nr][nc] - next_t
                        if wait_t % 2 == 0:
                            next_t = grid[nr][nc]
                        else:
                            next_t = grid[nr][nc] + 1

                    heapq.heappush(q, (next_t, nr, nc))

        return -1

'''
Consider the case where you have to go back and forth between two cells of the matrix to unlock some other cells.
그럼 초기 이동만 뚫린다면, 웬만해선 값이 -1이 아닐 것이다. 왔다갔다하면서 시간을 소비하면 되기 떄문이다.
그 왔다갔다 하는 시간을 wait_t 이라고 설정하고, wait_t 가 홀수이면 (다음 그리드 값 +1), 짝수이면 (그리드 값)으로 시간을 설정해서 큐에 넣으면 된다.
'''