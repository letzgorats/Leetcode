# solution 1 - (array,dp) - (3997ms) - (2025.07.17)

from typing import List
from collections import defaultdict

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 1

        for i in range(n):
            for j in range(i):
                mod = (nums[j] + nums[i]) % k
                if dp[j][mod]:
                    dp[i][mod] = max(dp[i][mod], dp[j][mod] + 1)
                else:
                    dp[i][mod] = max(dp[i][mod], 2)  # 새롭게 길이 2 시작 가능
                max_len = max(max_len, dp[i][mod])

        return max_len


# solution 2 - (dp) - (1368ms) - (2025.07.17)
from typing import List
from collections import defaultdict


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # dp[i][j] : i와 j로 끝나는 유효한 subsequence의 길이
        # i, j는 각각 nums 원소를 k로 나눈 나머지값, 즉 0부터 k-1까지의 값
        dp = [[0] * k for _ in range(k)]
        answer = 0

        # dp[prev][curr] : prev와 curr로 끝나는 subsequence의 최대 길이
        # (prev, curr)라는 나머지 쌍이 마지막 두 수인 subsequence의 최대 길이
        for num in nums:
            num %= k
            for prev in range(k):
                # 이전에 (num, prev)로 끝나는 subsequence가 있었다면,
                # 그 다음에는 (prev, num)을 붙여서 새로운 subsequence를 만들 수 있어.
                # 왜?
                # → (prev + num)과 (num + prev)는 같은 값을 k로 나눈 나머지를
                # 가지기 때문!
                dp[prev][num] = dp[num][prev] + 1
                answer = max(answer, dp[prev][num])

        return answer


'''
정리
dp[num][prev] : 과거 끝 쌍
dp[prev][num] : 현재 끝 쌍

즉, num이 새로 등장했을 때,
num 앞에 어떤 prev가 오더라도 dp[num][prev]를 바탕으로
새로운 subsequence (prev, num)을 만들 수 있는 구조야.
'''