class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()

        return (nums[-2] * nums[-1]) - (nums[1]*nums[0])
