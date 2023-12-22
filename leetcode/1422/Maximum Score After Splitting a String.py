class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0 
        for i in range(len(s)-1):

            answer = max(answer,s[:i+1].count('0')+s[i+1:].count('1'))

        return answer
