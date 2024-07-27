# solution1 - dijkstra
from collections import defaultdict
import heapq

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        n = len(original)
        graph = defaultdict(list)
        for i in range(n):
            graph[original[i]].append((changed[i], cost[i]))
            if changed[i] not in graph:
                graph[changed[i]] = []

        INF = int(1e9)

        def dijkstra(src):

            q = [(0, src)]  # (cost,node)
            distances = {node: INF for node in graph}
            distances[src] = 0

            while q:
                current_cost, node = heapq.heappop(q)

                if current_cost > distances[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_cost = current_cost + weight
                    if new_cost < distances[neighbor]:
                        distances[neighbor] = new_cost
                        heapq.heappush(q, (new_cost, neighbor))

            return distances

        all_pairs_shortest_paths = {}
        for node in graph:
            all_pairs_shortest_paths[node] = dijkstra(node)

        answer = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue

            if source[i] not in all_pairs_shortest_paths or target[i] not in all_pairs_shortest_paths[source[i]]:
                return -1

            dist = all_pairs_shortest_paths[source[i]][target[i]]
            if dist == INF:
                return -1
            else:
                answer += dist

        return answer

# solution2 - floyd warshall
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        # INF = int(1e9)는 10억을 뜻하니까 엄연히 말하면 무한대는 아니다.
        distance = [[float('inf')] * 26 for _ in range(26)]

        for i in range(26):
            distance[i][i] = 0

        for old, new, c in zip(original, changed, cost):
            old, new = ord(old) - ord('a'), ord(new) - ord('a')
            distance[old][new] = min(distance[old][new], c)

        # print(distance)
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

        answer = sum(distance[ord(s) - ord('a')][ord(t) - ord('a')] for s, t in zip(source, target))

        return answer if answer != float('inf') else -1