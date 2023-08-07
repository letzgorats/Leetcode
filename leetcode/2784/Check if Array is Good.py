class Solution(object):
    def isGood(self, nums):
      
        max_num = max(nums)
        nums = sorted(nums)
        
        if len(nums) == max_num+1:            # length check

            for i,num in enumerate(nums[:-1]):

                if nums[0] != 1:  # the array must start from number 1
                    return False
                else:
                    if (i == len(nums)-2):    # at the last, compared to the real last one.. if its the same, return True
                        if nums[-1] == num:
                            return True
                    if nums[i+1] == (num + 1):
                        continue
                        
                    else:                  # otherwise, return False
                        return False
        else:
            return False
