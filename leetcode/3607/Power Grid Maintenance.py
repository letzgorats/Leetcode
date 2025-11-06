# solution 1 - (dsu,union find,bfs,dfs) - (876ms) - (2025.11.06)
from collections import defaultdict
from sortedcontainers import SortedList
from typing import List


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # 1) DSU: union-find with path compression + union by size
        parent = list(range(c + 1))
        size = [1] * (c + 1)

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        # 2) 고정 연결성 구성
        for u, v in connections:
            union(u, v)

        # 3) 각 컴포넌트별 온라인 노드 SortedList 구성 (초기엔 모두 온라인)
        comp = defaultdict(SortedList)
        for x in range(1, c + 1):
            comp[find(x)].add(x)

        online = [True] * (c + 1)

        # 4) 쿼리 처리
        ans = []
        for t, x in queries:
            if t == 1:
                if online[x]:
                    ans.append(x)  # 스스로 처리
                else:
                    root = find(x)
                    sl = comp[root]
                    if len(sl) == 0:
                        ans.append(-1)
                    else:
                        ans.append(sl[0])  # 그리드 내 온라인 중 가장 작은 id
            else:  # t == 2: 오프라인 전환
                if online[x]:
                    online[x] = False
                    root = find(x)
                    comp[root].discard(x)  # O(log n)
                # 이미 오프라인이면 아무 것도 안 함

        return ans
