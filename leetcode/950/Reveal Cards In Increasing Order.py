from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        
        deck = sorted(deck)
        answer = deque([])
    
        for x in deck[::-1]:
            answer.rotate()
            answer.appendleft(x)

        return list(answer)
