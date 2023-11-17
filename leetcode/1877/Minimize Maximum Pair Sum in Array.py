class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        
        nums = sorted(nums)

        left = 0
        right = len(nums)-1
        current = nums[0] + nums[-1]

        while left <= right:
            current = max(nums[left]+nums[right],current)
            left += 1
            right -= 1

        # print(current)

        return current
