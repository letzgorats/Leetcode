# solution 1 - Dijkstra
from collections import deque
import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = [[] for _ in range(n)]

        for a, b, cost in edges:
            graph[a].append((b, cost))
            graph[b].append((a, cost))

        # print(graph)
        INF = int(1e9)

        def dijkstra(start):
            distances = [INF] * n
            distances[start] = 0
            q = []
            heapq.heappush(q, (0, start))  # (distance, node)

            while q:
                current_distance, current_node = heapq.heappop(q)

                if current_distance > distances[current_node]:
                    continue

                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(q, (distance, neighbor))

            return distances

        min_city = -1
        min_count = INF
        for i in range(n):
            distances = dijkstra(i)
            count = 0
            for d in distances:
                if d <= distanceThreshold:
                    count += 1
            # count = sum(1 for d in distances if d <= distanceThreshold)
            if count <= min_count:
                min_count = count
                min_city = i

        return min_city

    # solution 2 - Floyd warshall
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        INF = int(1e9)
        dist = [[INF] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0  # 자기 자신으로의 거리는 0

        # 주어진 간선 정보를 기반으로 거리 초기화
        for a, b, cost in edges:
            dist[a][b] = cost
            dist[b][a] = cost

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])

        min_city = -1
        min_count = INF
        for i in range(n):
            count = 0

            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1

            if count <= min_count:
                min_count = count
                min_city = i

        return min_city
