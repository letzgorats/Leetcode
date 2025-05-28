# solution 1 - (bfs,dfs,graph,edges,node) - (2025.05.28)
from typing import List
from collections import defaultdict,deque
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        def spread(source, graph, limit):
            visited = set()
            q = deque()
            q.append((source, 0)) # source 노드는 depth가 0으로 간주, 자기포함
            visited.add(source)
            count = 0

            while q:
                node, depth = q.popleft()
                if depth > limit:
                    continue
                # 노드 확산의 깊이를 하나 더 늘리는 작업이 아니라, 방문 가능한 노드의 수를 세는 작업
                # 이 노드까지 접근 가능하니까 개수로 세자라는 의미에서 count += 1
                # (2 - 0 - 1 라면 0번 노드를 기준으로 1번 노드, 2번 노드가 depth 1 만에 갈 수 있다-> 2개 노드)
                count += 1
                for nei in graph[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, depth + 1))
            return count

        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        n = len(edges1) + 1
        m = len(edges2) + 1
        for a, b in edges1:
            graph1[a].append(b)
            graph1[b].append(a)
        for a, b in edges2:
            graph2[a].append(b)
            graph2[b].append(a)

        # Tree2에서 최대확산 가능한 best_node 선택
        best_node = 0
        for i in range(m):
            connections = spread(i, graph2, k - 1)
            best_node = max(best_node, connections)

        # Tree1에서 각 노드에서 시작한 경우 결과 계산
        res = []
        for i in range(n):
            reachable = spread(i, graph1, k)
            res.append(reachable + best_node)
        return res