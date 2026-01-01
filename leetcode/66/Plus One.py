# Solution 1 - (array,math) - (0ms) - (2025.01.01)
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        tmp = ""
        for digit in digits:
            tmp += str(digit)

        tmp = int(tmp) + 1

        answer = []
        while tmp != 0:
            a = tmp % 10
            tmp = tmp // 10
            answer.append(a)

        return answer[::-1]