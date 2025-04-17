# solution 1 - (array) - (23ms) - (2025.04.17)
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:

        answer = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        answer += 1

        return answer
