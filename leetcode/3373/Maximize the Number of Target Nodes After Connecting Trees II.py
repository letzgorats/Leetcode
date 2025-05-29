# solution 1 - (tree,graph,bfs) - (499ms) - (2025.05.29)
from collections import defaultdict, deque


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def build_adj(edges):
            adj = defaultdict(list)
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            return adj

        adj1, adj2 = build_adj(edges1), build_adj(edges2)

        n = len(adj1)
        m = len(adj2)

        def bfs(source, adj):
            q = deque([(source, 0, -1)])  # node, parity, parent
            even, odd = set(), set()

            while q:
                node, parity, parent = q.popleft()
                if parity == 0:
                    even.add(node)
                else:
                    odd.add(node)

                for nei in adj[node]:
                    if nei != parent:
                        new_parity = 0 if parity == 1 else 1
                        q.append((nei, new_parity, node))

            return even, odd

        even2, odd2 = bfs(0, adj2)
        even1, odd1 = bfs(0, adj1)

        mx2 = max(len(even2), len(odd2))

        res = [0] * n
        for i in range(n):
            if i in even1:
                res[i] = len(even1) + mx2
            else:
                res[i] = len(odd1) + mx2

        return res
