# solution 1 - (string, count) - (279ms) - (2024.11.01)
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

# solution 2 - (string, dict) - (541ms) - (2025.07.21)
from collections import defaultdict
class Solution:
    def makeFancyString(self, s: str) -> str:

        cons_freq = defaultdict(int)
        prev, answer = "", ""
        for char in s:
            if prev == char:
                cons_freq[char] += 1
                if cons_freq[char] >= 3:
                    continue
            else:
                if cons_freq[prev]:
                    del cons_freq[prev]
                prev = char
                cons_freq[char] += 1
            answer += char

        return answer

# solution 3 - (count,string) - (191ms) - (2025.07.21)
class Solution:
    def makeFancyString(self, s: str) -> str:

        cnt = 0
        prev, answer = "", ""
        for char in s:
            if prev == char:
                cnt += 1
                if cnt >= 2:
                    continue
            else:
                cnt = 0
                prev = char
            answer += char

        return answer



