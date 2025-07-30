# solution 1 - (bitwise,and) - (677ms) - (2024.09.14)
from typing import List
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

# solution 2 - (bitwise,and) - (27ms) - (2025.07.30)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_val = max(nums)

        ans, cur = 0, 0
        for i in range(len(nums)):
            if nums[i] >= max_val:
                cur += 1
            else:
                ans = max(ans, cur)
                cur = 0

        return max(ans, cur)

'''
and 연산이 작은 값으로 수렴하는 성질이 있으므로 최대 and 값은 nums의 최댓값이다.
'''