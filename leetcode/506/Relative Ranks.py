# sorting, hash solution - 81.94%
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        rank = dict()

        rank_score = sorted(score,reverse=True)
        for idx,s in enumerate(rank_score):
            rank[s] = (idx+1)
        
        # print(rank)
        answer = []
        for s in score:
            if rank[s] == 1:
                answer.append("Gold Medal")
            elif rank[s] == 2:
                answer.append("Silver Medal")
            elif rank[s] == 3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(rank[s]))

        return answer

      
# heap solution - 51.74 %
import heapq
class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        
        maxHeap = []
        for i,s in enumerate(score):
            heapq.heappush(maxHeap,(-s,i))

        place = 1
        answer = [0] * len(score)

        while maxHeap:
            x = heapq.heappop(maxHeap)[1]
            if place > 3 :
                rank = str(place)
            elif place == 1:
                rank = "Gold Medal"
            elif place == 2:
                rank = "Silver Medal"
            elif place == 3:
                rank = "Bronze Medal"

            answer[x] = rank
            place += 1

        return answer 
