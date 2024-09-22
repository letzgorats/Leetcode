# solution 1
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        cur = 1
        i = 1  # 지금까지 탐색한 숫자의 개수

        def count(cur):

            res = 0  # 현재까지 찾은 숫자의 개수
            nei = cur + 1  # cur 바로 다음의 사전식 숫자
            # (ex, cur == 1 이면 nei == 2)
            while cur <= n:
                res += min(nei, n + 1) - cur
                cur *= 10
                nei *= 10

            return res

        while i < k:
            steps = count(cur)
            if i + steps <= k:
                cur = cur + 1  # move right
                i += steps
            else:
                # move down
                cur *= 10
                i += 1

        return cur


# solution 2
class Solution:

    def findKthNumber(self, n: int, k: int) -> int:

        def count_steps(prefix, n):
            steps = 0
            curr = prefix
            next_prefix = prefix + 1
            while curr <= n:
                steps += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return steps

        current = 1
        k -= 1

        while k > 0:

            steps = count_steps(current, n)
            if steps <= k:
                k -= steps
                current += 1
            else:
                current *= 10
                k -= 1

        return current