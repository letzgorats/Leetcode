# first
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


solution 2 try)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        zero_idx = []
        for i,n in enumerate(nums):
            if n == 0:
                zero_idx.append(i)
        
        if len(zero_idx) >= 2:
            return [0] * len(nums)
        
        total = 1
        for x in nums:
            if x != 0:
                total *= x

        answer = [0] * len(nums)
        if zero_idx :
            answer[zero_idx[0]] = total
            return answer

        answer = []
        for n in nums:
            answer.append(total // n)

        return answer
