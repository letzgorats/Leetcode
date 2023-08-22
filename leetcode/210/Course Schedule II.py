import heapq
from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        graph = [[] for _ in range(n)]
        indegree = [0] * (n+1)
        result = []
        queue = deque([])

        for p in prerequisites:

            graph[p[1]].append(p[0])
            indegree[p[0]] += 1

        for i in range(n):
           if indegree[i] == 0:
            queue.append(i)
        
        while queue: 
            
            now = queue.popleft()
            result.append(now)

            for i in graph[now]:
                indegree[i] -=1 
                if indegree[i] == 0:
                    queue.append(i)

        if n != len(result):
            return []

        else:   
            return result
