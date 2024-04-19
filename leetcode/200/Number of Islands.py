from collections import deque

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def bfs(r,c):

            queue = deque([(r,c)])
            visited[r][c] = True
            grid[r][c] = "0"

            while queue:

                r,c = queue.popleft()
                for d in range(4):
                    nr , nc = r + dr[d], c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m :
                        if not visited[nr][nc] and grid[nr][nc] == "1":
                            queue.append((nr,nc))
                            visited[nr][nc] = True
                            grid[nr][nc] = "0"
        
        n = len(grid)
        m = len(grid[0])
        visited = [[False] * m for _ in range(n)]
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        answer = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i,j)
                    answer += 1

        return answer
