# solution 1 - dynamic programming, LCS, subsequence, dp - (196ms) - (2025.03.22),(2026.01.08)
from typing import List
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        n, m = len(nums1), len(nums2)

        # 이 문제는 무조건 한 쌍 이상 선택해야 하므로, -inf 초기화가 필수!
        dp = [[float('-inf') for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prod = nums1[i - 1] * nums2[j - 1]

                dp[i][j] = max(
                    prod,  # 새 subsequence 시작
                    dp[i - 1][j - 1] + prod,  # 기존 subsequence에 이어 붙임
                    dp[i - 1][j],  # nums1[i-1] 무시
                    dp[i][j - 1]  # nums2[j-1] 무시
                )
                # # 현재 요소를 포함하고 새로운 subsequence 시작
                # option1 = nums1[i-1] * nums2[j-1]

                # # 현재 요소를 이전 subsequence에 포함 (확장)
                # option2 = dp[i-1][j-1] + prod

                # # nums1[i-1] 을 안 쓰고 넘어감
                # option3 = dp[i-1][j]

                # # nums2[j-1] 을 안 쓰고 넘어감
                # option4 = dp[i][j-1]

                # 최댓값을 선택
                # dp[i][j] = max(option1,option2,option3,option4)

        return dp[n][m]

'''
nums1 = [2,1,-2] , nums2 = [3,-6,7]

i\j	    ""	      3	    -6	    7
""	    -inf	-inf	-inf	-inf
2	    -inf	6	    6	    14
1	    -inf	6	    6	    14
-2	    -inf	6	    18	    18

dp[i][j]는 nums1[:i], nums2[:j]까지 고려했을 때의 max dot product를 의미

(ex) i=1, j= 1
값	            의미	                        결과
prod	        새 subsequence 시작(2×3)	    6      -> 선택
dp[0][0]	    -inf (초기화 값)	            -inf
dp[0][0]+prod	-inf + 6	                -inf
dp[0][1]	    -inf	                    -inf
dp[1][0]	    -inf	                    -inf

(ex) i=1, j= 3
값	            의미	                        결과
prod	        새 subsequence 시작 (2×7)	    14     -> 선택
dp[0][2]	    대각선 왼쪽 위	                -inf
dp[0][0]+prod	기존 subsequence에 이어 붙임	-inf
dp[0][3]	    위쪽 (nums1 무시)	            -inf
dp[1][2]	    왼쪽 (nums2 무시)	            6

(ex) i=2, j= 2
값	            의미	                        결과
prod	        새 subsequence 시작 (1×(-6))	-6
dp[0][2]	    대각선 왼쪽 위	                6      -> 선택
dp[1][1]+prod	기존 subsequence에 이어 붙임	6-6 = 0
dp[1][2]	    위쪽 (nums1 무시)	            6
dp[2][1]	    왼쪽 (nums2 무시)	            6

dp[2][2] = 6은 subsequence 쌍 [2], [3] 을 선택하고, 그 이후 쌍 (1, -6)은 무시한 결과!

(ex) i=3, j= 2
값	            의미	                        결과
prod	        새 subsequence 시작 (-2×(-6))	12
dp[2][1]	    대각선 왼쪽 위	                6      
dp[2][1]+prod	기존 subsequence에 이어 붙임	6+12 = 18  -> 선택
dp[2][2]	    위쪽 (nums1 무시)	            6
dp[3][1]	    왼쪽 (nums2 무시)	            

dp[3][2] = 18은 dp[2][1] + prod에서 왔다! nums1: [2, -2], nums2: [3, -6] 인 결과!
'''

