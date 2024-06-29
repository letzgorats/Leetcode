from collections import deque

class Solution(object):
    def getAncestors(self, n, edges):

        indegree = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1

        # print(graph)
        # print(indegree)

        answer = [set() for _ in range(n)]
        queue = deque([])

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # print(queue)

        while queue:

            now = queue.popleft()

            for node in graph[now]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)

                answer[node].add(now)
                answer[node].update(answer[now])

        # print(answer)
        for i in range(n):
            answer[i] = sorted(list(answer[i]))

        return answer



# Memory Limit Exceeded solution
from collections import deque


class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        indegree = [0] * n
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1

        # print(graph)
        # print(indegree)

        answer = [[] for _ in range(n)]
        queue = deque([])

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        # print(queue)

        while queue:

            now = queue.popleft()

            for node in graph[now]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)

                answer[node].append(now)
                answer[node].extend(answer[now])

        # print(answer)
        for i in range(n):
            answer[i] = sorted(list(set(answer[i])))

        return answer




