# solution 1 - (math,array) - (3ms) - (2025.05.27)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        num1, num2 = 0, 0
        for i in range(1, n + 1):
            if i % m != 0:
                num1 += i
            else:
                num2 += i

        return num1 - num2
