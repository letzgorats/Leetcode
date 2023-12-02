# sol 1)
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        answer = 0
        for w in words:
            for c in w:
                if w.count(c) > chars.count(c):
                    break
            else: answer += len(w)

        return answer


# sol 2)

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """

        answer = 0
        for w in words:
            for c in w:
                if w.count(c) > chars.count(c):
                    break
            else: answer += len(w)

        return answer
