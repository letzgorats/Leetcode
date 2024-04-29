class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0
        tmp = nums[0]
        for n in nums[1:]:
            tmp ^= n
        
        diff = tmp ^ k

        return bin(diff)[2:].count('1')
