# solution 1 - (hash table, count) - (71ms) - (2025.10.16)
from typing import List
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        cnt = [0] * value

        for x in nums:
            cnt[x % value] += 1

        # print(cnt)

        i = 0
        while True:
            r = i % value
            if cnt[r] > 0:
                cnt[r] -= 1
                i += 1
            else:
                return i

            # print(cnt)

# TLE
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:

        non_negative = set()

        for i in range(len(nums)):
            x = (nums[i] % value)

            if x == 0:
                if x in non_negative:
                    while x in non_negative:
                        x += value
                non_negative.add(x)
            else:
                if x in non_negative:
                    if x < value:
                        while x in non_negative:
                            x += value
                    elif x >= value:
                        while x in non_negative:
                            x -= value
                non_negative.add(x)

        # print(non_negative)
        for i in range(max(non_negative) + 1):
            if i not in non_negative:
                return i

        return i + 1