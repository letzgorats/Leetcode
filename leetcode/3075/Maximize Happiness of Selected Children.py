# 666/674 TLE - heapq solution
import heapq
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        queue = []
        for h in happiness:
            heapq.heappush(queue,(-h))
        
        answer = 0

        while k :
            
            x = heapq.heappop(queue)
            answer -= x
            
            queue = list(queue)
            for i in range(len(queue)):
                if queue[i] != 0:
                    queue[i] += 1

            heapq.heapify(queue)

            k -= 1
        
        return answer

# 667/674 TLE - sort solution
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
       
        answer = 0
        
        while k :
            happiness = sorted(happiness,reverse=True)
            answer += happiness.pop(0)

            for i in range(len(happiness)):
                if happiness[i] != 0:
                    happiness[i] -= 1

            k -= 1
        
        return answer


# solution - index!
class Solution(object):
    def maximumHappinessSum(self, happiness, k):
        """
        :type happiness: List[int]
        :type k: int
        :rtype: int
        """
        happiness.sort(reverse=True)
        answer = 0
        for i in range(min(len(happiness),k)):
            if happiness[i] <= i:
                break
            answer += happiness[i] - i
        
        return answer
