# solution 1 - union find, math, expected_edges in completed components - (95ms) - (2025.03.22)
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n  # 처음에는 컴포넌트에 자기 자신만 포함

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a != b:
            if self.size[a] < self.size[b]:
                self.parent[a] = b
                self.size[b] += self.size[a]
            else:
                self.parent[b] = a
                self.size[a] += self.size[b]

from collections import defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        uf = UnionFind(n)

        # 1. Build components
        for a, b in edges:
            uf.union(a, b)

        # print(uf.parent)

        # 2. Grouping each component
        groups = defaultdict(list)
        for node in range(n):
            root = uf.find(node)
            groups[root].append(node)

        # print(groups)

        # 3. count edges per group
        edge_count = defaultdict(int)
        for a, b in edges:
            root = uf.find(a)  # a와 b는 같은 그룹에 있으니까 하나로 충분
            edge_count[root] += 1

        # print(edge_count)

        answer = 0
        for root, nodes in groups.items():
            k = len(nodes)
            expected_completed_components_edges = k * (k - 1) // 2
            if edge_count[root] == expected_completed_components_edges:
                answer += 1

        return answer

# solution 2 - dfs, bfs - (47ms) - (2025.03.22)

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [0] * n

        def dfs(node):

            nonlocal node_count, edge_count
            visited[node] = 1
            node_count += 1
            edge_count += len(graph[node])  # 양방향이라 나중에 //2 해줄 것!

            for i in graph[node]:
                if not visited[i]:
                    dfs(i)

        answer = 0
        for i in range(n):
            if not visited[i]:
                node_count = 0
                edge_count = 0
                dfs(i)
                if edge_count // 2 == node_count * (node_count - 1) // 2:
                    answer += 1

        return answer

# solution 3 - dfs - (59ms) - (2025.03.22)
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(v,res):
            if v in visit:
                return
            visit.add(v)
            res.append(v)
            for nei in adj[v]:
                dfs(nei,res)
            return res

        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        res = 0
        visit = set()

        for v in range(n):
            if v in visit:
                continue
            component = dfs(v,[])
            print(component)
            for v2 in component:
                if len(component)-1 != len(adj[v2]):
                    # 하나라도 그렇지 않다면 완전 컴포넌트가 아님. break
                    break
            # else 면 break 안 걸리고 순회가 끝났다는 뜻이므로 + 1
            # = (component 에 있는 "모든" 노드들에서 뻗어나오는 간선의 수가 전체 컴포넌트를 구성하는 노드-1)이라면 +1
            else:
                res += 1
            # if all([len(component) - 1 == len(adj[v2]) for v2 in component]):
            #     res += 1

        return res

'''
nonlocal 이면 안에서만 nonlocal 명시해주면 된다.
global 이면 안에서만 global 이라고 명시해주면 된다. 
'''