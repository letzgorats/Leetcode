from collections import deque


class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        q = deque([i for i in range(1, n + 1)])

        while len(q) != 1:
            q.rotate(-(k - 1))
            q.popleft()

        return q.popleft()
