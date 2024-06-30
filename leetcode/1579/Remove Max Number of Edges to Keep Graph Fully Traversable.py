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

        # DSU 자료구조 초기
        dsu_alice = Disjoint_Set_Union(n)
        dsu_bob = Disjoint_Set_Union(n)
        dsu_total = Disjoint_Set_Union(n)

        # 간선을 타입에 따라 내림차순
        # (타입 3 간선을 먼저 처리하도록 하는 역할)
        # 타입 3 간선은 alice, bob 둘 다 사용할 수 있어
        # 최대한 활용하는 것이 간선을 절약하는 데 유리하다.

        edges.sort(reverse=True, key=lambda x: x[0])

        total_edges = 0 # 총 사용된 간선 수
        alice_edges = 0  # alice 가 사용한 간선 수
        bob_edges = 0 # bob 이 사용한 간선 수

        # 간선을 하나씩 처리
        for edge in edges:

            t, a, b = edge
            a -= 1  # 인덱스를 0 부터 시작하도록 조정
            b -= 1  # 인덱스를 0 부터 시작하도록 조정

            if t == 3:
                # 타입 3 간선: 전체, alice, bob 모두에 추가
                if dsu_total.union(a, b):
                    total_edges += 1
                    if dsu_alice.union(a, b):
                        alice_edges += 1
                    if dsu_bob.union(a, b):
                        bob_edges += 1

            elif t == 1:
                # 타입 1 간선: alice 에만 추가
                if dsu_alice.union(a, b):
                    alice_edges += 1
                    total_edges += 1

            elif t == 2:
                # 타입 2 간선: bob 에만 추가
                if dsu_bob.union(a, b):
                    bob_edges += 1
                    total_edges += 1

        print(alice_edges)
        print(bob_edges)
        if (alice_edges == n - 1) and (bob_edges == n - 1):
            # 제거할 수 있는 간선 수 반환
            return len(edges) - total_edges
        else:
            return -1


