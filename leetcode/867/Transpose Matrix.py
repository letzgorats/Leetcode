class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        
        graph = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                graph[i][j] = matrix[j][i]
        
        return graph


class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(map(list,(zip(*matrix))))
