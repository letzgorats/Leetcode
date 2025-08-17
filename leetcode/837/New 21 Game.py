# TLE - (2025.08.17)
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, maxPts + 1):
                if i - j >= 0 and i - j < k:
                    dp[i] += dp[i - j] / maxPts

        return sum(dp[k:])


# solution 1 - (dp,math) - (24ms) - (2025.08.17)
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        dp = [0] * (n + 1)
        dp[0] = 1
        s = 1 if k > 0 else 0

        for i in range(1, n + 1):
            dp[i] = s / maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]

        return sum(dp[k:])
