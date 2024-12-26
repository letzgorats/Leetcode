# solution 1 - backtracking, TLE
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp = {} # (index,cur_sum)

        def backtracking(idx, cur_sum):
            if idx == len(nums):
                return 1 if target == cur_sum else 0

            return (
                    backtracking(idx + 1, cur_sum + nums[idx]) +
                    backtracking(idx + 1, cur_sum - nums[idx])
            )

        return backtracking(0, 0)


# solution 2 - dp, backtracking
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}  # (index,cur_sum)

        def backtracking(idx, cur_sum):
            if (idx, cur_sum) in dp:
                return dp[(idx, cur_sum)]

            if idx == len(nums):
                return 1 if target == cur_sum else 0

            dp[(idx, cur_sum)] = (
                    backtracking(idx + 1, cur_sum + nums[idx]) +
                    backtracking(idx + 1, cur_sum - nums[idx])
            )
            return dp[(idx, cur_sum)]

        return backtracking(0, 0)

# solution 3 - 2D dp
from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1  # (0 elements, 0 sum) -> 1 way
        # 1 way to sum to zero with first 0 elements

        for i in range(len(nums)):

            for cur_sum, count in dp[i].items():
                dp[i + 1][cur_sum + nums[i]] += count
                dp[i + 1][cur_sum - nums[i]] += count

        return dp[len(nums)][target]


# solution 4 - 2D dp
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int)

        dp[0] = 1  # (0 sum) -> 1 way
        # 1 way to sum to zero with first 0 elements

        for i in range(len(nums)):

            next_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                next_dp[cur_sum + nums[i]] += count
                next_dp[cur_sum - nums[i]] += count
            dp = next_dp

        return dp[target]
