# BFS solution - 5.26 %
from collections import deque
class Solution(object):
    def getMaximumGold(self, grid):
        
        def bfs(r,c):

            visited = [[False] * m for _ in range(n)]
            queue = deque([(r,c,grid[r][c],visited)])
            visited[r][c] = True
            max_val = 0

            while queue:
                
                r,c,val,visited = queue.popleft()
                
                max_val = max(max_val, val)
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 0 and not visited[nr][nc]:
                        new_visited = [x[:] for x in visited]
                        new_visited[nr][nc] = True
                        queue.append((nr,nc,val+grid[nr][nc],new_visited))
                        
                        
            return max_val

        n = len(grid)
        m = len(grid[0])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        ans = 0 

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans,bfs(i,j))

        return ans


# set 을 이용한 bfs solution
from collections import deque
import copy
class Solution(object):
    def getMaximumGold(self, grid):

        def bfs(r,c):
            
            queue = deque([(r, c, grid[r][c], set([(r, c)]))])
            max_val = 0

            while queue:
                
                r,c,val,visited = queue.popleft()
                max_val = max(max_val, val)
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != 0 and (nr,nc) not in visited:
                        new_visited = visited.copy()
                        new_visited.add((nr, nc))
                        queue.append((nr,nc,val+grid[nr][nc],new_visited))
                    
                        
            return max_val

        n = len(grid)
        m = len(grid[0])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        ans = 0 

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans,bfs(i,j))

        return ans



# DFS solution - 17.54%
# grid 값을 0으로 바꾸면서 방문처리를 하는 solution
class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dfs(r,c):

            if r < 0 or r >=n or c < 0 or c>= m or grid[r][c] == 0 :
                return 0
            
            # Mark this cell as visited by setting it to 0
            original_value = grid[r][c]
            grid[r][c] = 0 
            
            max_gold = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                max_gold = max(max_gold,dfs(nr,nc))
                
            # Restore the original value after DFS
            grid[r][c] = original_value
    
            return original_value + max_gold


        n = len(grid)
        m = len(grid[0])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        ans = 0 

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans,dfs(i,j))

        return ans


# visited set 이나 visited list를 사용해서도 풀 수 있다.
# visited set을 이용한 dfs solution
class Solution(object):
    def getMaximumGold(self, grid):
      
        def dfs(r,c,visited):

            if r < 0 or r >=n or c < 0 or c >= m or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))
            max_gold = 0
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                max_gold = max(max_gold,dfs(nr,nc,visited))
            
            visited.remove((r,c))
    
            return grid[r][c] + max_gold


        n = len(grid)
        m = len(grid[0])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        ans = 0 

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    ans = max(ans,dfs(i,j,set()))

        return ans


# visited list 를 이용한 dfs solution
class Solution(object):
    def getMaximumGold(self, grid):
        
        def dfs(r,c,current_gold):

            if r < 0 or r >=n or c < 0 or c >= m or grid[r][c] == 0 or visited[r][c]:
                return current_gold
            
            visited[r][c] = True
            max_gold = 0

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                max_gold = max(max_gold,dfs(nr,nc,current_gold + grid[r][c]))
            
            visited[r][c] = False
    
            return max_gold


        n = len(grid)
        m = len(grid[0])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        visited = [[False] * m for _ in range(n)]
        max_gold = 0 

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    max_gold = max(max_gold,dfs(i,j,0))

        return max_gold
