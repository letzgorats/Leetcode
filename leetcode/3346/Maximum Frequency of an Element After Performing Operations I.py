# solution 1 - (prefix sum, sliding window,Counter,sorting) - (533ms) - (2025.10.21)
from collections import Counter
from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        nums.sort()
        max_val = max(nums) + k + 2
        count = [0] * max_val

        for v in nums:
            count[v] += 1

        # print(count)

        for i in range(1, max_val):
            count[i] += count[i - 1]

        # print(count)

        res = 0
        for i in range(max_val):
            left = max(0, i - k)
            right = min(max_val - 1, i + k)
            total = count[right] - (count[left - 1] if left else 0)

            freq = count[i] - (count[i - 1] if i else 0)
            res = max(res, freq + min(numOperations, total - freq))

        return res

# solution 2
from collections import Counter
class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        Find maximum frequency after at most numOperations changes
        Each operation can change a number by at most k

        Strategy: Two-pass sliding window approach
        1. Target existing values (some elements need 0 ops)
        2. Target gap values (all elements need ops)

        :type nums: List[int] - array of integers
        :type k: int - maximum change per operation
        :type numOperations: int - maximum number of operations
        :rtype: int - maximum achievable frequency
        """
        nums.sort()
        n = len(nums)
        r = 0  # Result: maximum frequency found
        i = 0  # Left pointer for sliding window
        j = 0  # Right pointer for sliding window
        h = Counter()  # Counter to track frequencies

        # Strategy 1: Target existing values
        for a in nums:
            # Expand j to include all reachable values
            # ➡️ EXPAND WINDOW: Include all values reachable TO 'a'
            # Values in range [a-k, a+k] can reach 'a' with 1 operation
            while j < n and nums[j] <= a + k:
                h[nums[j]] += 1
                j += 1

            # Contract i to exclude unreachable values
            # ⬅️ CONTRACT WINDOW: Exclude values too far from 'a'
            # Values < a-k cannot reach 'a' within distance k
            while i < n and nums[i] < a - k:
                h[nums[i]] += 1
                i += 1

            # Calculate max frequency for target value 'a'
            c = min(j - i, h[a] + numOperations)
            r = max(r, c)

        # Strategy 2: Target gap values
        i = 0
        for j in range(n):
            # Find window where all can converge
            while nums[i] + k + k < nums[j]:
                i += 1
            r = max(r, min(j - i + 1, numOperations))

        return r