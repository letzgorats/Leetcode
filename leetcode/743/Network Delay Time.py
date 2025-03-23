# solutjon 1 - dijkstra,shortest path,distance - (373ms) - (2025.03.23)
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)

        for a, b, c in times:
            graph[a - 1].append((b - 1, c))  # a -> b로 가는데 드는 시간 c

        distance = [float('inf')] * n

        def dijkstra(src):
            q = []
            heapq.heappush(q, (0, src))  # (비용,소스노드)
            distance[src] = 0

            while q:
                c1, now = heapq.heappop(q)

                # 현재 노드가 이미 최단 경로로 처리된적이 있다면, pass
                if distance[now] < c1:
                    continue

                for nei, c2 in graph[now]:

                    # nei 까지 도달 하는데 이동하는 거리가 c1+c2 보다 길다면, c1+c2 로 새로 갱신
                    if c1 + c2 < distance[nei]:
                        distance[nei] = c1 + c2
                        heapq.heappush(q, (c1 + c2, nei))

        dijkstra(k - 1)  # k 번(k-1) 노드 출발,
        # print(distance)

        return -1 if any(i == float('inf') for i in distance) else max(distance)

