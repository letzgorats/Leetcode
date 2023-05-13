class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accumulate = 0
        for idx, num in enumerate(nums):
            accumulate += num
            nums[idx] =  accumulate
        return nums
