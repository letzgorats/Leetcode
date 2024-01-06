class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        
        n = len(startTime)

        jobs = []

        for i in range(n):

            jobs.append([startTime[i],endTime[i],profit[i]])

        jobs = sorted(jobs,key=lambda x:x[0])
        # print(jobs)

        queue = []

        current, max_profit = 0,0

        for s,e,p in jobs:

            while queue and queue[0][0] <= s:
                et , temp = heapq.heappop(queue)
                current = max(current,temp)
            
            heapq.heappush(queue,(e,current+p))
            max_profit = max(max_profit,current+p)
            # print(queue, "max_profit =",max_profit)
        return max_profit
        
