# union-find solution

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(a, b):

            parent_a, parent_b = find(a), find(b)
            if parent_a != parent_b:
                parent[parent_a] = parent_b
                return 1
            return 0

        n = len(stones)
        parent = [i for i in range(n)]

        row_dict, col_dict = {}, {}

        cluster = n
        for idx, (r, c) in enumerate(stones):

            if r in row_dict:
                cluster -= union(idx, row_dict[r])
            else:
                row_dict[r] = idx

            if c in col_dict:
                cluster -= union(idx, col_dict[c])
            else:
                col_dict[c] = idx

        return n - cluster

# dfs solution
from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        n = len(stones)
        adj = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)

        # print(adj)

        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        visited = set()
        cluster = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                cluster += 1

        return n - cluster