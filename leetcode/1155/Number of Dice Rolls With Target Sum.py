class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        
        mod = 10**9 + 7
        
        # dp[i][j]는 i개의 주사위를 사용하여 합 j를 만들 수 있는 방법의 수
        dp = [[0] * (target + 1) for _ in range(n + 1)]
    
        # 0개의 주사위를 사용하여 합 0을 만들 수 있는 방법의 수 = 1
        dp[0][0] = 1


        for i in range(1,n+1):
            for j in range(1,target+1):
                for m in range(1,min(k,j)+1):
                    dp[i][j] = (dp[i][j] + dp[i-1][j-m]) % mod

        return dp[n][target]
