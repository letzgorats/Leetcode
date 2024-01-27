class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp, mod = [1]+[0] * k, 1000000007
        
        for i in range(n):
            tmp, sm = [], 0
            for j in range(k + 1):
                sm+= dp[j]
                if j-i >= 1: sm-= dp[j-i-1]
                sm%= mod
                tmp.append(sm)
            dp = tmp
          
        return dp[k]
