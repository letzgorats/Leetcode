# solution 1 - (stack, lexicographically, suffix) - (434ms) - (2025.06.06)
from collections import deque
class Solution:
    def robotWithString(self, s: str) -> str:

        s_list = list(s)
        n = len(s_list)
        suffix_min = [''] * n
        suffix_min[-1] = s_list[-1]
        for i in range(len(s_list) - 2, -1, -1):
            suffix_min[i] = min(s_list[i], suffix_min[i + 1])

        # print(suffix_min)

        s = deque(list(s))
        p = []
        t = []

        i = 0
        while s or t:
            while t and (i == n or t[-1] <= suffix_min[i]):
                p.append(t.pop())

            if s:
                t.append(s.popleft())
                i += 1

            # print(p)
            # print(t)

        return ''.join(p)

# solution 2 - same logic
class Solution:
    def robotWithString(self, s: str) -> str:

        n = len(s)
        min_suffix = list(s)

        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(min_suffix[i + 1], min_suffix[i])

        # print(min_suffix)

        t = []
        paper = []

        for i, ch in enumerate(s):
            t.append(ch)
            while t and (i + 1 == n or t[-1] <= min_suffix[i + 1]):
                paper.append(t.pop())

        # print(paper)

        while t:
            paper.append(t.pop())

        return ''.join(paper)
