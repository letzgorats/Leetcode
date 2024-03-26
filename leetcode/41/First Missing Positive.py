# We must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

# Set Algorithm 
# Time : O(n) / Space : O(n)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numSet = set(nums)

        for num in range(1,len(nums)+1):

            if num not in numSet:
                return num
        
        return len(nums) + 1


# Sort Algorithm 
# Time : O(nlogn) / Space : O(1)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 1

        for num in sorted(nums):
            if num == result :
                result += 1

        return result


# Optimization Algorithm -------------- We must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
# Time : O(n) / Space : O(1)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            
            while 1 <= nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:

                nums[nums[i]-i], nums[i] = nums[i], nums[nums[i]-i]

        
        for i in range(len(nums)):

            if nums[i] != i+1:
                    return i+1
        
        return len(nums) + 1



ref : (https://www.youtube.com/watch?v=orNygQroXL4)
