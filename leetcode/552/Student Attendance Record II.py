class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        mod = 10**9 + 7


        not_acceptable = ["LLL"]
        # A 두번은 나중에 검사

        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]
        
        dp[0][0][0] = 1

        for i in range(n+1):

            for j in range(2):

                for k in range(3):

                    # 'P'를 추가하는 경우
                    dp[i][j][0] += (dp[i-1][j][k] % mod)

                    # 'L'을 추가하는 경우
                    if k > 0 :
                        dp[i][j][k] += (dp[i-1][j][k-1] % mod)

                    # 'A'를 추가하는 경우
                    if j > 0 :
                        dp[i][1][0] += (dp[i-1][0][k] % mod)
        
        res = 0
        for j in range(2):
            for k in range(3):
                res += dp[n][j][k]
        
        
        return res % mod
