# solution 1 - (math) - (14ms) - (2023.10.23)
import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and math.log(n,4) == int(math.log(n,4))

# solution 2 - (bitwise) - (0ms) - (2025.08.15)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        p = str(bin(n)[2:])

        if n < 0 or p.count('1') != 1:
            return False

        for i in range(0, n.bit_length(), 2):

            if (n >> i) & 1:
                return True

        return False