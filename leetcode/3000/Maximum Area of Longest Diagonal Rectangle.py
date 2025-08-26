# solution 1 - (math,array) - (0ms) - (2025.08.26)
from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:

        max_len_square = 0
        answer = -1
        for a, b in dimensions:

            if max_len_square < a * a + b * b:
                max_len_square = a * a + b * b
                answer = a * b
            elif max_len_square == (a * a + b * b):
                answer = max(answer, a * b)

        return answer