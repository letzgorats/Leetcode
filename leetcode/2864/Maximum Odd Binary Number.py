class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # odd = odd + even
        # we have to put '1' on the last position, which means 1(odd)
        # because the other position means even number(2,4,8,16,...)

        answer = ''
        
        cnt = s.count('1') - 1

        for i in range(len(s)-1):
            if cnt > 0:
                answer += '1'
                cnt -= 1
            else:
                answer += '0'
        
        return answer + '1'

        
