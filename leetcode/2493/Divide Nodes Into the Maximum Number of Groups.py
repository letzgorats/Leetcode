# solution 1
from collections import deque,defaultdict
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visit = [0] * (n + 1)
        max_groups = 0

        # 연결 요소(component) 찾기
        def find_component(node, component):
            stack = [node]
            component.add(node)
            visit[node] = 1
            while stack:
                cur = stack.pop()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = 1
                        component.add(nei)
                        stack.append(nei)

        # BFS를 통해 최대 그룹 개수 찾기
        def longest_path(start):
            queue = deque([(start, 1)])  # (노드, 그룹 레벨)
            dist = {start: 1}
            max_depth = 1

            while queue:
                node, level = queue.popleft()
                for nei in adj[node]:
                    if nei not in dist:
                        dist[nei] = level + 1
                        max_depth = max(max_depth, level + 1)
                        queue.append((nei, level + 1))
                    elif dist[nei] % 2 == level % 2:
                        return -1  # 홀수 길이 사이클 발견 -> 이분 그래프 X

            return max_depth

        # 전체 그래프를 연결 요소 단위로 탐색
        for i in range(1, n + 1):
            if not visit[i]:
                component = set()
                find_component(i, component)  # 연결 요소 찾기

                # 연결 요소 내에서 BFS 실행하여 최대 그룹 수 찾기
                max_depth = -1
                for node in component:
                    depth = longest_path(node)
                    if depth == -1:
                        return -1  # 홀수 길이 사이클이 존재하면 -1 반환
                    max_depth = max(max_depth, depth)

                max_groups += max_depth  # 가장 깊은 BFS 레벨 추가

        return max_groups


# solution 2
from collections import deque, defaultdict


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        # 연결 요소(component) 찾기
        def get_connected_component(src):

            queue = deque([src])
            component = set([src])
            while queue:
                node = queue.popleft()
                for nei in adj[node]:
                    if nei in component:
                        continue
                    queue.append(nei)
                    component.add(nei)
                    visit.add(nei)

            return component

        def longest_path(src):
            queue = deque([(src, 1)])  # (node,group)
            dist = {src: 1}  # node -> length from src + 1

            while queue:

                node, length = queue.popleft()
                for nei in adj[node]:
                    if nei in dist:
                        if dist[nei] == length:
                            return -1
                        continue
                    queue.append((nei, length + 1))
                    dist[nei] = length + 1

            return max(dist.values())

        visit = set()
        max_groups = 0
        # 전체 그래프를 연결 요소 단위로 탐색
        for i in range(1, n + 1):
            if i in visit:
                continue

            visit.add(i)
            component = get_connected_component(i)

            max_cnt = 0
            for src in component:
                length = longest_path(src)
                if length == -1:
                    return -1
                max_cnt = max(max_cnt, length)

            max_groups += max_cnt

        return max_groups




