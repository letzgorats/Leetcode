class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        answer = ""

        for t in s.split():
            answer += (t[::-1] + " ")  
        
        return answer.strip()
