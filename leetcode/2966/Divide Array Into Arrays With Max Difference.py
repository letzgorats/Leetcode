class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        n = len(nums)
        nums = sorted(nums)
        answer = [nums[:3]]

        st = nums[0]
        for i in range(3,n,3):
            # print(i,answer)
            if (nums[i-1] - st) <= k:
                answer.append(nums[i:i+3])
                st = nums[i]
            else:
                return []

        if answer[-1][0] + k < answer[-1][2] :
            return []
        

        return answer

        
        
