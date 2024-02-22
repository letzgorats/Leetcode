class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        people = [0] * n
        believe = [[] for _ in range(n)]

        for a,b in trust:
            
            believe[a-1].append(b-1)
            people[b-1] += 1
        
        for idx,p in enumerate(people):

            if p == n-1:
                if len(believe[idx]) == 0:
                    return idx+1
        
        return -1


        
