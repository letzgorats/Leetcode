# TLE - (heapq) - (TLE) - (2025.06.28)
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        max_val = float('-inf')
        q = []

        def backtracking(idx, cur):
            nonlocal max_val

            if len(cur) > k:
                return

            if len(cur) == k and max_val < sum(cur):
                max_val = sum(cur)
                heapq.heappush(q, (-max_val, cur))
                return

            for i in range(idx, len(nums)):
                backtracking(i + 1, cur + [nums[i]])
                backtracking(i + 1, cur)

        backtracking(0, [])
        # print(q)
        _, b = heapq.heappop(q)

        return b

# solution 1 - (heapq) - (7ms) - (2025.06.28)
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        q = []
        for i, num in enumerate(nums):
            heapq.heappush(q, (-num, i))

        top_k = []
        while k:
            x, idx = heapq.heappop(q)
            heapq.heappush(top_k, (idx, -x))
            k -= 1

        ans = []
        while top_k:
            i, x = heapq.heappop(top_k)
            ans.append(x)
        return ans