# Memoey Limit Exceeded
from collections import deque, defaultdict
class Solution(object):
    def canTraverseAllPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def gcd(a,b):

            while b:
                a,b = b, a % b

            return a

        def buildGraph(nums):
            graph = defaultdict(list)
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if gcd(nums[i],nums[j]) > 1:
                        graph[i].append(j)
                        graph[j].append(i)
            return graph
        
        def bfs(graph,start,n):

            visited = [False] * n
            queue = deque([start])
            visited[start] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            return all(visited)
        
        graph = buildGraph(nums)

        return bfs(graph,0,len(nums))

        

# solution

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        if len(nums) == 1    : return True          # <-- some edge cases
        if 1 in nums         : return False         #

        nums = sorted(set(nums), reverse = True)    # <-- sort (big to little) and  
        if (n:=len(nums))==1 : return True          #     deal with another edge case

        for i in range(n-1):                        # <-- nums[i] >= nums[j]
            for j in range(i+1,n):
            
                if gcd(nums[i],nums[j])-1:          # <-- i,j traversal exists; 
                    nums[j] *= nums[i]              # <-- if an i,k traversal exists   
                    break                           #     (for some index k), then now 
                                                    #     a j,k traversal exists

            else: return False                      # <-- no match means no traversal 

        return True 
