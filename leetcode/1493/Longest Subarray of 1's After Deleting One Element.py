# solution 1 - (two pointers, sliding window) - (56ms) - (2025.08.24)
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        zero = -1
        start = 0
        answer = 0
        for i in range(len(nums)):

            if nums[i] == 0:
                start = zero + 1
                zero = i

            answer = max(answer, i - start)

        return answer

'''
 0 1 2 3 4 5 6 7
[1,1,1,0,1,1,0,1]
       z
s

참고 
: https://www.youtube.com/watch?v=1uxfCY5ud6o
'''
