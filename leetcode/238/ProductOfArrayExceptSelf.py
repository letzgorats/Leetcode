class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # left 
        answer = [] 
        p = 1
        for idx in range(len(nums)):
            answer.append(p)
            p *= nums[idx]

        # [1,2,4,12]
        # [24,24,16,12]

        # right
        # right = []
        p = 1
        for idx in range(len(nums)-1,-1,-1):
            answer[idx] = p * answer[idx]
            p *= nums[idx]
        # print(p)
     
        return answer
