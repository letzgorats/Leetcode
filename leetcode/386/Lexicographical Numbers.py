# solution 1 - recursive - O(n) - (2024.09.21)
from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        result = []

        def dfs(curr):
            if curr > n:
                return
            result.append(curr)
            for i in range(10):
                next_num = curr * 10 + i
                if next_num > n:
                    break
                dfs(next_num)

        for i in range(1, 10):
            dfs(i)

        return result

# solution 2 - iterative, math, O(n), O(n) - (2024.09.21)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        result = []
        cur = 1
        while len(result) < n:
            result.append(cur)

            if cur * 10 <= n:
                cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur = cur // 10

                cur += 1

        return result

# solution 3 - O(nlogn), O(nlogn) - (2024.09.21)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(i) for i in range(1, n + 1)]
        nums.sort()
        nums = list(map(int, nums))

        return nums

# solution 4 - (dfs,recursive) - (48ms) - (2025.06.08)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        ans = []

        def recurse(current):

            if current > n:
                return

            ans.append(current)
            for i in range(0, 10):
                if current * 10 + i <= n:
                    recurse(current * 10 + i)

        for i in range(1, 10):
            if i <= n:
                recurse(i)

        return ans

# solution 5 - heapq, O(n logn) - (2025.06.08)
import heapq
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        q = []
        for i in range(1, n + 1):
            heapq.heappush(q, str(i))
        # print(q)
        ans = []
        while q:
            ans.append(int(heapq.heappop(q)))

        return ans