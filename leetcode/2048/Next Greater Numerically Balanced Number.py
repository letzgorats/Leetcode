# solution 1 - (greedy) - (4184ms) - (2025.10.24)
from collections import Counter
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        cnt = Counter(str(n))
        # print(cnt)
        for i in range(n + 1, 10 ** 9):

            cnt = Counter(str(i))
            balanced = True
            # print(cnt)
            for k, v in cnt.items():

                if int(k) != v:
                    balanced = False
                    break

            if balanced:
                return i

        return -1

# solution 2 - (ord) - (1860ms) - (2025.10.24)
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:

        def solve(x):
            s = str(x)
            vec = [0] * 10
            for ch in s:
                vec[ord(ch) - 48] += 1

            for ch in s:
                c = ord(ch) - 48
                if c == 0 or vec[c] != c:
                    return False
            return True

        i = n + 1
        while True:
            if solve(i):
                return i
            i += 1

