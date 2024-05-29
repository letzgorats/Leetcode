class Solution(object):
    def numSteps(self, s):
        
        answer = 0 
        while s != '1':

            num = int(s,2)
            if num % 2 == 0:
                num //= 2
            else:
                num += 1

            answer += 1
            s = bin(num)[2:] 
        
        return answer
