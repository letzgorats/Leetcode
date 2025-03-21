# solution 2 - dp, LIS  - (2070ms) - (2024.07.05)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[j],dp[i]+1)
            # print(dp)

        return max(dp)
'''
nums = [10,9,2,5,3,7,101,18]

[1, 1, 1, 1, 1, 1, 2, 2]
[1, 1, 1, 1, 1, 1, 2, 2]
[1, 1, 1, 2, 2, 2, 2, 2]
[1, 1, 1, 2, 2, 3, 3, 3]
[1, 1, 1, 2, 2, 3, 3, 3]
[1, 1, 1, 2, 2, 3, 4, 4]
[1, 1, 1, 2, 2, 3, 4, 4]
'''

# solution 2 - bisect, LIS - (3ms) - (2025.03.22)
from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        tails = []
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                # 삽입
                tails.append(num)
            else:
                # 더 작은 값으로 교체
                tails[pos] = num
        return len(tails)

'''
nums = [0, 1, 0, 3, 2, 3]
# bisect_left(tails, num) : num이 들어갈 수 있는 위치를 이진탐색으로 찾음
# 작거나 같은 값만 유지 : 그 자리를 num으로 대체 (더 작은 값이 있으면 교체)

bisect_left(arr, x)는 x를 끼워넣을 수 있는 "가장 왼쪽" 위치의 인덱스를 반환
arr은 정렬된 상태여야 함 (우리에겐 항상 tails가 정렬돼 있음!)

1. num = 0
    tails = []
    bisect_left(tails, 0) → pos = 0
    tails = [0]
2. num = 1
    bisect_left([0], 1) → pos = 1
    tails = [0, 1] ← 길이 2 가 됨(삽입)
3. num = 0
    bisect_left([0, 1], 0) → pos = 0
    tails = [0, 1] → 0으로 교체해봤자 의미 없음 (값 유지) 
4. num = 3
    bisect_left([0, 1], 3) → pos = 2
    tails = [0, 1, 3] ← 길이 3 이 됨(삽입)
5. num = 2
    bisect_left([0, 1, 3], 2) → pos = 2
    tails = [0, 1, 2] ← 3보다 작으니 (교체) (길이는 그대로지만 마지막 값이 더 작아짐!)
6. num = 3
    bisect_left([0, 1, 2], 3) → pos = 3
    tails = [0, 1, 2, 3] ← 길이 4 가 됨(삽입)

→ 최종 LIS 길이 = len(tails) = 4
'''