class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # cnt = 0

        # for n in nums:

        #     if cnt < 2 or n != nums[cnt-2]:
        #         nums[cnt] = n
        #         cnt += 1
        
        # return cnt

        i = 2 
        for j in range(2,len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
            # print(nums)
        return i

        
