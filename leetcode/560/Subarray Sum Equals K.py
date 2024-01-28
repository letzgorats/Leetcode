class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        accumulation = {0:1}
        cnt = 0
        currentSum = 0 

        for i,n in enumerate(nums):
            currentSum += n

            if (currentSum-k) in accumulation:
                cnt += accumulation[currentSum-k]
            
            accumulation[currentSum] = accumulation.get(currentSum,0) + 1
            print(accumulation)
            print(cnt)
     
        return cnt
