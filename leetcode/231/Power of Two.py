# iterative solution
# Time : O(nlogn)  / Space : O(1) - (2024.02.19)
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
# Time : O(nlogn)  / Space : O(1) - (2024.02.19)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and bin(n).count('1') == 1

# Math solution
# Time : O(1)  / Space : O(1) - (2024.02.19)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and (1<<31) % n == 0


# Pre-Compute all powers of 2 solution
# Time : O(1)  / Space : O(1) - (2024.02.19)
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        power_of_2 = set(2**i for i in range(31))
        return n in power_of_2


# solution 5 - (bit manipulation) - (0ms) - (2025.08.09)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n > 0 and n & (n - 1) == 0:
            return True

        return False
'''
n 이 2의 승수라면, 항상 이진수는 1개인데, 
n-1 과 and 연산을 하게 되면, 0 이 된다는 성질을 이용
'''
