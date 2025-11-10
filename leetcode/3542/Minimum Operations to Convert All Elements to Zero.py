# solution 1 - (monotonic stack) - (208ms) - (2025.11.10)
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        stack = []
        res = 0
        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()
            if n == 0:
                continue
            if not stack or stack[-1] < n:
                res += 1
                stack.append(n)
            # print(stack)

        return res