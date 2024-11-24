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

