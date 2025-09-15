# solution 1 - (set,greedy) - (6ms) - (2025.09.15)
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        txtlst = list(text.split())
        # print(txtlst)
        blst = set(map(str, brokenLetters))
        # print(blst)
        ans = 0
        for t in txtlst:
            if not (set(t) & blst):
                ans += 1

        return ans