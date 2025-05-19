# solution 1 - (array,math,sorting) - (1ms) - (2025.05.19)
class Solution:
    def triangleType(self, nums: List[int]) -> str:

        if (nums[0] + nums[1] > nums[2] and
                nums[1] + nums[2] > nums[0] and
                nums[0] + nums[2] > nums[1]):
            if len(set(nums)) == 1:
                return "equilateral"
            elif len(set(nums)) == 3:
                return "scalene"
            else:
                return "isosceles"

        return "none"
