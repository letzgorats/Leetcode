# solution 1
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # [[not lost],[lost only 1]]

        winner = set()
        havelost = defaultdict(int)
        havelostonly1 = set()

        for m in matches:
            winner.add(m[0])
            havelost[m[1]] += 1
            havelostonly1.add(m[1])
            if m[1] in winner:
                winner.remove(m[1])
            if m[0] in havelost:
                winner.remove(m[0])
            if havelost[m[1]] > 1:
                havelostonly1.remove(m[1])
            
        # print(havelostonly1)
        # print(winner)

        answer = [sorted(winner),sorted(havelostonly1)]

        return answer

# solution 2

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # [[not lost],[lost only 1]]

        lost = defaultdict(int)

        for m in matches:
            lost[m[0]] += 0
            lost[m[1]] += 1
        
        return [sorted(k for k,l in lost.items() if l == 0),sorted(k for k,l in lost.items() if l == 1)]
