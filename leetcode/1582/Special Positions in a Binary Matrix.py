class Solution(object):
    def numSpecial(self, mat):
        
        answer = 0
        m = len(mat)
        n = len(mat[0])
        candi = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    candi.append((i,j))

        while candi:
            check = True
            r,c  = candi.pop()

            for i in range(m):
                if i != r and mat[i][c] == mat[r][c]:
                    check = False
                    break
            
            if not check :
                continue
            
            for j in range(n):
                if j != c and mat[r][j] == mat[r][c]:
                    check = False
 
            if check:
               answer += 1 

        return answer


            
        
        
