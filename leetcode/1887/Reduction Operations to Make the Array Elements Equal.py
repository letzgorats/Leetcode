class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # [5,1,3]
        
        # [3,3,2,2,1,1] - 0
        # [2,2,2,2,1,1] - 2
        # [1,1,1,1,1,1] - 6
       


        nums.sort(reverse=True)
        answer = 0
        
        idx = 0 
        while idx < len(nums)-1:

            if nums[idx] != nums[idx+1]:
                answer += (idx+1)
            idx += 1        
            
        return answer
