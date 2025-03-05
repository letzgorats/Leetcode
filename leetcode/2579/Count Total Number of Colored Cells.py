# solution 1 - math - (0ms) - (2025.03.05)
class Solution:
    def coloredCells(self, n: int) -> int:

        # 1 -> 1
        # 2 -> 5 (1 + 4*(n-1))
        # 3 -> 13 (5+ 8)
        # 4 -> 25 (13+12)

        # an = 1,2,3,4,...
        # bn =  4,8,12,...

        # an = 1 + sigma(k=1,n-1)*4k
        # an = 1 + 4 * ((n-1)*n//2) = 1 + n*(n-1)*2
        return 1 + n*(n-1)*2

# solution 2 - math - (254ms) - (2025.03.05)
class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 -> 1
        # 2 -> 5 (1 + 4*(n-1))
        # 3 -> 13 (5+ 8)
        # 4 -> 25 (13+12)

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + 4 * (i - 1)
        # print(dp)
        return dp[n]
