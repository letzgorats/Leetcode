class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == "0" or not s :
            return 0

        # 1205

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1

        for i in range(2,n+1):

            print(s[:i])
            if s[i-1] != '0':
                dp[i] += dp[i-1]
   
            # print(dp)
            # print()
            print(s[i-2:i])
            if 10 <= int(s[i-2:i]) <= 26:

                dp[i] += dp[i-2]
            # print(dp)
            # print()
                
        return dp[n]     
