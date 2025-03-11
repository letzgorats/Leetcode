# solution 1 - sliding window, substrings length - (115ms) - (2025.03.11)
from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        abc = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(s)):

            abc[s[r]] += 1

            while len(abc) == 3:
                # 현재 right 에서 가능한 모든 서브스트링을 세는 것
                # 현재까지 포함, 뒷 +문자열도 다 가능한 서브스트링이므로
                # len(s) - r 을 더해주고, l 을 증가시켜본다.
                res += len(s) - r
                abc[s[l]] -= 1
                if abc[s[l]] == 0:
                    abc.pop(s[l])
                l += 1

        return res
