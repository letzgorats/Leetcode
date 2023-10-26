class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        count = 0
        arr = sorted(arr)

        MOD = 10**9 + 7
    
        # 2 3 6 36 
        
        dp = {x:1 for x in arr}
    

        for idx, num in enumerate(arr):
            for j in range(idx):
                if not(num % arr[j]) and (num//arr[j]) in dp:
                    dp[num] += dp[arr[j]] * dp[num//arr[j]]
                    dp[num] %= MOD

        return sum(dp.values()) % MOD
