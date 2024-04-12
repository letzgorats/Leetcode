# TLE solution
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        answer = 0

        for i in range(1,len(height)-1):
            left_max = max(height[:i])
            right_max = max(height[i+1:])

            compare = min(left_max,right_max)

            if height[i] < compare:
                answer += compare-height[i]
        
        return answer

# two pointer solution

class Solution(object):
    def trap(self, height):

        answer = 0
        
        left, right = 0, len(height)-1
        leftmax = height[left]
        rightmax = height[right]

        while left < right : 

            if leftmax < rightmax:
                left += 1
                leftmax = max(leftmax, height[left])
                answer += max(0, leftmax-height[left])
            else:
                right -= 1
                rightmax = max(rightmax, height[right])
                answer += max(0,rightmax-height[right])
        
        return answer
