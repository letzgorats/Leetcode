import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.q = nums
        heapq.heapify(self.q)

        while len(self.q) > k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:

        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        # print(kth_largest)
        return self.q[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)