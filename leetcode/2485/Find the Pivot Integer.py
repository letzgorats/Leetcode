class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        prefixSum = 0
        suffixSum = (1+n) * n // 2
        
        for i in range(1,n+1):

            prefixSum += i
            if prefixSum == suffixSum:
                return i
            suffixSum -= i

        return -1





