import heapq
class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        
        n = len(profits)

        projects = []
        for s in zip(capital,profits):
            projects.append(s)

        projects = sorted(projects,key=lambda x : x[0])
        # print(projects)

        q = []

        i = 0
        for _ in range(k):

            while i < n and projects[i][0] <= w:
                heapq.heappush(q,-projects[i][1])
                i += 1
            
            if not q:
                break

            w += -heapq.heappop(q)

        return w
