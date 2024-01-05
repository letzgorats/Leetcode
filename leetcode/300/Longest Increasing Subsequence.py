class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        dp = [1] * (n)

        for i in range(n):
            for j in range(i+1,n):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
    
        return max(dp)
