# dp solution
class Solution:
    def minSteps(self, n: int) -> int:

        dp = [1000] * (n + 1)

        dp[1] = 0

        for i in range(2, n + 1):
            for j in range(1, 1 + i // 2):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]

# backtracking, memoization solution
class Solution:
    def minSteps(self, n: int) -> int:

        cache = {}

        def backtracking(count, paste):

            if count == n:
                return 0

            if count > n:
                return 1000

            if (count, paste) in cache:
                return cache[(count, paste)]

            # Paste
            res1 = 1 + backtracking(count + paste, paste)

            # Copy & Paste
            res2 = 2 + backtracking(count + count, count)

            cache[(count, paste)] = min(res1, res2)
            return cache[(count, paste)]

        if n == 1:
            return 0

        return 1 + backtracking(1, 1)