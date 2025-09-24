# solution 1 - (bottom up, dynamic programming) - (7ms) - (2025.09.26)
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j + 1], triangle[i + 1][j])

        return triangle[0][0]