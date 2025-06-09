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


# solution 3 - (trie, prefix tree) - (0ms) - (2025.06.09)
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        # cur 이라는 prefix 를 루트로 하는 서브트리 안에 숫자가 몇개 있는지 세기
        def count(cur):

            res = 0
            nei = cur + 1  # 다음 prefix 시작점
            while cur <= n:
                nei = min(nei, n + 1)  # n보다 넘지 않도록 조절하면서 범위 내 숫자 개수 누적
                res += nei - cur  # cur~nei-1 사이의 숫자수 = nei-cur
                cur *= 10  # 각 단계에서 cur*=10 로 한 자리씩 확장(ex. 1->10->100...) -> 자식으로 들어가는 것
                nei *= 10  # 그 자식들의 다음 형제를 추적하는 것 (ex. 2-> 20->200...)

            return res

        cur = 1  # 시작 숫자(사전 순에서 첫 번째)
        i = 1  # 현재 몇 번째 숫자인지 추적(1부터 시작)

        while i < k:
            steps = count(cur)  # count(cur) 로 prefix 아래 숫자 계산
            if i + steps <= k:  # 만약 k 를 넘지 않으면
                cur = cur + 1  # 다음 형제 prefix 로 이동 ( cur += 1)
                i += steps
            else:
                cur *= 10  # 넘는다면, 자식으로 들어감 (cur *= 10)
                i += 1

        return cur

'''
사전 순 트리(prefix Tree, Trie)
- 숫자를 접두사 기반으로 트리처럼 생각해보면,
1 -> 자식 : 10,11,12,...,19
2 -> 자식 : 20,21,22,...,29
...
즉, 숫자 curr 의 자식은 curr*10 ~ curr*10+9 까지이다.
우리는 이 트리를 사전 순으로 순회하면서 k번째 노드를 찾아가면 된다.

'''