# solution 1 - (counting) - (3ms) - (2025.06.10)
from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:

        counts = Counter(s)
        # print(counts)
        a1, a2 = 0, float('inf')
        for k, v in counts.items():

            if v % 2 == 1:  # odd
                a1 = max(a1, v)
            else:    # even
                a2 = min(a2, v)

        return a1 - a2