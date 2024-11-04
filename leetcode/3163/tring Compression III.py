# solution 1
class Solution:
    def compressedString(self, word: str) -> str:

        comp = ""
        pre = word[0]
        cnt = 0
        while word:

            if pre != word[0]:
                comp += (str(cnt)+pre)
                cnt = 1
            elif pre == word[0] and cnt < 9:
                cnt += 1
            else:
                comp += (str(cnt) + pre)
                cnt = 1
            pre = word[0]
            word = word[1:]

        return comp + str(cnt) + pre

# solution 2
class Solution:
    def compressedString(self, word: str) -> str:

        res = []
        cnt = 1
        prev = word[0]
        for idx, ch in enumerate(word[1:]):
            if ch == prev and cnt < 9:
                cnt += 1
                continue
            res.append(f"{cnt}{prev}")
            cnt = 1
            prev = ch

        res.append(f"{cnt}{prev}")
        return ''.join(res)