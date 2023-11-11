class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.graph = [[] for _ in range(n)]

        for e in edges:
            self.graph[e[0]].append((e[1],e[2]))


    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        self.graph[edge[0]].append((edge[1],edge[2]))
    
    def dijkstra(self,node1,node2):
        queue = [(0,node1)]
        n = len(self.graph)
        distance = [float('inf')] * n 
        distance[node1] = 0

        while queue:
            dist, current_node = heapq.heappop(queue)

            if distance[current_node] < dist:
                continue
            
            if current_node == node2:
                return distance[current_node]
            
            for i in self.graph[current_node]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue,(cost,i[0]))
        
        return -1

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        return self.dijkstra(node1,node2)
    
    

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
