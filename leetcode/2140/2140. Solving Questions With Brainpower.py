# solution 1 - bottom-up, iterative, dynamic programming- (74ms) - (2025.04.01)
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        '''
        Step 1 : 상태 정의
        - dp[i] = i 번째 문제부터 끝까지 봤을 때 얻을 수 있는 최대 점수
        '''
        state = [0] * (len(questions) + 1)

        '''
        Step 2 : 점화식
        - 선택(solve) : question[i][0] 점수를 얻고, i + question[i][1] + 1 번째로 이동
        - 스킵(skip) : 그냥 i+1 번째로 이동

        dp[i] = max(question[i][0] + dp[i+brainpower + 1], dp[i+1])
        '''
        '''
        Step 3 : 구현 방식
        - Top-down : 재귀 + 메모제이션(직관적)
        - Bottom-up : 반복문(메모리 효율이 더 좋을 수 있음)
        '''

        '''
        Step 4 : dp를 끝에서부터 채워나가는 방식이라면 : do[n] = 0(n은 문제 개수)
        '''

        for i in range(len(questions) - 1, -1, -1):
            point, brainpower = questions[i]
            next_idx = i + brainpower + 1
            # next_idx 가 범위를 넘을 수 있으니 조건 체크

            # solve
            solve = point + (state[next_idx] if next_idx < len(state) else 0)
            # skip
            skip = state[i + 1]

            state[i] = max(solve, skip)

        # print(state)
        return state[0]


# solution 2 - top down, recursive, memoization, dynamic programming- (192ms) - (2025.04.01)
from functools import lru_cache

'''
Q) @lru_cache(None) 가 하는 일(=메모이제이션 역할)?

A) @lru_cache(None) 를 함수 위에 붙이면,
    - lru는 least recently used 의 약자이고, cache 는 저장소를 의미한다.
    - 원래는 최근 사용하지 않은 것부터 제거하는 캐시인데, 
    - @lru_cache(None)으로 설정하면 무제한으로 저장한다는 뜻이다.

    - 이전에 계산한 결과를 자동으로 저장해두고, 같은 인풋이 들어오면 다시 계산하지 않고 바로 결과를 반환해준다.
    - 즉, dfs(5) 를 한 번 호출해서 계산했으면, 다음에 dfs(5)를 다시 호출할 땐, 저장된 값을 그대로 리턴한다.

Q) @lru_cache(maxsize=128) 와 같이 쓰는 경우는?

A) 이건 최대 128개의 결과만 캐시한다는 뜻이다.
    - 캐시가 가득차면 가장 오래전에 사용된 값부터 제거한다.
    - 파라미터 디폴트값은 "maxsize = 128" 이다.

   즉, @lru_cache(None) 은 무제한 캐시를 의미한다. None 을 넣으면 저장할 수 있는 함수 결과값의 개수제한이 없다.

Q) 딕셔너리를 직접 사용해서 캐시 관리를 하는 방법은?(해시타입만 lru_cache에 사용가능하므로, 딕셔너리 형태면 튜플로 바꾸거나 직접 메모이제이션 구현)

A) 
```
memo = {}

def dfs(i):
    if i in memo:
        return memo[i]

    # 계산 
    memo[i] = ....

    return memo[i]
```
이런식으로 하면 된다.
'''


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # Top-down
        @lru_cache(None)
        def dfs(i):
            # 종료조건 - 문제를 다 봤거나 범위를 넘었다면 점수는 0
            if i >= len(questions):
                return 0

            points, brainpower = questions[i]
            # 풀고 점수 받고, i+brainpower+1 번째로 넘어가기
            solve = points + dfs(i + brainpower + 1)

            # 풀지않고(스킵하고), 다음문제로 넘어가기
            skip = dfs(i + 1)

            return max(solve, skip)

        return dfs(0)