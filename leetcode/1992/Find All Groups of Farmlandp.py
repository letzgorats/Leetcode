from collections import deque

class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []
        
        def bfs(r,c):

            queue = deque([(r,c)])
            tmp = [r,c]
            land[r][c] = 0

            while queue:

                r, c = queue.popleft()
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1:
                        land[nr][nc] = 0
                        queue.append((nr,nc))
            
            tmp.append(r)
            tmp.append(c)

            return tmp


        n = len(land)
        m = len(land[0])
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]

        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    answer.append(bfs(i,j))
        
        return answer
