class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        max_length = 0
        count = 0
        match = {}

        for i in range(len(nums)):

            current = nums[i]

            if current == 0:
                count -= 1
            else:
                count += 1
            
            if count == 0:
                max_length = i + 1
            
            if count in match:
                max_length = max(max_length,i-match[count])
            else:
                match[count] = i
        
        return max_length
