# solutio 1 - (sorting,array) - (104ms) - (2025.10.14)
from typing import List
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:

        def check_increasing(lst):
            for i in range(len(lst) - 1):
                if lst[i] < lst[i + 1]:
                    continue
                else:
                    return False
            return True

        n = len(nums)
        for i in range(n - k):

            a = nums[i:i + k]
            b = nums[i + k:i + 2 * k]
            if len(a) == len(b):
                if check_increasing(a) & check_increasing(b):
                    return True

        return False

# solution 2 - (slicing) - (77ms) - (2025.10.14)
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if 2 * k > n:
            return False

        # inc[i]: nums에서 i를 끝으로 하는 "엄격 증가" 구간 길이
        inc = [1] * n
        for i in range(1, n):
            inc[i] = inc[i-1] + 1 if nums[i-1] < nums[i] else 1

        # 두 구간 [s, s+k-1], [s+k, s+2k-1]가 모두 증가인지 확인
        for s in range(0, n - 2 * k + 1):
            if inc[s + k - 1] >= k and inc[s + 2 * k - 1] >= k:
                return True
        return False


