# solution 1 - (dp,indegree,graph, topological sort, memoization) - (2169ms) - (2025.05.26)
from collections import defaultdict,deque
from typing import List
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1

        # print(graph)
        # print(indegree)

        # 색깔은 26가지니까 node까지 오는 경로 중에서 색깔 color 가 등장한 최대 개수
        dp = [[0] * 26 for _ in range(n)]
        # print(dp)

        # 진입차수가 0 인 노드를 큐에 넣기 위함
        q = deque([])
        for idx, v in enumerate(indegree):
            if v == 0:
                q.append(idx)
                dp[idx][ord(colors[idx]) - ord('a')] = 1

        # print(q)

        # 큐에서 하나씩 꺼내며 연결된 다음 노드들을 탐색하고, 그때 DP 값을 갱신해나가면 된다.
        visited = set()
        while q:

            node = q.popleft()
            visited.add(node)
            for nxt in graph[node]:
                for c in range(26):
                    add = 1 if ord(colors[nxt]) - ord('a') == c else 0
                    dp[nxt][c] = max(
                        dp[nxt][c],
                        dp[node][c] + add
                    )
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # 위상정렬로 사이클 탐지(모든 노드를 제거하지 못했다면, 사이클 안에 갇힌 노드가 있다는 뜻)
        if len(visited) < n:
            return -1

        answer = -1
        for i in range(n):
            answer = max(max(dp[i]), answer)

        return answer


'''
위상 정렬과 사이클의 관계

- 위상 정렬에서는 진입차수가 0인 노드부터 하나씩 꺼내서 방문해 나간다.
- 그런데, 만약 사이클이 있다면, 사이클 안에 있는 노드는 진입차수가 0 이 되는 순간이 없기 때문에 큐에 들어갈 수 없다.
- 그래서, 결국 큐에서 꺼낸 노드 수가 전체 노드 수보다 적어진다.
'''