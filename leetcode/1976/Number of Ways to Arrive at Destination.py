# solution 1 - dijkstra, dp - (16ms) - (2025.03.23)
import heapq
from collections import defaultdict
'''
목표 
1. 최단거리(distance) 계산 -> 다익스트라 사용
2. 해당 거리로 도달하는 경우의 수(ways) 계산 -> 다익스트라 중에 동시에 계산
'''
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        mod = 10 ** 9 + 7

        # Step 1 -> 최단거리 구하기
        def dijkstra(src, cost):

            q = []
            heapq.heappush(q, (cost, src))
            # visited = set()   # 사실상 필요없음(distance 조건으로 걸러지기 때문)
            # visited.add(src)
            distance[src] = 0
            while q:

                c1, now = heapq.heappop(q)
                if distance[now] < c1:   # 이미 더 짧은 거리로 처리한 적이 있으면 무시
                    continue

                for nei, c2 in graph[now]:
                    if c1 + c2 == distance[nei]:  # 같은 거리로 또 도달(이미 nei까지의 최단거리가 존재하는데)
                        # 또 하나의 경로(now -> nei) 가 동일한 거리라면,
                        # 기존 방법에 더해 하나의 경로가 더 생긴 것이므로
                        # nei 까지 오는 최단거리 경로의 수는 ways[now] 까지 오는 최단경로의 수를 더해주면 그만이다.
                        ways[nei] += ways[now]
                    elif c1 + c2 < distance[nei]:  # 더 짧은 거리로 도달
                        # nei 까지 오는 최단거리 경로의 수는 now 까지 오는 최단거리 경로의 수다.(이제부터는 이게 최단, 경로 수 새로 세팅)
                        ways[nei] = ways[now]
                        # 거리도 갱신
                        distance[nei] = c1 + c2
                        heapq.heappush(q, (c1 + c2, nei))

        graph = defaultdict(list)

        for a, b, cost in roads:
            graph[a].append((b, cost))
            graph[b].append((a, cost))

        distance = [float('inf')] * (n)

        # Step 2 -> 경로찾기
        ways = [0] * n
        ways[0] = 1 # 출발지에서 출발하는 경로는 1개

        dijkstra(0, 0)
        # print(ways)
        # print(distance)

        return ways[-1] % mod

