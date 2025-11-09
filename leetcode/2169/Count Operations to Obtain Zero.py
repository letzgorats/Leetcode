# solution 1 - (greedy) - (37ms) - (2025.11.09)
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        cnt = 0
        while num1 and num2:

            if num2 >= num1:
                num2 -= num1
            else:
                num1 -= num2

            cnt += 1

        return cnt