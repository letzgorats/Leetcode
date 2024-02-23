# approach 1 - wrong solution(dijkstra)
from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Create a graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Queue: (cost, current_node, stops)
        queue = deque([(0, src, 0)])
        # Visited dictionary to keep track of the least amount of stops to a node
        visited = {src: 0}
        
        while queue:
            cost, node, stops = queue.popleft()
            # If we reach the destination, return the cost
            if node == dst:
                return cost
            # If we have stops left, we can continue to explore
            if stops <= k:
                for next_node, price in graph[node]:
                    next_cost = cost + price
                    # If this path is better or we haven't visited the next node yet
                    if next_node not in visited or stops < visited[next_node]:
                        visited[next_node] = stops
                        queue.append((next_cost, next_node, stops + 1))
        
        # If we can't reach the destination within k stops, return -1
        return -1

# approach 2 (python3) - not dijkstra, but bellman-ford(DP + BFS)
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        
        for i in range(k + 1):
            tempPrices = prices.copy()
            for u, v, w in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + w < tempPrices[v]:
                    tempPrices[v] = prices[u] + w
            prices = tempPrices
        
        return -1 if prices[dst] == float('inf') else prices[dst]


# TLE
import heapq
class Solution(object):

    def findCheapestPrice(self, n, flights, src, dst, k):
    
        graph = [[] for _ in range(n)]

        for a,b,c in flights:

            graph[a].append((b,c))
        
        # print(graph)

        queue = []

        # Min heap to store the current cost to reach a node, the number of stops, and the node itself
        queue = [(0, src, k + 1)]

        while queue:
            cost, now, stops = heapq.heappop(queue)
            if now == dst:
                return cost
            if stops > 0:
                for next_node, price in graph[now]:
                    heapq.heappush(queue, (cost+price, next_node, stops - 1))
            

        return -1
