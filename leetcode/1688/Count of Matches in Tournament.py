class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        answer = 0
        while n != 1:

            answer += (n // 2)
            n -= (n//2)
        
        return answer
