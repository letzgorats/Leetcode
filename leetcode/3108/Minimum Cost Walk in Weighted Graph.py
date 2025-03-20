# solution 1 - union find, graph, bitwise - (192ms) - (2025.03.20)
'''
bitwise AND 연산을 하면 항상 작은 쪽으로 값이 수렴하는 특성이 있다.
때문에, 같은 컴포넌트 내의 값을 다 & 하는 것이 최소값을 찾는 것을 보장한다.
'''
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n  # 모든 집합은 처음엔 자기 자신만 포함

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Connects x and y
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
            return True


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:

        '''
        preprocessing
        1) component(using UF | BFS | DFS)
        2) cost of component
        '''

        uf = UnionFind(n)

        # 1. Build Components
        for u, v, w in edges:
            uf.union(u, v)

        # 2. Get cost of each component
        component_cost = {}  # root -> cost
        for u, v, w in edges:
            root = uf.find(u)
            if root not in component_cost:
                component_cost[root] = w
            else:
                component_cost[root] &= w

        # 3. Queries
        res = []
        for src, dst in query:
            r1, r2 = uf.find(src), uf.find(dst)
            if r1 != r2:
                res.append(-1)
            else:
                res.append(component_cost[r1])

        return res

'''
union_find 에서 union 함수를 짤 때, 한쪽의 컴포넌트의 깊이가 치우치지 않고 각 컴포넌트의 깊이가 고르게 하려면 (그래야, find 연산의 시간도 빨라진다.)
parent 배열만 선언하는 것이 아니라 size 배열(component 크기)도 선언해서 작은 사이즈의 컴포넌트를 큰 쪽으로 흡수시키는 코드로 짜는게 효율적이다.
union find 알고리즘의 효율적인 코드를 다시 또 배웠다.
'''

