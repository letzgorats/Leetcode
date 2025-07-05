from collections import Counter
from typing import List
# solution 1 - (counter,sort) - (0ms) - (2025.07.05)
class Solution:
    def findLucky(self, arr: List[int]) -> int:

        cnt = sorted(Counter(arr).items(), reverse=True)
        print(cnt)
        for k, v in cnt:
            if k == v:
                return k

        return -1
