# solution 1 - (math,greedy,count) - (38ms) - (2025.08.19)
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        cnt = 0
        answer = 0
        for i in range(len(nums)):

            if nums[i] == 0:
                cnt += 1
            else:
                answer += ((cnt + 1) * cnt // 2)
                cnt = 0

        if cnt != 0:
            answer += ((cnt + 1) * cnt // 2)

        return answer

