class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def find_parent(parent, x):
            if parent[x] != x:
                parent[x] = find_parent(parent, parent[x])
            return parent[x]

        def union_parent(parent, a, b):
            a = find_parent(parent, a)
            b = find_parent(parent, b)
            if a < b:
                parent[b] = a
            else:
                parent[a] = b

        n = len(edges)
        parent = [i for i in range(n + 1)]

        for a, b in edges:

            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
            else:
                return [a, b]
