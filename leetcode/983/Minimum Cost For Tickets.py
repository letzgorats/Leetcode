# solution 1 - top down,recursive
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = {}
        def dfs(i):
            if i == len(days):
                return 0

            if i in dp:
                return dp[i]

            dp[i] = float('inf')
            for cost, duration in zip(costs, [1, 7, 30]):
                j = i
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dfs(j))

            return dp[i]

        return dfs(0)


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = {len(days): 0}

        def dfs(i):
            if i in dp:
                return dp[i]

            dp[i] = float('inf')
            for cost, duration in zip(costs, [1, 7, 30]):
                j = i
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dfs(j))

            return dp[i]

        return dfs(0)


# solution 2 - bottom up
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [0] * (len(days) + 1)

        for i in reversed(range(len(days))):
            dp[i] = float('inf')
            j = i
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + dp[j])

        return dp[0]
