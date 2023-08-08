class Solution(object):
    def lengthOfLongestSubstring(self, s):

        if s == "":
            return 0

        dp = [1] * (len(s)+1)

        # dp = [1,1,1,1,1,1,1,1,1]
        tmp = s[0]
        for i in range(1,len(s)):
           
            if s[i] not in tmp:
                tmp += s[i]
                dp[i] += dp[i-1]

            else:
                tmp = tmp[tmp.index(s[i])+1:] + s[i]
                dp[i] = len(tmp)

        return max(dp)

                                
            
