# solution 1 - (hash table,sliding window) - (191ms) - (2025.07.22)
from typing import List
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        vals = set()
        curr = 0
        left = 0
        answer = 0

        for right, num in enumerate(nums):

            while num in vals:
                vals.discard(nums[left])
                curr -= nums[left]
                left += 1

            vals.add(num)
            curr += num
            answer = max(answer, curr)
            # print(curr,answer)
            # print(vals)

        return answer


# wrong answer
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        vals = set()
        curr = 0
        left = 0
        answer = 0

        for right, num in enumerate(nums):

            if num not in vals:
                curr += num
                vals.add(num)
            else:
                curr -= nums[left]
                vals.discard(nums[left])
                left += 1
                while left <= right and num == nums[left]:
                    curr -= nums[left]
                    vals.discard(nums[left])
                    left += 1

                curr += num
                vals.add(num)

            answer = max(answer, curr)
            # print(curr,answer)
            # print(vals)

        return answer