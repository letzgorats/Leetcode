# solution 1 - str, sum - (727ms) - (2025.04.11)
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        ans = 0
        for num in range(low, high + 1):

            s = str(num)
            if len(s) % 2 == 0:
                n = len(s) // 2
                pre = s[:n]
                suf = s[n:]
                if sum(list(map(int, pre))) == sum(list(map(int, suf))):
                    ans += 1

        return ans
