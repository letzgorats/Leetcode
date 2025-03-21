# solution 1 - dp, LCS based - (475ms) - (2025.03.22)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        # 역추적 검증 함수(문제의 직접적인 솔루션과는 무관)
        # def trace(s, t, i, j, path, results, dp):
        #     if j == 0:
        #         results.append("".join(reversed(path)))
        #         return
        #     if i == 0:
        #         return

        #     if s[i - 1] == t[j - 1]:
        #         if dp[i - 1][j - 1] > 0:
        #             # 선택한 경우
        #             trace(s, t, i - 1, j - 1, path + [s[i - 1]], results, dp)
        #         if dp[i - 1][j] > 0:
        #             # 건너뛴 경우
        #             trace(s, t, i - 1, j, path, results, dp)
        #     else:
        #         if dp[i - 1][j] > 0:
        #             # 문자가 다르니까 무조건 건너뜀
        #             trace(s, t, i - 1, j, path, results, dp)

        m, n = len(s), len(t)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # s가 비어 있는데 t가 비어 있지 않다 → 만들 수 있는 방법은 0개
        for j in range(n):
            dp[0][j] = 0

        #  s에서 아무 문자도 선택하지 않고도 항상 t를 만들 수 있다!
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # 선택(현재 문자를 사용해서 맞출지, 현재 문자를 무시하고 넘어갈지)
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # 현재 문자를 무조건 건너뛰어야 함.
                    dp[i][j] = dp[i - 1][j]
        # print(dp)

        # results = []
        # trace(s, t, m, n, [], results, dp)

        # print("총 경우의 수:", dp[m][n])
        # print("가능한 subsequence 조합:")
        # for r in results:
        #     print("-", r)

        return dp[m][n]

