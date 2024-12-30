# solution 1 - backtracking,recursive,memoization(top-down)
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        mod = 10 ** 9 + 7
        dp = {}

        def backtracking(length):
            if length > high:
                return 0
            if length in dp:
                return dp[length]

            dp[length] = 1 if length >= low else 0
            dp[length] += backtracking(length + zero) + backtracking(length + one)

            return dp[length] % mod

        return backtracking(0)

# solution 2 - dp, tabulation(bottom-up)
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {0: 1}  # length -> num of strs
        mod = 10 ** 9 + 7

        for i in range(1, high + 1):
            dp[i] = (dp.get(i - one, 0) + dp.get(i - zero, 0))

        return sum([dp[i] for i in range(low, high + 1)]) % mod
