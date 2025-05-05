# solution 1 - (dp, math) - (0ms) - (2025.05.05)
class Solution:
    def numTilings(self, n: int) -> int:

        mod = 10 ** 9 + 7
        if n <= 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5

        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 5

        for i in range(4, n + 1):
            dp[i] = (
                            dp[i - 1] * 2  # 1 vertical / 2 horizontals at columns i
                            + dp[i - 3]  # 2 mirrored L-shaped trominoes in [i-2,i]
                    ) % mod

        return dp[n]
'''
5 = 2 * 2 + 1

11 = 5 * 2 + 1

24 = 11 * 2 + 2

53 = 24 * 2 + 5

117 = 53 * 2 + 11

A[N] = A[N-1] * 2 + A[N-3]
'''