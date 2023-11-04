class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        
        # left_ants = [0,0,0,1,1] ->  ([0,0,1,1,0] -> [0,0,1,1,0]) -> ([0,1,1,0,0] ->[0,1,1,0,0]) -> [1,1,0,0,0] -> [1,0,0,0,0]
        # right_ants = [1,1,0,0,0] -> ([0,1,1,0,0] -> [0,1,1,0,0]) -> [0.0.1.1.0] -> [0,1,1,0,0]) -> [0,0,0,1,1] -> [0,0,0,0,1]
        
        left.append(0)
        left = max(left)

        right.append(n)
        right = min(right)

        return max(n-right,left)


class Solution(object):
    def getLastMoment(self, n, left, right):
        """
        :type n: int
        :type left: List[int]
        :type right: List[int]
        :rtype: int
        """
        
        # left_ants = [0,0,0,1,1] ->  ([0,0,1,1,0] -> [0,0,1,1,0]) -> ([0,1,1,0,0] ->[0,1,1,0,0]) -> [1,1,0,0,0] -> [1,0,0,0,0]
        # right_ants = [1,1,0,0,0] -> ([0,1,1,0,0] -> [0,1,1,0,0]) -> [0.0.1.1.0] -> [0,1,1,0,0]) -> [0,0,0,1,1] -> [0,0,0,0,1]
        
        t = 0

        for l in left:

            t = max(t,l)

        for r in right:

            t = max(t,n-r)
        
        return t
