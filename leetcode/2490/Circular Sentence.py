class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        s = list(sentence.split(' '))
        if s[-1][-1] != s[0][0]:
            return False

        for i in range(1, len(s)):
            if s[i][0] != s[i - 1][-1]:
                return False

        return True