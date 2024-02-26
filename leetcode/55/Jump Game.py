# neither backtracking nor DP

# O(n) solution - greedy
# (https://www.youtube.com/watch?v=Yan0cv2cLy8)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # initial goal
        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
