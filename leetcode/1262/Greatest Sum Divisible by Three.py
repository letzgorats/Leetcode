# solution 1 - (lru_cache + backtrack) - (327ms) - (2025.11.23)
from functools import lru_cache
from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()

        @lru_cache(None)
        def backtrack(idx, r):
            if idx == len(nums):
                return 0 if r == 0 else -float('inf')

                # skip
            skip = backtrack(idx + 1, r)
            # assign
            assign = nums[idx] + backtrack(idx + 1, (r + nums[idx]) % 3)

            return max(skip, assign)

        return backtrack(0, 0)

# solution 2 - (sort,math,simulation) - (17ms) - (2025.11.23)
from functools import lru_cache
from typing import List
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        S = sum(nums)
        if S % 3 == 0:
            return S

        rem1 = sorted([x for x in nums if x % 3 == 1])
        rem2 = sorted([x for x in nums if x % 3 == 2])

        if S % 3 == 1:
            cand = []
            if rem1:
                cand.append(rem1[0])  # 나머지가 1인 수 1개 제거
            if len(rem2) >= 2:
                cand.append(rem2[0] + rem2[1])  # 나머지가 2인 수 2개 제거

            # 둘 중 "제거하는 값의 합이 최소"인 것을 선택
            return S - min(cand) if cand else S

        else:
            cand = []
            if rem2:  # 나머지가 2인 수 1개 제거
                cand.append(rem2[0])
            if len(rem1) >= 2:  # 나머지가 1인 수 2개 제거
                cand.append(rem1[0] + rem1[1])

            # 둘 중 "제거하는 값의 합이 최소"인 것을 선택
            return S - min(cand) if cand else S


# MLE
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        nums.sort()
        max_val = 0

        @lru_cache(None)
        def backtrack(cur, idx):
            nonlocal max_val

            if idx == len(nums):
                if cur % 3 == 0:
                    max_val = max(max_val, cur)
                return

            # skip
            backtrack(cur, idx + 1)
            # assign
            backtrack(cur + nums[idx], idx + 1)

        backtrack(0, 0)

        return max_val
