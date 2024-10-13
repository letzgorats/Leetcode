import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:

        k = len(nums)
        left = right = nums[0][0]
        min_heap = []
        for i in range(k):
            lst = nums[i]

            left = min(left, lst[0])
            right = max(right, lst[0])
            # min_val, idx_of_list, idx_of_n
            heapq.heappush(min_heap, (lst[0], i, 0))

        res = [left, right]

        while True:
            n, i, idx = heapq.heappop(min_heap)
            idx += 1

            if idx == len(nums[i]):
                return res

            next_val = nums[i][idx]
            heapq.heappush(
                min_heap, (next_val, i, idx)
            )

            right = max(right, nums[i][idx])
            left = min_heap[0][0]

            if right - left < res[1] - res[0]:
                res = [left, right]
