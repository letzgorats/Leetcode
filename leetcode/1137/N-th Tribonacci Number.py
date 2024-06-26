class Solution(object):
    
    def tribonacci(self, n):

        triresult = [0,1,1]

        for i in range(3,n+1):
            triresult[i%3] = sum(triresult)
        
        return triresult[n%3]


class Solution:
    def tribonacci(self, n: int) -> int:

        dp = [0,1,1]

        for i in range(3,n+1):

            dp.append(dp[i-3] + dp[i-2]+ dp[i-1])

        return dp[n] 



class Solution(object):
    def tribonacci(self, n):

        dp = [0] * 38
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        for i in range(3,n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        
        return dp[n]




