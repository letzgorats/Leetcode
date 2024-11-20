# solutino 1 - sliding window(119ms)
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        freqs = [0] * 3
        n = len(s)

        for c in s:
            freqs[ord(c) - ord('a')] += 1

        i = 0
        j = 0
        if freqs[0] < k or freqs[1] < k or freqs[2] < k:
            return -1

        for j in range(n):
            freqs[ord(s[j]) - ord('a')] -= 1

            if freqs[0] < k or freqs[1] < k or freqs[2] < k:
                freqs[ord(s[i]) - ord('a')] += 1
                i += 1

        return n - (j - i + 1)


# solution 2 - sliding window(245ms)
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        # total counts
        count = [0, 0, 0]  # [a,b,c]
        for c in s:
            count[ord(c) - ord('a')] += 1

        if min(count) < k:
            return -1

        # sliding window
        res = float('inf')
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1

            res = min(res, len(s) - (r - l + 1))

        return res
