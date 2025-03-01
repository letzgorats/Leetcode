# solution 1 - dp - lcs - (407ms) - (20205.02.28)
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:

        m, n = len(str1), len(str2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # LCS 찾기 (bottom-up)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # print(dp)

        # LCS 를 따라 SCS 만들기
        i, j = m, n
        scs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # LCS 문자 포함
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # 위쪽이 더 크다면, str1 문자 추가
                scs.append(str1[i - 1])
                i -= 1
            else:  # 왼쪽이 더 크다면, str2 문자 추가
                scs.append(str2[j - 1])
                j -= 1

        # print(scs)

        # 남은 문자 추가(s) (str1 또는 str2 중 한쪽이 먼저 끝난 경우)
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1

        # print(scs)

        return "".join(reversed(scs))  # 뒤집어서 반환