class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        hash = {}
        for i in range(len(graph)):
            hash[i] = graph[i]
        hash = sorted(hash.items(), key=lambda x: -len(x[1]))

        values = [0] * n
        value = n
        for node, v in hash:
            values[node] = value
            value -= 1

        answer = 0
        for a, b in roads:
            answer += (values[a] + values[b])

        return answer
