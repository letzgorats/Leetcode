import heapq
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # queue = []
        # print(queue)
        
        # answer = []
        # for n in nums:
        #     heapq.heappush(queue,n**2) 
        #     answer.append(heapq.heappop(queue))

        # return sorted(answer)
        return sorted(list(i**2 for i in nums))
