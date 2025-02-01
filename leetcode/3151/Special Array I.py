# solution 1
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        flag = nums[0]
        for i in range(1, len(nums)):
            if bin(flag ^ nums[i])[2:][-1] == '1':
                flag = nums[i]
            else:
                return False

        return True

# solution 2
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        for i in range(1,len(nums)):
            if (nums[i] % 2) == (nums[i-1] % 2):
                return False

        return True