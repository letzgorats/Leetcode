# dfs + memoziation(top-down)

class Solution(object):
    def minFallingPathSum(self, matrix):

        def backtracking(i,j):

            # 범위를 벗어나는 경우 무한대 반환
            if i < 0 or i >= n or j < 0 or j >= n:
                return float('inf')

            # 마지막 행에 도달한 경우
            if i == n - 1:
                return matrix[i][j]

            # 이미 계산된 값이 있다면 재사용
            if memo[i][j] is not None:
                return memo[i][j]

            # 모든 가능한 다음 위치에 대해 재귀 호출
            down = matrix[i][j] + backtracking(i + 1, j)
            down_left = matrix[i][j] + backtracking(i + 1, j - 1)
            down_right = matrix[i][j] + backtracking(i + 1, j + 1)

            # 최소값을 메모이제이션하고 반환
            memo[i][j] = min(down, down_left, down_right)
            return memo[i][j]

        n = len(matrix)
        memo = [[None] * n for _ in range(n)] # 메모이제이션 테이블
        
        # 첫 행의 모든 위치에서 시작하는 경우를 탐색
        return min(backtracking(0, j) for j in range(n))


# memoziation(bottom-up)

from collections import deque

class Solution(object):
    def minFallingPathSum(self, matrix):

        n = len(matrix)
        
        # 첫 번째 행 아래의 각 행에 대해 계산
        for i in range(1, n):
            for j in range(n):
                # 왼쪽 대각선 아래, 바로 아래, 오른쪽 대각선 아래 중 최소값을 찾아서 현재 값과 더함
                left = matrix[i-1][j-1] if j > 0 else float('inf')
                down = matrix[i-1][j]
                right = matrix[i-1][j+1] if j < n - 1 else float('inf')
                print(left,down,right)
                matrix[i][j] += min(left, down, right)
                print(matrix[i][j])
            
        # 마지막 행에서 최소값을 찾음
        return min(matrix[n-1])



