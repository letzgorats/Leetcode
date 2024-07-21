from collections import deque
from typing import List
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        matrix = [[0] * k for _ in range(k)]

        row_graph = [[] for _ in range(k + 1)]
        col_graph = [[] for _ in range(k + 1)]

        row_indegree = [0] * (k + 1)
        col_indegree = [0] * (k + 1)

        for a, b in rowConditions:
            row_graph[a].append(b)
            row_indegree[b] += 1
        for a, b in colConditions:
            col_graph[a].append(b)
            col_indegree[b] += 1

        def topology_sort(graph, indegree):
            res = []
            q = deque()

            for i in range(1, k + 1):
                if indegree[i] == 0:
                    q.append(i)

            while q:
                node = q.popleft()
                res.append(node)
                for nei in graph[node]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        q.append(nei)

            if len(res) == k:
                return res
            else:
                # cycle or not all nodes are connected
                return []

        r = topology_sort(row_graph, row_indegree)
        c = topology_sort(col_graph, col_indegree)

        if not r or not c:
            return []

        row_pos = {num: i for i, num in enumerate(r)}
        col_pos = {num: i for i, num in enumerate(c)}

        for i in range(1, k + 1):
            matrix[row_pos[i]][col_pos[i]] = i

        return matrix