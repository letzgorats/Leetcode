class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)+1):
            tmp = 0
            for n in nums:
                if i <= n:
                    tmp += 1
            
            if tmp == i:
                return i

        return -1
