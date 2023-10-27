# naive
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

# two pointer
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def compare(l,r):

            while l >=0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]


        answer = ""

        for i in range(len(s)):
            
            odd = compare(i,i)
            if len(odd) > len(answer):
                answer = odd
            even = compare(i,i+1)
            if len(even) > len(answer):
                answer = even
    
        return answer
        
