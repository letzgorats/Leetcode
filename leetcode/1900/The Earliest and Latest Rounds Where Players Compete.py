# solution 1 - (memoization,dp) - (3ms) - (2025.07.12)
from functools import lru_cache
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:

        @lru_cache(None)
        def dfs(n, first, second):
            left, right = min(first, second), max(first, second)

            # 두 사람이 지금 바로 만나면 끝!
            if left + right == n + 1:
                return [1, 1]

            # 빠르게 끝나는 케이스(인원수가 적어서 무조건 다음 라운드에서 만날 수 밖에 없는 경우는 미리 처리)
            if n == 3 or n == 4:
                return [2, 2]

            # 대칭되면, 뒤집어서 동일한 문제로 처리 (대칭 최소화)
            # (ex) (7,2) 도 (2,7) 과 똑같은 상황이니까 항상 왼쪽이 작게 고정해주는 것
            if left - 1 > n - right:
                left = n + 1 - right
                right = n + 1 - min(first, second)

            next_n = (n + 1) // 2
            min_round = n
            max_round = 1

            results = []

            if right * 2 <= n + 1:
                # 두 플레이어가 "앞쪽 절반"에서 등장하는 경우 (ex, first = 2, second = 4, n= 8)
                preLeft = left - 1  # left 앞에 있는 사람 수
                midGap = right - left - 1   # 둘 사이에 있는 사람 수

                for i in range(preLeft + 1):  # i: # left 앞에서 몇 명 살아남을지
                    for j in range(midGap + 1):  # j : 둘 사이에서 몇 명 살아남을지
                        # i명이 이기고, j명이 이기고, 우리가 i+1번째와 i+j+2번째 위치에서 만나게 된다는 가정.
                        new_left = i + 1
                        new_right = i + j + 2
                        r1, r2 = dfs(next_n, new_left, new_right)
                        min_round = min(min_round, 1 + r1)
                        max_round = max(max_round, 1 + r2)
            else:
                # 두 사람이 떨어져 있고, 서로 다른 절반에 있는 경우
                mirrored = n + 1 - right
                preLeft = left - 1
                midGap = mirrored - left - 1
                innerGap = right - mirrored - 1

                for i in range(preLeft + 1):
                    for j in range(midGap + 1):
                        # j명 사이에서 살아남고, 오른쪽에서 innerGap 중 절반이 살아남으면
                        # 그걸 고려한 다음 라운드의 second 위치를 계산
                        new_left = i + 1
                        new_right = i + j + 1 + ((innerGap + 1) // 2) + 1
                        r1, r2 = dfs(next_n, new_left, new_right)
                        min_round = min(min_round, 1 + r1)
                        max_round = max(max_round, 1 + r2)

            return [min_round, max_round]

        return dfs(n, firstPlayer, secondPlayer)