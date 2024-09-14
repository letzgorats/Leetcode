class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_num = max(nums)
        answer = 0
        length = 0
        for i in nums:
            if i == max_num:
                length += 1
            else:
                answer = max(answer, length)
                length = 0

        return answer
