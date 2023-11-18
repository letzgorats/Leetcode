class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        currentSum = 0
        freq = 0

        left = 0
        for right in range(len(nums)):
            currentSum += nums[right]

            while currentSum + k < nums[right] * (right-left+1):
                currentSum -= nums[left]
                left += 1
            
            freq = max(freq, right-left + 1)
        
        return freq
