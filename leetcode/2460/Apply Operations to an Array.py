# solution 1 - two pointers, greedy - (3ms) - (2025.03.01)
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        answer = []
        for j in nums:
            if j != 0:
                answer.append(j)

        zero_cnt = len(nums) - len(answer)
        answer += [0] * zero_cnt
        return answer
