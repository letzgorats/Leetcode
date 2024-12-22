# solution 1 TLE - greedy, brtue force
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        # left to right,up
        # doesn't have to be contiguous
        # for [2,4], 4 would be theoretical left most

        # O(n) for each query -> greedy
        res = [-1] * len(queries)

        for i, query in enumerate(queries):

            l, r = sorted(query)
            if l == r or (heights[r] > heights[l]):
                res[i] = r
                continue

            for j in range(r + 1, len(heights)):
                if heights[j] > max(heights[l], heights[r]):
                    res[i] = j
                    break

        return res


# solution 2 = heapq, monotonic stack
import heapq
from collections import defaultdict
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        res = [-1] * len(queries)
        groups = defaultdict(list)  # r => [(required_height, query_index)]

        for i, q in enumerate(queries):

            l, r = sorted(q)
            if l == r or heights[r] > heights[l]:
                res[i] = r
            else:
                h = max(heights[l], heights[r])
                groups[r].append((h, i))

        min_heap = []
        for i, h in enumerate(heights):

            for q_h, q_i in groups[i]:
                heapq.heappush(min_heap, (q_h, q_i))

            while min_heap and h > min_heap[0][0]:
                q_h, q_i = heapq.heappop(min_heap)
                res[q_i] = i

        return res