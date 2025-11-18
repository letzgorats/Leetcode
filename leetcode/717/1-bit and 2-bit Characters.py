# solution 1 - (greedy,stack) - (3ms) - (2025.11.18)
from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        # 0, 10, 11

        stack = []

        for i in range(len(bits) - 1):

            if stack and stack[-1] == 1:
                stack.pop()
            else:
                stack.append(bits[i])

        # print(stack)
        # print(bits[-1])

        return True if sum(stack) == 0 and bits[-1] == 0 else False

# solution 2 - (greedy,index) - (0ms) - (2025.11.18)
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:

        i = 0
        while i < len(bits) - 1:

            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return True if i == len(bits) - 1 else False