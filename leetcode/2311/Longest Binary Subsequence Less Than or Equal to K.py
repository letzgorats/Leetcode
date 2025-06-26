# solution 1 - (math,greedy,string,memoization) - (3ms) - (2025.06.26)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        n = len(s)
        zeros = s.count('0')    # zero는 최대한 다 포함해야 가장 긴 길이의 substring이 된다.
        ones = 0    # 1의 개수
        value = 0   # 실제 값
        power = 1   # 이진수에서의 멱(거듭제곱)

        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                if value + power > k:
                    continue
                value += power
                ones += 1
            power <<= 1
            if power > k:
                break

        return zeros + ones

# TLE
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:

        def check_number(ss):
            b = 0
            number = 0
            for i in range(len(ss) - 1, -1, -1):
                number += int(ss[i]) * pow(2, b)
                b += 1
            return number

        # candi = set()
        ans = 0
        def backtracking(idx, cur):
            nonlocal ans
            if cur and check_number(cur) > k:
                return
            if cur and check_number(cur) <= k:
                ans = max(ans, len(cur))
                # candi.add(cur)
            for i in range(idx, len(s)):
                backtracking(i + 1, cur + s[i])  # include
                backtracking(i + 1, cur)  # skip

        backtracking(0, '')
        # print(candi)
        return ans
