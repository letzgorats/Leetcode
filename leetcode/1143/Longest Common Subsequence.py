# solution 1 - dp, LCS - (524ms) - (2024.07.25)
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        n = len(text1)
        m = len(text2)

        # DP 테이블 초기화
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # DP를 사용하여 LCS 길이 계산
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        return dp[n][m]


# solution 2 - dp, LCS - (515ms) - (2025.03.22)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)

        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        # print(dp)

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # print(dp)

        return dp[n][m]

'''
LCS 의 전형적인 문제로, 주의할 점은 인덱스 처리인 것 같다.
text1이 m, text2 가 n 이니까 행x행 순회할 때, i,j를 잘 맞춰주는 것만 주의하면 된다.
첫 행과 첫 열이 다 0으로 채워지기 때문에(빈 문자열과 첫 문자의 공통수열은 당연히 빈 문자열이니까 0) 
2차원 배열의 길이는 n+1, m+1 이다.
dp 2차원 배열에서 마지막 끝에 위치하는 수가 답이다. 이 때도, n-1,m-1 자리가 아니라 n,m 이다.
'''
