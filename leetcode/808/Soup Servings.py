# solution 1 - (dp,math) - () - (2025.08.08)
class Solution:
    def soupServings(self, n: int) -> float:

        def dfs(a, b, dp):

            if a <= 0 and b > 0:
                return 1.0
            if a == 0 and b == 0:
                return 0.5
            if a > 0 and b <= 0:
                return 0.0
            if a <= 0 and b <= 0:
                return 0.5
            if dp[a][b] != -1:
                return dp[a][b]

            x = 0.25 * dfs(a - 100, b, dp)
            y = 0.25 * dfs(a - 75, b - 25, dp)
            z = 0.25 * dfs(a - 50, b - 50, dp)
            w = 0.25 * dfs(a - 25, b - 75, dp)

            dp[a][b] = x + y + z + w
            return dp[a][b]

        if n > 4800:
            return 1.0

        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        return dfs(n, n, dp)


# solution 2 - (dp,math) - (7ms) - (2025.08.08)
from functools import cache
class Solution:
    def soupServings(self, n: int) -> float:

        if n > 4800:
            return 1

        n = (n + 24) // 25

        @cache
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0

            return 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) + dp(a - 2, b - 2) + dp(a - 1, b - 3))

        return dp(n, n)

'''
1) 문제를 확률 함수로 정리하기
 우리가 구하는 값은
    - "A가 먼저 바닥나는 확률 + 동시에 바닥날 확률의 절반" 이다.
    - 이를 함수로 쓰면, f(a,b) = P(A먼저) + 0.5P(동시)
    - 여기서 a,b 는 각 수프의 남은 "단위 수" 이다.
    
 매 스텝에서 4가지 동작이 동일확률(0.25)로 일어나니까
 f(a,b) = 0.25 * [f(a-4,b)+f(a-3,b-1)+f(a-2,b-2)+f(a-1,b-3)]
 이게 핵심 점화식이다.

2) 왜 25ml 로 스케일링해도 되나?
 모든 서빙이 25의 배수이므로 n을 25로 나눈 단위로 생각해도 상태 전이가 동일하다.
  - n (ml) -> m = ceil(n/25) (단위 수로 변환)
  - 위 4가지 연산은 "(A,B에서 각각, (4,0, 3,1, 2,2, 1,3) 을 뺴는 것)"과 동일하다.
이렇게 바꾸면 상태공간이 엄청 줄어든채로 DP가 가능해진다.

3) base case 가 왜 저렇게 될까?
 "빈 순간"에 게임이 멈춘다고 정의했을 때,
    - a <= 0, b <= 0 : 바로 직전 한 번의 서빙으로 동시에 0 이하가 됐다는 뜻 -> 동시 종료 : 0.5    
    - a <= 0, b > 0 : A가 먼저 0 이 되었고, B는 아직 남음 -> 동시 종료 : 1.0    
    - a > 0, b <= 0 : B가 먼저 0 -> 우리가 원하는 사건이 아님 -> 0.0    

4) 왜 큰 n에서 답이 1에 가까워질까?(컷오프의 이유)
 매 스텝에서 기대 감소량을 보면,
    - E[deltaA] = (100+75+50+25)/4 = 62.5    
    - E[deltaB] = (0+25+50+75)/4 = 37.5
    
    즉, 평균적으로 A 가 빨리 준다. n이 커질수록, "A가 먼저 끝남"의 확률이 1에 수렴한다.
    즉, m 을 어느 정도 넘으면, (ex : n > 5000) 오차가 1e-5 미만이라고 보고 바로 1.0을 바환해도 정답 판정을 통과한다.   
    (커트라인은 약간씩 다르지만, 4800~5000 근처가 흔한 안전선)

5) 메모이제이션이 왜 필요한가?
 같은 (a,b) 상태는 여러 경로로 반복 방문된다. 이를 dp[a][b] 에 저장해두면, 각 상태를 한 번만 계산한다.
 -> O(m^2)로 줄어든다.

'''