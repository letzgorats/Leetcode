class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        answer = ""
        longest = 1
        
        for i in range(len(s)):
            for j in range(1,len(s)+1):
                if len(s[i:j]) < longest:
                    continue
                if s[i:j] == s[i:j][::-1]:
                    answer = s[i:j]
                    longest = len(answer)
        
        
        return answer
