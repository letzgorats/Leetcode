class Solution:
    def makeFancyString(self, s: str) -> str:

        s = list(s)
        cnt = 0
        for i in range(1, len(s)):

            if s[i - 1] == s[i]:
                cnt += 1
                if cnt >= 2:
                    s[i - 1] = ''
            else:
                cnt = 0

        return ''.join(s)