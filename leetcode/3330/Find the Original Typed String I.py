# solution 1 - (string,count) - (24ms) - (2025.07.01)
class Solution:
    def possibleStringCount(self, word: str) -> int:

        pre = ''
        cnt = 1
        for w in word:
            if w == pre:
                cnt += 1

            pre = w

        return cnt