class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        stack = []
        n = len(heights)

        answer = 0
        for idx,d in enumerate(heights):
            
            while stack and stack[-1][1] > d:
                w, h = stack.pop()
                width = idx if not stack else idx-stack[-1][0]-1
                answer = max(width * h, answer)
            
            stack.append((idx,d))

        while stack:
            w, h = stack.pop()
            width = n if not stack else n-stack[-1][0]-1
            answer = max(width * h, answer)
        
        return answer


# w = i - 1 - stack[-1]: Since the stack is always in ascending order, 
# i-1 represents the right boundary of the rectangle being considered, 
# and stack[-1] represents its left boundary. 
# The width is calculated by subtracting these two boundaries.


# solution 2 ( little bit faster )
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()

        return ans

