import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        q = []
        for i in nums:
            heapq.heappush(q, -i)

        score = 0
        while k != 0:
            x = heapq.heappop(q)
            score += (-x)
            y = math.ceil((-x) / 3)
            heapq.heappush(q, -y)
            k -= 1

        return score