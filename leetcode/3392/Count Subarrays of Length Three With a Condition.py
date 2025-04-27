# solution 1 - (math,array) - (3ms)- (2025.04.27)
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        answer = 0
        for i in range(0, len(nums) - 2):
            if (nums[i + 1] / 2.0) == nums[i] + nums[i + 2]:
                answer += 1

        return answer