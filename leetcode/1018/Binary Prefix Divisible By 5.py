# solution 1 - (bin,string) - (787ms) - (2025.11.24)
from typing import List
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        cur = ''
        ans = []
        for i in range(len(nums)):

            cur += str(nums[i])

            if int(cur, 2) % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)

        return ans

# solution 2 - (bit manipulation) - (95ms) - (2025.11.24)
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        cur = 0
        ans = []
        for i in range(len(nums)):
            cur = cur << 1 | nums[i]

            ans.append(cur % 5 == 0)

        return ans