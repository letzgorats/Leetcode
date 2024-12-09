from _bisect import bisect_right
from _bisect import bisect_left
# solution 1 - binary search
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        n = len(nums)
        store, answer = [], []

        for i in range(1, n):
            if (nums[i] % 2) == (nums[i - 1] % 2):
                store.append(i)

        print(store)

        for l, r in queries:
            idx = bisect_right(store, l)

            if idx < len(store) and store[idx] <= r:
                answer.append(False)
            else:
                answer.append(True)

        return answer

# solution 2 - prefix
from itertools import pairwise
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:

        prefix, cnt = [0], 0
        for a, b in pairwise(nums):

            if (a + b) % 2 == 1:
                cnt += 1
            prefix.append(cnt)
        # print(prefix)

        answer = []
        for a, b in queries:
            answer.append(prefix[b] - prefix[a] == b - a)

        return answer