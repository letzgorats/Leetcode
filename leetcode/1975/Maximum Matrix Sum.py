# solution 2 - (greedy,matrix) - (115ms) - (2026.01.05)
from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        absolute_val = 0
        cnt = 0
        smallest_val = float('inf')
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:  # negative
                    cnt += 1
                absolute_val += abs(matrix[i][j])
                smallest_val = min(smallest_val, abs(matrix[i][j]))
        if cnt % 2 == 0:  # even-negative
            return absolute_val
        else:  # odd-negative
            return absolute_val - 2 * smallest_val

# solution 1 - (greedy,.matrix) - (117ms) - (2024.11.24)

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        absolute_sum = 0
        cnt = 0
        smallest_abs = float('inf')
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < 0:
                    cnt += 1
                absolute_sum += abs(matrix[i][j])
                smallest_abs = min(smallest_abs, abs(matrix[i][j]))
        # print(cnt)

        if cnt % 2 == 0:  # even
            return absolute_sum
        else:  # odd
            # print(min_negative)
            return absolute_sum - smallest_abs * 2

