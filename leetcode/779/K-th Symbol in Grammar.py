class Solution(object):
    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # 0 = 01
        # 1 = 10

        diff = True

        n = 2 ** (n-1)

        while n != 1:

            n //= 2

            if k > n :

                k -= n 

                diff = not diff

        return 0 if diff else 1
