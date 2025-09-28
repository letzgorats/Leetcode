# solution 1 - (dynamic programming) - (23ms) - (2025.09.29)
from typing import List
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        # 점화식(아이디어): i < k < j 인 중간 꼭짓점 k를 마지막 삼각형의 세 꼭짓점 중 하나로 택하면
        # dp[i][j] = min over k ( dp[i][k] + dp[k][j] + values[i]*values[k]*values[j] )
        # 길이 2(즉, 삼각형 미만) 구간은 비용 0, 길이 3(정확히 삼각형)은 한 번의 곱만 더하면 됨.

        n = len(values)
        dp = [[0] * n for _ in range(n)]

        # len은 i 와 j 사이의 간격(최소 2부터 : 삼각형 이상)
        for length in range(2, n):
            for i in range(0, n - length):
                j = i + length
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + values[i] * values[k] * values[j]
                    if cost < dp[i][j]:
                        dp[i][j] = cost

        return dp[0][n - 1]
