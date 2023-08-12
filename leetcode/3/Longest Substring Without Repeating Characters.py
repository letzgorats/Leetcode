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


how to solve -> (https://letzgorats.tistory.com/entry/%EB%A6%AC%ED%8A%B8%EC%BD%94%EB%93%9Cleetcodepython-3-Longest-Substring-Without-Repeating-Characters)
                                
            
