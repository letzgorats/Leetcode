# solution 1 - (Chebyshev Distance) - (30ms,4ms) - (2023.12.03),(2026.01.13)
class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        answer = 0
        for i in range(len(points)-1):

            x1, y1 = points[i][0], points[i][1] 
            x2, y2 = points[i+1][0], points[i+1][1] 

            # if x1-y1 == x2-y2:
            #     answer += abs(x1-x2)
            # else:
            #     
            answer += max(abs(x1-x2),abs(y1-y2))
                # answer += int(sqrt(abs(x1-x2) ** 2 + abs(y1-y2) ** 2))
                
        return answer
            
            
        
