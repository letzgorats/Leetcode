# set solution - (2024.02.19)
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power_of_three = set(3**i for i in range(31))
        return n > 0 and n in power_of_three


# recursion solution - (2024.02.19)
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

# range solution - (2024.02.19)
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return n > 0 and 3**19 % n == 0
        

# solution 1 - (iterative) - (55ms) - (2025.08.13)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        for i in range(31):
            if n == 3 ** i:
                return True

        return False

# solution 2 - (math) - (4ms) - (2025.08.13)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (3 ** 19) % n == 0
