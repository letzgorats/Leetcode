# solution 1 - (dfs) - (3ms) - (2025.06.05)
from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        n = len(s1)
        adj = defaultdict(set)
        for i in range(n):
            adj[s1[i]].add(s2[i])
            adj[s2[i]].add(s1[i])

        visited = set()
        group_map = {}

        def dfs(node, group):
            visited.add(node)
            group.append(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei, group)

        new_str = ""
        m = len(baseStr)

        # 모든 문자에 대해 그룹 만들고, 대표 문자 매핑
        for c in set(s1 + s2):
            if c not in visited:
                group = []
                dfs(c, group)
                min_char = min(group)
                print(c, group)
                for ch in group:
                    group_map[ch] = min_char

        # baseStr 변환
        res = []
        for c in baseStr:
            res.append(group_map.get(c, c))

        return ''.join(res)


'''
아직 방문하지 않은 문자를 기준으로 dfs 를 돌려서 하나의 그룹을 구한다.
그 그룹 중에서 사전순으로 가장 작은 문자를 min_char 로 정한다.
그리고 그 그룹에 속한 모든 문자들을 다 min_char 로 치환될 수 있도록 group_map[ch] = min_char 로 매핑한다.
'''


# solution 2 - (union find) - (3ms) - (2025.06.05)
class UnionFind:
    def __init__(self, n):
        # self.parent = {chr(i + ord('a')): chr(i + ord('a')) for i in range(26)}
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(len(baseStr))
        for a, b in zip(s1, s2):
            uf.union(a, b)

        return ''.join(uf.find(c) for c in baseStr)


'''
dict.setdefault(key, default)의 뜻
-> key가 딕셔너리에 존재하면 그 값을 리턴,
-> key가 존재하지 않으면 default를 넣고 그 값을 리턴.


self.parent.setdefault(x, x)
-> 만약 x가 self.parent 딕셔너리에 없으면 self.parent[x] = x로 설정하고, 그 값을 리턴
-> 이미 있으면 그냥 기존 값을 리턴

전체 if x != self.parent.setdefault(x, x):
-> 결국 x가 자신의 부모가 아니면, 즉 루트 노드가 아니면 재귀 호출로 find 수행
'''

# solution 3 - (ord,union find) - (3ms) - (2025.06.05)
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        def find(x):
            i = ord(x) - ord('a')
            while i != parent[i]:
                i = parent[i]
            return i

        parent = list(range(26))
        for a, b in zip(s1, s2):
            pa = find(a)
            pb = find(b)
            if pa > pb:
                parent[pa] = pb
            else:
                parent[pb] = pa

        res = []
        for c in baseStr:
            res.append(chr(ord('a') + find(c)))

        return "".join(res)