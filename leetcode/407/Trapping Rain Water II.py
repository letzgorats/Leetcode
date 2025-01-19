import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        n = len(heightMap)
        m = len(heightMap[0])

        # 가장자리 처리 : 가장자리는 물이 빠져나갈 수 있으므로, 처음에 모두 최소 힙에 넣는다.
        min_heap = []
        visited = set()  # 방문 처리 배열
        for i in range(n):
            for j in range(m):
                if (i in [0, n - 1]) or (j in [0, m - 1]):
                    heapq.heappush(min_heap, (heightMap[i][j], i, j))
                    visited.add((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
        water_trapped = 0

        # 현재까지 참색한 가장 낲은 높이를 기준으로, 주변 칸의 물이 고일 수 있는지 탐색

        while min_heap:

            # 높이, 행, 열
            h, r, c = heapq.heappop(min_heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= m or (nr, nc) in visited:
                    continue

                # 물은 max(0, 현재 높이 - heightMap[nr][nc]) 만큼 고일 수 있다.
                water_trapped += max(0, h - heightMap[nr][nc])
                visited.add((nr, nc))

                # 힙에 추가할 때는 max(h,heightMap[nr][nc]) 로 기준높이를 갱신하여 물이 더 이상 고이지 않게 한다.
                heapq.heappush(min_heap, (max(h, heightMap[nr][nc]), nr, nc))

        return water_trapped