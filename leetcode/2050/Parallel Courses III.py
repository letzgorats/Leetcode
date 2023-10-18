class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        :type n: int
        :type relations: List[List[int]]
        :type time: List[int]
        :rtype: int
        """

        indegree = [0] * (n+1)
        graph = [[] for i in range(n+1)]

        latest=[0]*(n+1)

        for r in relations:
            prev , after = r[0], r[1]

            graph[prev].append(after)
            indegree[after] += 1

        # print("graph",graph)
        # print("indgree",indegree)

        total_time = 0
        queue = deque([])

        for i in range(1,n+1):
            if indegree[i] == 0:
                latest[i]=time[i-1]
                queue.append(i)
        # print("queeu",queue)
        # print("latest",latest)
        # prev_takes = 0
        while queue:

            now = queue.pop()
            # print("now->",now)
            t0 = latest[now]
            # print("t0(latest[now])->",t0)

            for i in graph[now]:
                t=time[i-1]
                # print("t->",t)
                # print()
                # print("latest[i] :",latest[i])
                # print("t0+t :",t0+t)
                latest[i]=max(latest[i],t0+t)
   
                # print()
                # print("latest[i]->",latest[i])
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        # print(latest)
        return max(latest)
        
        
