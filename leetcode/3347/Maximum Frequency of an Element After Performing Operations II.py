# solution 1 - (binary search, sliding window,Counter,sorting) - (1746ms) - (2025.10.22)
from bisect import bisect_left, bisect_right
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        def check(nums, n, t, m):
            '''
            nums : 정렬된 숫자 배열
            n(target) : 중심으로 맞추고 싶은 값
            t(tolerance) : 한 번의 연산으로 이동할 수 있는 범위(즉, k)
            m(moves) : 남은 연산횟수(numOperations)

            return

            현재 중심값 nL을 기준으로,
            양쪽에서 k 거리 안에 있는 애들 중 numOperations번만 골라서 nL로 바꿀 수 있다면,
            최대로 만들 수 있는 nL의 개수 = 원래 nL의 개수 + min(numOperations, 주변 후보 수)
            '''
            nL = n  # 중심값(target)
            tL = t  # 이동 가능 범위 k
            l = bisect_left(nums, nL)  # nums 에서 처음으로 nL 이상인 인덱스(target 구간 시작)
            h = bisect_right(nums, nL)  # nums에서 처음으로 nL보다 큰 인덱스(target 구간 끝)
            ll = bisect_left(nums, nL - tL)  # [nL-tL] 이상 시작 인덱스 (좌측 윈도우 경계)
            hh = bisect_right(nums, nL + tL)  # [nL+tL] 초과 경계 인덱스 (우측 윈도우 경계)

            res = (hh - h) + (l - ll)  # 오른쫑세서 nL+k 이내인 원소 개수 - 왼쪽에서 nL-k 이내인 원소 개수
            return min(m, res) + (h - l)  # (h-l) : 원래 값이 정확히 nL인 원소 개수

        nums.sort()
        ans = 1
        for i in range(len(nums) - 1):
            ans = max(ans, check(nums, nums[i], k, numOperations))
            ans = max(ans, check(nums, nums[i] - k, k, numOperations))
            ans = max(ans, check(nums, nums[i] + k, k, numOperations))

        return ans

# solution 2 - (defaultdict,prefix sum) - () -(2025.10.22)
'''
“타깃이 배열에 있을 때”와 “타깃이 배열에 없을 때”를 분리해서, 
두 경우의 최댓값을 각각 슬라이딩 윈도우로 구한 뒤 max로 합치는 방식
'''
from collections import defaultdict
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)

        # case 1 : 타깃이 배열에 있는 값일 때
        count = defaultdict(int)
        res = i = j = 0
        for num in nums:
            while j < n and nums[j] <= num + k:
                count[nums[j]] += 1
                j += 1
            while i < n and nums[i] < num - k:
                count[nums[i]] -= 1
                i += 1
            cur = min(j - i, count[num] + numOperations)
            res = max(res, cur)

        # case 2 : 타깃이 배열에 없는 값일 때
        i = 0
        for j in range(n):
            while nums[i] + k + k < nums[j]:
                i += 1
            res = max(res, min(j - i + 1, numOperations))
        return res