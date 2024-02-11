class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        def dp(i,j1,j2):

            if i == n:
                return 0
            if j1 < 0 or j1 >= m or j2 < 0 or j2 >=m:
                return 0
            
            if (i,j1,j2) in memo:
                return memo[(i,j1,j2)]
            
            result = 0

            for newJ1 in [j1-1,j1,j1+1]:
                for newJ2 in [j2-1,j2,j2+1]:
                    result = max(result, dp(i+1,newJ1,newJ2))
                
            result += grid[i][j1]

            if j1 != j2:
                result += grid[i][j2]
            
            memo[(i,j1,j2)] = result

            return result

        n = len(grid)
        m = len(grid[0])

        memo = {}

        return dp(0,0,m-1)
