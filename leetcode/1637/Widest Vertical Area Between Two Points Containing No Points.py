class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        points = sorted(points, key = lambda x:x[0])
        # print(points)

        gap = 0
        for i in range(len(points)-1):

            gap = max(gap, points[i+1][0]-points[i][0])

        return gap
