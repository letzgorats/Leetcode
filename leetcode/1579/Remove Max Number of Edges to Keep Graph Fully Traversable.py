class Disjoint_Set_Union:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):

        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):

        # DSU 자료구조 초기화
        dsu_alice = Disjoint_Set_Union(n)
        dsu_bob = Disjoint_Set_Union(n)
        dsu_total = Disjoint_Set_Union(n)

        edges.sort(reverse=True, key=lambda x: x[0])

        total_edges = 0
        alice_edges = 0
        bob_edges = 0

        for edge in edges:

            t, a, b = edge
            a -= 1
            b -= 1

            if t == 3:
                if dsu_total.union(a, b):
                    total_edges += 1
                    if dsu_alice.union(a, b):
                        alice_edges += 1
                    if dsu_bob.union(a, b):
                        bob_edges += 1

            elif t == 1:
                if dsu_alice.union(a, b):
                    alice_edges += 1
                    total_edges += 1

            elif t == 2:
                if dsu_bob.union(a, b):
                    bob_edges += 1
                    total_edges += 1

        if alice_edges == n - 1 and bob_edges == n - 1:
            return len(edges) - total_edges
        else:
            return -1


