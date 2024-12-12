import heapq, math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        q = []
        for g in gifts:
            heapq.heappush(q, -g)

        for _ in range(k):
            x = -(heapq.heappop(q))
            left = int(math.sqrt(x))
            heapq.heappush(q, -left)

        # print(q)

        return -sum(list(q))