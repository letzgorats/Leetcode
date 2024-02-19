# iterative solution
# Time : O(nlogn)  / Space : O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(31):
            if 2 ** i == n:
                return True
        
        return False


# Follow up: without loops/recursion - Pattern in Power of 2
# Time : O(nlogn)  / Space : O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and bin(n).count('1') == 1

# Math solution
# Time : O(1)  / Space : O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and (1<<31) % n == 0


# Pre-Compute all powers of 2 solution
# Time : O(1)  / Space : O(1)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power_of_2 = set(2**i for i in range(31))
        return n in power_of_2
