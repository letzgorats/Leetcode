# solution 1 - (dp,matrix) - (711ms) - (2025.11.26)
from typing import List
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        MOD = 10 ** 9 + 7
        n = len(grid)
        m = len(grid[0])
        prev = [[0] * k for _ in range(m)]
        curr = [[0] * k for _ in range(m)]

        s = 0
        for j in range(m):
            s = (s + grid[0][j]) % k
            prev[j][s] = 1

        s = grid[0][0] % k

        for i in range(1, n):
            s = (s + grid[i][0]) % k
            curr[0] = [0] * k
            curr[0][s] = 1

            for j in range(1, m):
                curr[j] = [0] * k
                val = grid[i][j]
                for r in range(k):
                    nr = (r + val) % k
                    curr[j][nr] = (prev[j][r] + curr[j - 1][r]) % MOD

            prev, curr = curr, prev

        return prev[m - 1][0]


'''
DFS/백트래킹 느낌이 강해서 완전탐색으로 풀수 있을까 싶지만, 그렇게 하면 200x200 격자에서 
경로수가 2^400 수준이라 절대 불가능하다. 이 문제는 동적계획법+모듈러(sum%k 상태저장)이 핵심이다.

우리가 알고 싶은 것은 "전체 합 % k == 0" 인지 이므로, 합의 전체 값은 필요없고,
"k로 나눈 나머지 상태"만 중요하다.

dp[i][j][r] = (i,j)까지 이동했을 때, 합 % k == r 인 경로 "수"
(0<= r <= k-1) (총 k개)
각 칸마다 "나머지 상태"를 저장하는 DP 테이블을 둔다.

현재 셀 값 = grid[i][j]
현재 값을 더한 후의 나머지 = new_r = (old_r+grid[i][j]) % k
이동방향이 위에서 내려오고, 왼쪽에서 오므로, 
    - dp[i][j][new_r] += dp[i-1][j][old_r]
    - dp[i][j][new_r] += dp[i][j-1][old_r]

초기값 : dp[0][0][grid[0][0] % k] = 1
최종답 : dp[m-1][n-1][0]

'''
# solution 2 - (dp,matrix) - (1851ms) - (2025.11.26)
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        MOD = 10 ** 9 + 7
        n = len(grid)
        m = len(grid[0])

        dp = [[[0] * k for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(n):
            for j in range(m):
                for r in range(k):
                    modded_sum = (r + grid[i][j]) % k
                    if j > 0:
                        dp[i][j][modded_sum] += dp[i][j - 1][r]
                    if i > 0:
                        dp[i][j][modded_sum] += dp[i - 1][j][r]
                    dp[i][j][modded_sum] %= MOD

        return dp[n - 1][m - 1][0]
