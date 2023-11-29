class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums[:] = sorted(set(nums))
  

        print(nums)
        
        return len(nums)


# Q. How does nums[:] count as the same list object as nums? Isn't nums[:] a deepcopy of nums?
# A. Nope, it's replacing it in-place.

# l = [1, 2, 3]
# id(l)
# 139722190642240
# l[:] = [4, 5, 6]
# id(l)
# 139722190642240
