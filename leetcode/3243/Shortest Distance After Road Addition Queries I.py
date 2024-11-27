# solution 1 - dijkstra, 1630ms
import heapq
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append((i + 1, 1))
        # print(graph)
        INF = float('inf')

        def dijkstra(start):
            distance = [INF] * n
            q = []
            heapq.heappush(q, (0, start))
            distance[start] = 0
            while q:

                dist, now = heapq.heappop(q)
                if dist > distance[now]:
                    continue
                for i in graph[now]:
                    cost = dist + i[1]
                    if cost < distance[i[0]]:
                        distance[i[0]] = cost
                        heapq.heappush(q, (cost, i[0]))
            return distance

        answer = []
        for i in range(len(queries)):
            a, b = queries[i]
            graph[a].append((b, 1))
            distance = dijkstra(0)
            answer.append(distance[n - 1])

        return answer

# solution 2 - bfs, 486ms
from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        adj = [[i + 1] for i in range(n)]

        def shortest_path():
            q = deque()
            q.append((0, 0))  # node, length
            visit = set()
            visit.add((0, 0))

            while q:
                cur, length = q.popleft()
                if cur == n - 1:
                    return length
                for nei in adj[cur]:
                    if nei not in visit:
                        q.append((nei, length + 1))
                        visit.add(nei)

        res = []
        for src, dst in queries:
            adj[src].append(dst)
            res.append(shortest_path())

        return res
