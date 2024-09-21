# solution 1 - O(n) , O(n)
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


# solution 2 - O(nlogn), O(nlogn)
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [str(i) for i in range(1, n + 1)]
        nums.sort()
        nums = list(map(int, nums))

        return nums