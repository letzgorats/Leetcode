class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        return word[:word.index(ch)+1][::-1] + word[word.index(ch)+1:]
