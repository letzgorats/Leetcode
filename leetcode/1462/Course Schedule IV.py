from collections import deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[
        bool]:

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1

        isReachable = [[False] * numCourses for _ in range(numCourses)]

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:

            now = q.popleft()
            for next_course in graph[now]:

                for i in range(numCourses):
                    if isReachable[i][now]:
                        isReachable[i][next_course] = True

                # 자기 자신도 도달 가능성 추가
                isReachable[now][next_course] = True

                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)

        return [isReachable[a][b] for a, b in queries]
