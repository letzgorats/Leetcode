class Solution(object):
  
    def islandPerimeter(self, grid):

        answer = 0
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
        n = len(grid)
        m = len(grid[0])

        def cal_stripes(r,c):
        
            tmp = 4
            for d in range(4):

                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    tmp -= 1

            return tmp

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    answer += cal_stripes(i,j)


        return answer 
