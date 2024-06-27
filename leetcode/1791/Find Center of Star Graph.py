class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """

        indegree = [0] * (len(edges) + 1)
        # print(indegree)

        for a, b in edges:
            indegree[a - 1] += 1
            if indegree[a - 1] != 1:
                return a
            indegree[b - 1] += 1
            if indegree[b - 1] != 1:
                return b

        return -1
