# solution 1 - (prefix sum,modular, defaultdict) - (398ms,79ms) - (2024.10.03,2025.11.30)
from typing import List
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total_sum = sum(nums)
        remain = total_sum % p

        if remain == 0:
            return 0

        res = len(nums)
        cur_sum = 0

        # map remain of prefix sums to "last idx"
        remain_to_idx = {
            0: -1
        }

        for i, n in enumerate(nums):
            # remain + x = cur_sum  -> cur_sum = x - remain
            cur_sum = (cur_sum + n) % p
            prefix = (cur_sum - remain + p) % p

            if prefix in remain_to_idx:
                length = i - remain_to_idx[prefix]
                res = min(res, length)

            remain_to_idx[cur_sum] = i

        return -1 if res == len(nums) else res

# solution 2
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        total_sum = sum(nums)
        target = total_sum % p

        # 전체 합이 p 로 나누어 떨어지면 이미 조건을 만족함
        if target == 0:
            return 0

        prefix_sum = 0
        min_length = float('inf')
        prefix_map = {0: -1}  # prefix_sum % p 값을 인덱스에 매핑

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            needed = (prefix_sum - target) % p

            if needed in prefix_map:
                min_length = min(min_length, i - prefix_map[needed])

            prefix_map[prefix_sum] = i

        return min_length if min_length < len(nums) else -1

