# solution 1 - (sliding window) - (183ms) - (2025.08.04)
from collections import defaultdict
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        basket = defaultdict(int)
        left = 0
        ans = 0

        for r in range(len(fruits)):
            basket[fruits[r]] += 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            ans = max(ans, r - left + 1)

        return ans