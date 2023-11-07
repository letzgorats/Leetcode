# my sol 
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        return bin(n).count('1')


# sol 2

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        answer = 0
        mask = 1

        for i in range(32):
            if (n & mask) != 0: # check 1
                answer += 1
            mask <<= 1
        
        return answer

# sol 3
class Solution(object):
    def hammingWeight(self, n):


        ans = 0
        while n :
            ans += (n%2)
            n >>= 1
        
        return ans
