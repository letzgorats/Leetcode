# union-find solution

class Solution(object):
    def validPath(self, n, edges, source, destination):

        def find_parent(parent,node):

            if parent[node] != node:
                parent[node] = find_parent(parent,parent[node])
            
            return parent[node]

        def union_parent(parent,a,b):

            a = find_parent(parent,a)
            b = find_parent(parent,b)

            if a < b :
                parent[b] = a
            else:
                parent[a] = b

        # graph = [[] for _ in range(n)]
        # for a,b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)

        parent = [i for i in range(n)]
        cycle = False

        for a,b in edges:
            union_parent(parent,a,b)
        
        print(parent)

        return find_parent(parent,parent[source]) == find_parent(parent,parent[destination])


# BFS solution

from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        if not edges:
            return True
            
        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue = deque([source])
        seen = set()

        while queue :

            now = queue.popleft()
            seen.add(now)
            for node in graph[now]:
                if node == destination:
                    return True
                if node not in seen:
                    queue.append(node)
                    seen.add(node)
        
        return False
