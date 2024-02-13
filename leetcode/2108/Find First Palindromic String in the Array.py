class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for w in words:
            for i in range(len(w)):
                if w[i] != w[len(w)-1-i]:
                    break
            
            else:
                return w
        
        
        return ""



class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for w in words:
            if w == w[::-1]:
                return w
        
        return ""
