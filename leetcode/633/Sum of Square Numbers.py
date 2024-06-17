# solution - hash, dp
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        case = set()

        for i in range(int(math.sqrt(c)) + 1):

            if i * i == c or i * i == c - i * i or c - i * i in case:
                return True
            else:
                case.add(i * i)
            # print(case)

        return False


# solution - two pointers
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """

        left, right = 0, int(math.sqrt(c))
        current_sum = 0

        while left <= right:

            current_sum = left ** 2 + right ** 2

            if current_sum == c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1

        return False
