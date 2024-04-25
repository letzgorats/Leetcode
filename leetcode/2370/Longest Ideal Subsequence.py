class Solution(object):
    def longestIdealString(self, s, k):
        n = len(s)
        dp = [0] * 128
        max_len = 0

        for alpha in s:

            start = max(0,ord(alpha)-k)
            end = min(127,ord(alpha)+k)

            max_dp = 0
            for i in range(start, end+1):
                max_dp = max(max_dp,dp[i])
            
            dp[ord(alpha)] = max_dp + 1
            max_len = max(max_len, dp[ord(alpha)])
        
        return max_len

# others solution

class Solution(object):
    def longestIdealString(self, s, k):
        n = len(s)
        dp = [0]*26
        dp[ord(s[0])-97] += 1

        for i in range(1, n):
            ordi = ord(s[i]) - 97
            dp[ordi] = 1 + max(dp[max(0, ordi-k):min(26, ordi+k+1)])
        
        return max(dp)

def longestIdealString(self, s, k):
    dp = [0] * 128
    for c in s:
        i = ord(c)
        dp[i] = max(dp[i - k : i + k + 1]) + 1
    return max(dp)
