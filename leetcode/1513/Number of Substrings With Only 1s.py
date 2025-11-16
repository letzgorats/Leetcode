# solution 1 - (math,greedy,count) - (27ms) - (2025.11.16)
class Solution:
    def numSub(self, s: str) -> int:

        ans = 0
        modulo = 10 ** 9 + 7
        s = list(s)
        pre = 0

        for i in range(len(s) - 1):

            if s[i] == '1' and s[i + 1] == '1':
                continue
            elif s[i] == '0':
                pre = i + 1
            elif s[i] == '1' and s[i + 1] == '0':
                ans += (((i - pre + 1) * (1 + i - pre + 1) // 2) % modulo)

        if s[i + 1] == '1':
            ans += (((i + 1 - pre + 1) * (1 + i + 1 - pre + 1) // 2) % modulo)

        return ans


# solution 2 - (greedy,math) - (3ms) - (2025.11.16)
class Solution:
    def numSub(self, s: str) -> int:
        s = s.split('0')
        modulo = 10 ** 9 + 7
        cnt = 0
        for num in s:
            cnt += len(num) * (len(num) + 1) // 2

        cnt %= modulo

        return cnt