# solution 1 - (simulation,greedy,operations) - (3396ms) - (2025.10.28)
from collections import deque
from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        def is_valid(pos, direction, tmp):
            '''
            process 진행하는 함수
            '''
            while 0 <= pos < n:

                if tmp[pos] != 0:
                    tmp[pos] -= 1
                    direction = -direction  # 방향 전환
                pos += direction

            return tmp

        q = deque([])
        for i, num in enumerate(nums):
            if num == 0:
                q.append(i)

        n = len(nums)
        ans = 0
        while q:

            pos = q.popleft()

            # left
            original_pos = pos
            tmp = nums[:]
            if sum(is_valid(pos - 1, -1, tmp)) == 0:
                ans += 1

                # right
            pos = original_pos
            tmp = nums[:]
            if sum(is_valid(pos + 1, 1, tmp)) == 0:
                ans += 1

        return ans

# solution 2 - (math) - (41ms) - (2025.10.28)
from typing import List
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:

        total = sum(nums)
        left_sum = 0
        ans = 0

        for num in nums:

            if num == 0:
                right_sum = total - left_sum
                if left_sum == right_sum:
                    ans += 2
                elif abs(left_sum - right_sum) == 1:
                    ans += 1
            else:
                left_sum += num

        return ans
