# solution 1 - (dfs,dynamic programming) - (6304ms) - (2025.05.18)
import heapq
from collections import defaultdict


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:

        mod = 10 ** 9 + 7

        def generate_cols(pattern, patterns):
            """
            가능한 모든 세로 색 조합을 만든다.
            """
            if len(pattern) == m:
                patterns.append(tuple(pattern))
                return
            for color in range(3):
                # 인접한 칸이 비어있거나 이전과 다른 색이라면, 해당 색 추가
                if not pattern or pattern[-1] != color:
                    generate_cols(pattern + [color], patterns)

        # 모든 가능한 색칠 조합 생성
        patterns = []
        generate_cols([], patterns)

        @cache
        def dfs(col, prev_pattern):
            """
            현재 열(col)에서 이전 패턴(prev_pattern) 기준으로 탐색
            """
            # 마지막 열까지 도달하면 1가지 방법을 찾은 것
            if col == n - 1:
                return 1

            total = 0
            # 가능한 다음 열의 패턴을 모두 탐색
            for next_pattern in patterns:
                if all(prev_pattern[i] != next_pattern[i] for i in range(m)):
                    total += dfs(col + 1, next_pattern)
                    total %= mod

            return total

        answer = 0
        for start_pattern in patterns:
            answer += dfs(0, start_pattern)
            answer %= mod

        return answer

'''
- generate_cols: 가능한 세로 조합을 미리 생성

- dfs:
    - 현재 열에서 다음 열로 넘어가며 색이 겹치지 않는 패턴 탐색
    - 마지막 열에 도달하면 경우의 수 1을 반환
    - 매번 DFS가 재귀 호출될 때, 새로운 열을 탐색하는 것이기 때문에 total = 0 의 위치는 dfs 내부가 적절한다.
    - 만약 초기화가 되지 않으면 이전 값이 누적되어, 결과가 잘못 계산된다.

- cache:
    - dfs가 재귀적으로 호출될 때, (col,prev_pattern)의 조합이 반복해서 탐색될 수 있다.
    - @cache는 이를 막고, 한 번 계산된 값은 그대로 반환한다. (ex. dfs(2, (0, 1)) 를 만나면 해당값을 바로 반환)
    - 중복 탐색을 줄여줘서 시간을 줄여준다.
    - 사용하면 좋은 경우    
        1) 중복된 하위 문제(Overlapping Subproblems)가 존재할 때 (ex.피보나치 수열) 혹은
        2) 경로 탐색에서 같은 상태가 반복될 때(ex.col,row 같은 값이 여러 번 같은 위치로 돌아올 때=DFS가 격자를 탐색할 때 같은 좌표와 같은 상태로 돌아올때)
    - 사용하면 좋지 않은 경우
        1) 탐색 경로가 유일한 경우(ex.dfs가 매번 다른 경로로 진행될 때)
        2) 전역 상태가 변경될 때(ex. 오히려 잘못된 값을 반환할 수 있다)
        3) 상태가 유일하지 않거나 동적으로 변할 때.(ex.randint)
    
- 모든 경우의 수를 누적하여 최종 결과를 반환
'''