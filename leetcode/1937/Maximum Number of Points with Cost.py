# TLE code - O (n*m*m)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        m = len(points[0])

        dp = [[0] * m for _ in range(n)]

        for j in range(m):
            dp[0][j] = points[0][j]

        for i in range(1, n):
            for j in range(m):
                for k in range(m):
                    dp[i][j] = max(
                        dp[i - 1][k] + points[i][j] - abs(j - k),
                        dp[i][j]
                    )

        return max(dp[n - 1])


# solution - O(n*m)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        m = len(points[0])

        # Initialize dp array with the first row
        dp = points[0]

        for i in range(1, n):
            left = [0] * m
            right = [0] * m

            # Fill the left array
            left[0] = dp[0]
            for j in range(1, m):
                left[j] = max(left[j - 1] - 1, dp[j])

            # Fill the right array
            right[m - 1] = dp[m - 1]
            for j in range(m - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, dp[j])

            # update dp for current row
            for j in range(m):
                dp[j] = points[i][j] + max(left[j], right[j])

        return max(dp)
