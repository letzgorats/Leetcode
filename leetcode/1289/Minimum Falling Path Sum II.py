# BFS solution - Memory Limit Exceeded
from collections import deque
class Solution(object):
    def minFallingPathSum(self, grid):
      
        n = len(grid)
        min_answer = float('inf')

        def bfs(r,c):

            queue = deque([(r,c,grid[r][c])])
            min_val = 100

            while queue:

                r, c, val = queue.popleft()
                if (r+1) < n :
                    nr = (r+1)
                    for j in range(n):
                        if j != c:
                            nc = j
                            queue.append((nr,nc,val+grid[nr][nc]))
                
                if r == n-1 :
                    min_val = min(val,min_val)
                # print(r,c, min_val)

            return min_val

        
        for j in range(n):
            min_answer = min(min_answer,bfs(0,j))
        
        return min_answer

# DP solution
class Solution(object):
    def minFallingPathSum(self, grid):

        n = len(grid)

        def twoMins(arr):

            min1 = float('inf')
            min2 = float('inf')

            for num in arr:
                if num < min1:
                    min2 = min1
                    min1 = num
                elif num < min2:
                    min2 = num
            
            return (min1,min2)

        for i in range(1,n):
            
            min1, min2 = twoMins(grid[i-1])

            for j in range(n):
                minVal = min1
                if min1 == grid[i-1][j]:
                    minVal = min2
                
                grid[i][j] = grid[i][j] + minVal
            
        
        return min(grid[-1])
