# solution 1 - (array) - (0ms) - (2025.09.07)
from typing import List
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n):
            ans.append(i)

        return ans + [-sum(ans)]

# solution 2 - (array) - (0ms) - (2025.09.07)
class Solution:
    def sumZero(self, n: int) -> List[int]:

        ans = []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)

        if n % 2 == 1:
            ans.append(0)

        return ans
