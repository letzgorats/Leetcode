# 98 %
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums,reverse=True)
        total = sum(nums)
        # 50 12 5 3 2 1 1
        # 7 5 1 1
        val = -1
        for i in range(len(nums[:-2])):
            if nums[i] < total-nums[i]:
                val = total
                break
            total -= nums[i]
        return val

# 95 %
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums,reverse=True)
        # 50 12 5 3 2 1 1
        # 7 5 1 1
        val = -1
        for i in range(len(nums[:-2])):
            if nums[i] < sum(nums[i+1:]):
                val = sum(nums[i:])
                break

        return val
        
        

        
