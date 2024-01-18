class Solution(object):
    def climbStairs(self, n):

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

        # 4 

        # 1+1+1+1
        # 1+2+1
        # 1+1+2
        # 2+1+1
        # 2+2


# second sol
class Solution:
    def climbStairs(self, n: int) -> int:

        # 1 
        # 2 -> 2 , 1 + 1
        # 3 -> 1 + 2 , 1 + 1 + 1, 2 + 1
        # 4 -> 2 + 2, 1 + 1 + 2
        #   -> 2 + 1 + 1, 1 + 1 + 1 + 1, 1 + 2 + 1
        # dp[2] + dp[3]

        dp = (n+1) * [0]
        dp[0] = 1
        dp[1] = 1 
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
