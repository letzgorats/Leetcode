class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """

        answer = 0
        
        for i in range(len(s)-1):

            pre = ord(s[i])
            now = ord(s[i+1])

            answer += abs(now-pre)
        
        return answer
