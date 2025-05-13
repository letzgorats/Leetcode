# solution 1 - (counting sort) - (2176ms) - (2025.05.12)
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        mod = 10 ** 9 + 7

        for _ in range(t):
            nxt = [0] * 26
            # derived from 'z'
            nxt[0] = cnt[25]
            # derived from 'z' and 'a'
            nxt[1] = (cnt[25] + cnt[0]) % mod
            # derived from previos alphabet
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt

        answer = sum(cnt) % mod
        return answer


# TLE
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:

        mod = 10 ** 9 + 7
        for _ in range(t):
            new_str = []
            for idx, alpha in enumerate(s):
                if alpha == 'z':
                    new_str.append('ab')
                else:
                    new_str.append(chr(ord(s[idx]) + 1))

            # print(new_str)
            s = "".join(new_str)

        return len(s) % mod