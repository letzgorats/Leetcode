# solution 1 - (greedy,math,simulation) - (67ms) - (2025.11.13)
class Solution:
    def maxOperations(self, s: str) -> int:

        ones = 0
        res = 0
        for i, c in enumerate(s):
            # 1 이 발견된다면, ones 누적
            if c == '1':
                ones += 1
            # 빈공간이 처음 발견되는 순간
            elif i > 0 and s[i] == '0' and s[i - 1] == '1':
                res += ones

        return res

'''
(ex) [1,0,0,1,1,0,1]

1) To compute how many movement operations it will take for the car(s) to move the right:

 - We count the number cars as seen from the left of "zero"

 - No. of cars seen from the left: 1
 - No. of operations: 1

2) When we found another empty space, we add up the car count to the total operations.

 - No. of cars seen from the left: 3
 - No. of operations: 1+3=4
'''
