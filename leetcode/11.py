class Solution(object):
    def maxArea(self, height):

        left = 0
        right = len(height)-1
        max_amount = 0  # tentative answer

        # decide the standard height
        while(left < right):
            change_left, change_right = False, False

            if height[left] < height[right]:
                standard = height[left]
                change_left = True
            else:
                standard = height[right]
                change_right = True

            amount = (right-left) * standard
            max_amount = max(max_amount,amount) # renew the max_amount compared to original_max_amount

            if change_left :
                left += 1   # let's change the start point
            elif change_right:
                right -= 1  # let's change the end point

            # print(max_amount)
    
        return max_amount
        
        """
        :type height: List[int]
        :rtype: int
        """
