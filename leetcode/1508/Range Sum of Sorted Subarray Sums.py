# solution 1 - O(n^2) , space - O(n^2)
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        mod = 10 ** 9 + 7
        subArray = []

        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum = (cur_sum + nums[j]) % mod
                subArray.append(cur_sum)

        subArray.sort()
        res = 0
        for i in range(left - 1, right):
            res = (res + subArray[i]) % mod
        return res

# solution 2 - O(n^3)
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        mod = 10 ** 9 + 7
        subArray = []
        i, j = 0, 1
        while i < n:

            j = i + 1
            while j <= n:
                subArray.append(sum(nums[i:j]))
                j += 1

            i += 1

        subArray.sort()
        return sum(subArray[left - 1:right]) % mod

# solutino 3 - minHeap solution - (tricky method) - O(n^2) , space - O(n)
import heapq


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:

        mod = 10 ** 9 + 7
        minHeap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(minHeap)

        res = 0
        for i in range(right):
            num, index = heapq.heappop(minHeap)
            if i >= left - 1:
                res = (res + num) % mod

            if index + 1 < n:
                next_pair = (num + nums[index + 1], index + 1)
                heapq.heappush(minHeap, next_pair)

        return res