class Solution(object):
    def findMaxK(self, nums):
        max_val = -1
        
        for n in nums:

            if n > 0:
                if -n in nums and n > max_val:
                    max_val = n
        
        return max_val
