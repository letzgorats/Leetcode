# solution 1 - recursive, O(n) , O(n)
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

# solution 2 - iterative, math, O(n), O(n)
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


# solution 3 - O(nlogn), O(nlogn)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(i) for i in range(1, n + 1)]
        nums.sort()
        nums = list(map(int, nums))

        return nums

