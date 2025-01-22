class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        n, m = len(isWater), len(isWater[0])
        heights = [[-1] * m for _ in range(n)]

        queue = deque([])
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    heights[i][j] = 0
                    queue.append((i, j))

        dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌
        dc = [0, 1, 0, -1]  # 상, 우, 하, 좌

        while queue:

            r, c = queue.popleft()
            # visited.add((r,c))
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and (nr, nc) and heights[nr][nc] == -1:
                    heights[nr][nc] = heights[r][c] + 1  # 이전 높이 + 1
                    queue.append((nr, nc))

        # print(heights)

        return heights