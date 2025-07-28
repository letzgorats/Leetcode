# solution 1 - (brute force, recursive, dfs) - (241ms,246ms) - (2024.10.18),(2025.07.28)
from typing import List
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_or = 0
        for n in nums:
            max_or |= n

        res = 0

        def dfs(i, cur_or):
            nonlocal res, max_or
            if i == len(nums):
                res += 1 if cur_or == max_or else 0
                return

            # skip i
            dfs(i + 1, cur_or)
            # include i
            dfs(i + 1, cur_or | nums[i])

        dfs(0, 0)
        return res


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_or = 0
        for n in nums:
            max_or |= n

        def dfs(i, cur_or):
            nonlocal max_or
            if i == len(nums):
                return 1 if cur_or == max_or else 0

            # skip i + include i
            return dfs(i + 1, cur_or) + dfs(i + 1, cur_or | nums[i])

        return dfs(0, 0)

# solution 2 - memoization - (214ms,307ms) - (2024.10.18),(2025.07.28)
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_or = 0
        for n in nums:
            max_or |= n

        cache = [[-1] * (max_or + 1) for _ in range(len(nums))]

        def dfs(i, cur_or):
            nonlocal max_or
            if i == len(nums):
                return 1 if cur_or == max_or else 0

            if cache[i][cur_or] != -1:
                return cache[i][cur_or]

            cache[i][cur_or] = (
                    dfs(i + 1, cur_or) +
                    dfs(i + 1, cur_or | nums[i])
            )
            return cache[i][cur_or]

        return dfs(0, 0)

# solution 3 - bottom up solution,dp - (19ms) - (2024.10.18)
from collections import defaultdict
from copy import deepcopy
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        dp = defaultdict(int)  # (key = cur_or ,val=cnt)
        dp[0] = 1
        max_or = 0

        for n in nums:
            new_dp = deepcopy(dp)
            for cur_or, cnt in dp.items():
                new_or = n | cur_or
                new_dp[new_or] += cnt

            dp = new_dp
            max_or |= n

        return dp[max_or]

# solution 3 - bitmask - (1260ms,1483ms) - (2024.10.18), (2025.07.28)
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        max_or = 0

        for n in nums:
            max_or |= n

        length = len(nums)
        res = 0

        for subset in range(1, 2 ** length):
            cur_or = 0
            for i in range(length):
                if (1 << i) & subset:
                    cur_or |= nums[i]

            res += 1 if cur_or == max_or else 0

        return res
