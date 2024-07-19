class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        n = len(matrix)
        m = len(matrix[0])

        min_rows = [min(row) for row in matrix]
        # print(min_rows)
        max_cols = [[0] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                max_cols[j][i] = matrix[i][j]
        max_cols = [max(row) for row in max_cols]
        # print(max_cols)

        return list(set(min_rows) & set(max_cols))

# max_cols = [max(col) for col in zip(*matrix)] 는
# 2차원 리스트(matrix)를 열(column) 단위로 그룹화하는 데 사용
# -> zip(*matrix)의 결과는 각 열의 요소들을 하나씩 묶어서 새로운 튜플로 변환