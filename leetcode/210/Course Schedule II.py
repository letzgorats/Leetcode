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



# topological sort -> (https://letzgorats.tistory.com/entry/%EA%B7%B8%EB%9E%98%ED%94%84-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-2-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%97%90%EC%84%9C-%EC%9E%90%EC%A3%BC-%EB%93%B1%EC%9E%A5%ED%95%98%EB%8A%94-%EA%B8%B0%ED%83%80-%EA%B7%B8%EB%9E%98%ED%94%84-%EC%9D%B4%EB%A1%A0)
