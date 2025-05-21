# solution 1 - (matrix) - (2ms) - (2025.05.21)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])
        zeros = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zeros.add((i, j))

        for i, j in zeros:
            for k in range(m):
                matrix[i][k] = 0
            for k in range(n):
                matrix[k][j] = 0
