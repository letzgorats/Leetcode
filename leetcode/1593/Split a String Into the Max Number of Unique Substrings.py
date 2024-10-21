class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def backtracking(idx, cur):
            nonlocal res, max_len

            if idx == len(s):
                max_len = max(len(res), max_len)
                return res

            for i in range(idx, len(s)):
                cur = s[idx:i + 1]
                if cur not in res:
                    res.add(cur)
                    backtracking(i + 1, cur)
                    res.remove(cur)
                else:
                    continue

        max_len = 0
        res = set()
        backtracking(0, "")

        return max_len