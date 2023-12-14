# solution 1)

class Solution(object):
    def onesMinusZeros(self, grid):
    
        n = len(grid)
        m = len(grid[0])
    
        rows = []
        for i in range(n):
            rows.append( (grid[i].count(0), grid[i].count(1)) )
        
        trans_grid = zip(*grid)
        cols = []
        for j in range(m):
            cols.append((trans_grid[j].count(0),trans_grid[j].count(1)))

        for i in range(n):
            for j in range(m):
                grid[i][j] = rows[i][1] + cols[j][1] - rows[i][0] - cols[j][0]
        
        return grid

# solutin 2)

class Solution(object):
    def onesMinusZeros(self, grid):

        n = len(grid)
        m = len(grid[0])

        rows = []
        for i in range(n):
            rows.append( (grid[i].count(0), grid[i].count(1)) )

        cols = []
        for j in range(m):
            col0 = 0
            col1 = 0
            for i in range(n):
                if grid[i][j] == 0:
                    col0 += 1
                if grid[i][j] == 1:
                    col1 += 1
            cols.append((col0,col1))

        for i in range(n):
            for j in range(m):
                grid[i][j] = rows[i][1] + cols[j][1] - rows[i][0] - cols[j][0]
        
        return grid
