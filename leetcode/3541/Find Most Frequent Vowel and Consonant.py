#solution 1 - (counting,sort) - (3ms) - (2025.09.13)
from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:

        cnts = Counter(s)
        cnts = sorted(cnts.items(), key=lambda x: -x[1])

        vowels = ['a', 'e', 'i', 'o', 'u']
        a, b = 0, 0
        for k, v in cnts:

            if k not in vowels:
                b = max(b, v)
            else:
                a = max(a, v)

        return a + b

