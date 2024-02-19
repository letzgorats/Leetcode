# set solution
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power_of_three = set(3**i for i in range(31))
        return n > 0 and n in power_of_three


# recursion solution
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 :
            return False
        if n == 1 :
            return True
        return n > 0 and n % 3 == 0 and self.isPowerOfThree(n//3)

# range solution
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return n > 0 and 3**19 % n == 0
        
