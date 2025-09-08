# solution 1 - (math,string) - (0ms) - (2025.09.08)
from typing import List
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        for i in range(n - 1, 0, -1):

            a = i
            b = n - i
            if ('0' in str(a)) or ('0' in str(b)):
                continue
            else:
                return [a, b]