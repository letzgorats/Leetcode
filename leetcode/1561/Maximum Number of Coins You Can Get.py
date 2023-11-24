class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """

        piles = sorted(piles)
        queue = deque(piles)
        answer = 0

        while queue:

            mini = queue.popleft()
            maxi = queue.pop()

            if queue[0] <= queue[-1]:
                answer += queue.pop()
            else:
                answer += queue.popleft()

        # print(queue)

        return answer
