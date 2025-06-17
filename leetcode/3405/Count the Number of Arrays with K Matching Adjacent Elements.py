# TLE - (2025.06.17)
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        mod = 10 ** 9 + 7
        candi = []

        def backtracking(idx, cur, cnt):

            if cnt > k:
                return

            if idx == n:
                if cnt == k:
                    candi.append(cur)
                return

            for i in range(1, m + 1):
                if cnt <= k:
                    if cur and cur[-1] == i:
                        backtracking(idx + 1, cur + [i], cnt + 1)
                    else:
                        backtracking(idx + 1, cur + [i], cnt)
                else:
                    if cur[-1] != i:
                        backtracking(idx + 1, cur + [i], cnt)

        backtracking(0, [], 0)
        # print(candi)

        return len(candi) % mod

'''
일일이 조합을 다 구해버리려고 하니까 TLE 가 나는 듯함. 조합은 제대로 구했음.
다만, 문제에서는 단순히 개수를 구하는 것이니까, cur[-1] 을 비교하지 않고 그냥 prev 를 파라미터로 넘겨주면서
이전 요소와 현재 바라보는 요소를 비교하도록 함으로써 개수를 카운팅하는 방법으로 하면 됨. 
'''

# TLE 2 - (backtracking,combinations,count) - (2025.06.17)
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        mod = 10 ** 9 + 7
        answer = 0

        def backtracking(idx, prev, cur, cnt):
            nonlocal answer
            if cnt > k:
                return

            if idx == n:
                if cnt == k:
                    answer += 1
                    # 조합을 확인해보려면 여기서 print만 잠깐 하면 됨!
                    # print(cur)
                return

            for i in range(1, m + 1):

                if i == prev:
                    backtracking(idx + 1, i, cur + [i], cnt + 1)
                else:
                    backtracking(idx + 1, i, cur + [i], cnt)

        backtracking(0, 0, [], 0)

        return answer % mod


# dp 로 바꿔보자.
# TLE 3 - (dp-top_down) - (TLE) - (2025.06.17)
from functools import lru_cache
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        mod = 10 ** 9 + 7
        answer = 0

        @lru_cache(None)
        def dp(idx, prev, cnt):
            if cnt > k:
                return 0
            if idx == n:
                return 1 if cnt == k else 0

            res = 0
            for i in range(1, m + 1):
                if i == prev:
                    res += dp(idx + 1, i, cnt + 1)
                else:
                    res += dp(idx + 1, i, cnt)

            return res % mod

        return dp(0, 0, 0)

'''
top-down(재귀 + @lru_cache) 은 재귀 깊이 및 call overhead 때문에 느리다.
'''

# bottom-up DP 방식으로 바꾸고, O(n*k) 방식으로 압축하면 통과할 수 있다.
# MLE - (dp,bottom up) - (Memory Exceeded) - (2025.06.17)
'''
dp[i][j] = 길이 i, 인접한 같은 숫자가 j번 등장하는 배열의 수

새로 추가한 수가 이전 수와 다르면 
dp[i][j] += dp[i-1][j] * (m-1)
dp[i][j] += dp[i-1][j-1]

'''
from functools import lru_cache
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        mod = 10 ** 9 + 7

        # dp[i][j] : 길이 i 인 배열 중 인접한 동일 수가 j 번인 개수
        dp = [[0] * (k + 2) for _ in range(n + 1)]
        dp[1][0] = m  # 첫 번째 수는 무조건 k=0

        for i in range(2, n + 1):
            for j in range(0, min(i, k + 1)):
                # 1. 마지막 수가 이전 수와 다를 때
                # : 이전 dp[i-1][j] * (m-1)
                dp[i][j] = (dp[i - 1][j] * (m - 1)) % mod

                # 2. 마지막 수가 이전 수와 같을 때
                # : 이전 dp[i-1][j-1] * 1
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod

        return dp[n][k]

from math import comb
# solution 1 - (math,combination) - (1851ms) - (2025.06.17)
'''
조합 공식 사용
-> 정답 : m x C(n-1,k) X (m-1)^(n-1-k)

-> why?
- m : 처음 시작하는 숫자 선택(1~m 중)
- C(n-1,k) : 총 n-1 개의 인접 자리 중, k개를 "같은 숫자"로 만들 위치 선택
- (m-1)^(n-1-k) : 나머지 자리에 다른 숫자(m-1 종류) 중 하나를 선택해서 배치

이 문제는 사실상 "길이 n의 배열에 인접한 중복이 k 개 생기도록 배치하는 경우의 수"이기 때문에, 수학적으로 
푸는게 유일하게 시간초과/메모리초과를 방지할 수 있는 방법이다.
'''
class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        MOD = 10 ** 9 + 7

        if k > n - 1:
            return 0

        # 빠르게 팩토리얼, 역팩토리얼 계산
        fac = [1] * (n)
        for i in range(1, n):
            fac[i] = fac[i - 1] * i % MOD

        inv = [1] * (n)
        inv[n - 1] = pow(fac[n - 1], MOD - 2, MOD)  # 페르마 소정리
        for i in range(n - 1, 0, -1):
            inv[i - 1] = inv[i] * i % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return fac[a] * inv[b] % MOD * inv[a - b] % MOD

        return m * comb(n - 1, k) % MOD * pow(m - 1, n - 1 - k, MOD) % MOD