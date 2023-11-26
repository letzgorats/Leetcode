class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1,n):
            for j in range(m):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]

        answer = 0

        for row in matrix:
            row.sort(reverse=True)
            for j in range(m):
                answer = max(answer, row[j] * (j+1))
        
        # print(matrix)
        return answer
  
