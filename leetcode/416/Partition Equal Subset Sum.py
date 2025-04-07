# solution 1 - dp, knapsack,subsets - 467ms - (2025.04.07)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False  # total 이 홀수라면 두 부분을 똑같이 나눌 수 없다.

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True  # 아무것도 고르지 않으면 합이 0 이니까 True

        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True  # dp[i] 를 만들 수 있으면 True

        return dp[target]  # target 이 True 라면 똑같은 합의 두 부분으로 나눌 수 있다는 뜻