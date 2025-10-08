# solution 1 - (array,sorting,binary search) - (619ms) - (2025.10.08)
from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        m = len(potions)
        n = len(spells)
        res = []

        for spell in spells:

            left, right = 0, m - 1
            while left <= right:

                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            res.append(m - left)

        return res