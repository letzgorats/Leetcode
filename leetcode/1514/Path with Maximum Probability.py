from collections import deque
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        graph = [[] for _ in range(n)]

        for idx, startTo in enumerate(edges):
            a, b = startTo[0], startTo[1]
            graph[a].append((b, succProb[idx]))
            graph[b].append((a, succProb[idx]))

        # print(graph)
        probability = [0.0] * (n)

        def dijkstra(start):
            q = []
            heapq.heappush(q, (-1.0, start))
            probability[start] = 1.0

            while q:

                prob, now = heapq.heappop(q)
                prob = -prob

                if probability[now] > prob:
                    continue

                for cur in graph[now]:
                    cost = prob * cur[1]

                    if cost > probability[cur[0]]:
                        probability[cur[0]] = cost
                        heapq.heappush(q, (-cost, cur[0]))

        dijkstra(start_node)
        return probability[end_node]