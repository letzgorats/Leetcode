# solution 1 - deque
from collections import deque


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        deque1 = list(sentence1.split())
        deque2 = list(sentence2.split())

        # 처음 -> 끝 비교
        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.pop(0)
            deque2.pop(0)

        # 끝 -> 처음 비교
        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop(-1)
            deque2.pop(-1)

        return not deque1 or not deque2

# solution 2 - two pointers
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        a, b = "", ""

        if sentence1 == sentence2:
            return True

        if len(sentence1) >= len(sentence2):
            a = sentence1
            b = sentence2
        else:
            a = sentence2
            b = sentence1

        a = list(a.split(' '))
        b = list(b.split(' '))

        left, right = 0, len(b) - 1

        while left < len(b) and a[left] == b[left]:
            left += 1

        while right >= 0 and a[len(a) - len(b) + right] == b[right]:
            right -= 1

        if left > right:
            return True
        else:
            return False

