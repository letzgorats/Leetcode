class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 4:
            return 0

        nums.sort()
        l, r = 0, len(nums) - 4
        answer = max(nums) - min(nums)

        for i in range(4):
            diff = nums[r] - nums[l]
            r += 1
            l += 1
            answer = min(diff, answer)

        return answer