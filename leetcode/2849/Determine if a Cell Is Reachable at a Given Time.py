class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """

        xDistance = abs(sx-fx)
        yDistance = abs(sy-fy)
        
        extra = abs(yDistance-xDistance)
        
        minDist = min(xDistance,yDistance) + extra

        if minDist == 0:
            return t != 1

        return minDist <= t


# to undestand visit to below link
# https://www.youtube.com/watch?v=2DNQHCls0Kw
