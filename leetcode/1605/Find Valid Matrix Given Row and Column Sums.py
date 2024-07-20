# solution 1
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        matrix = [[0] * m for _ in range(n)]

        while sum(rowSum) != 0 and sum(colSum) != 0:
            x = min([v for v in rowSum if v > 0] + [v for v in colSum if v > 0])
            xi = rowSum.index(min([v for v in rowSum if v > 0]))
            xj = colSum.index(min([v for v in colSum if v > 0]))

            matrix[xi][xj] = x
            rowSum[xi] -= x
            colSum[xj] -= x

        return matrix

# solution 2
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        n = len(rowSum)
        m = len(colSum)
        dp = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                dp[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= dp[i][j]
                colSum[j] -= dp[i][j]

        return dp