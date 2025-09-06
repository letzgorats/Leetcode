# solution 1 - (math) - (2121ms) - (2025.09.06)
from typing import List
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        # 4의 거듭제곱을 충분히 미리 준비(4^15 > 1e9)
        pow4 = [1]
        for _ in range(16):  # 길이를 17로 만들어 pow4[k+1] 접근 안전
            pow4.append(pow4[-1] * 4)

        def sum_floor_log4(n):
            if n <= 0:
                return 0

            res = 0
            k = 0
            while pow4[k] <= n:
                left = pow4[k]
                right = min(n, pow4[k + 1] - 1)
                cnt = right - left + 1
                res += k * cnt
                k += 1
            return res

        ans = 0
        for l, r in queries:
            total_steps = (r - l + 1) + (sum_floor_log4(r) - sum_floor_log4(l - 1))
            ans += (total_steps + 1) // 2  # =ceil(total_steps/2)

        return ans

'''
Dividing a number by 4 is equivalent to shifting it right by two bits in binary. 
For example, 11,(1011)2 divided by 4 becomes 2,(10)2
Let’s look at some examples to see how many operations are needed to reduce numbers to 0:
    - Numbers 1,2,3 require only 1 operation, and their binary lengths are 1 and 2.
    - Numbers 4,5,…,15 require 2 operations, and their binary lengths are 3 and 4.
    - Numbers 16,17,…,63 require 3 operations, and their binary lengths are 5 and 6.

From this pattern, we see that for a binary number of length x, we need only ⌈x/2] operations.
Using this, we can calculate the total number of operations for all numbers within a given range. 
'''

# solution 2 - (math) - (4406ms) - (2025.09.06)
class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:

        def get(num):
            i = 1
            base = 1
            cnt = 0
            while base <= num:
                cnt += ((i + 1) // 2) * (min(base * 2 - 1, num) - base + 1)
                i += 1
                base *= 2
            return cnt

        res = 0
        for q in queries:
            res += (get(q[1]) - get(q[0] - 1) + 1) // 2

        return res