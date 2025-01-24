# solution 1 - bfs (63ms)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n

        # 역방향 그래프 생성 및 진입 차수 계산
        for node, neighbors in enumerate(graph):
            for neighbor in neighbors:
                reverse_graph[neighbor].append(node)
                in_degree[node] += 1

                # 진입 차수가 0인 노드(=terminal node)
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        answer = []

        # print(in_degree)

        while queue:
            node = queue.popleft()
            answer.append(node)

            for prev_node in reverse_graph[node]:
                ## graph 입장에서의 in_degree 는
                # reverse_graph 입장에서는 outgoing
                in_degree[prev_node] -= 1
                if in_degree[prev_node] == 0:
                    queue.append(prev_node)

        return sorted(answer)


# solution 2 - dfs (11ms)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        state = [0] * n  # 노드 상태 : 0(미방문), 1(방문 중), 2(안전)

        def dfs(node):
            if state[node] != 0:  # 이미 방문한 노드
                return state[node] == 2  # 안전한 노드인지 여부 판단

            state[node] = 1  # 방문 중
            for neighbor in graph[node]:
                if not dfs(neighbor):  # 사이클이 발견되면 False
                    return False

            state[node] = 2  # 안전한 노드로 갱신
            return True

        # 모든 노드에 대해 DFS 호출
        return sorted([i for i in range(n) if dfs(i)])