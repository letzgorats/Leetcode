# solution 1 - (regular expression,vowel,search,ASCII) - (0ms) - (2025.07.15)
import re


class Solution:
    def isValid(self, word: str) -> bool:

        if len(word) < 3:
            return False

        # if not word.isalnum():  # alnum() 은 숫자 or 알파벳인 경우를 포함
        #     return False

        pattern = re.compile("[A-za-z0-9]+")  # pattern 정하기
        if not pattern.fullmatch(word):  # pattern 이랑 word fullmatch
            return False

        vowel = {'a', 'e', 'i', 'o', 'u'}

        if all(w.lower() not in vowel for w in word if w.isalpha()):
            return False

        if all(w.lower() in vowel for w in word if w.isalpha()):
            return False

        return True


'''
<함수>(<조건식> for <변수> in <시퀀스> if <조건>)
'''