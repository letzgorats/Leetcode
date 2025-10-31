# solution 1 - (greedy) - (3ms) - (2025.10.31)
from collections import Counter
from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        cnts = Counter(nums)
        ans = []
        for k, v in cnts.items():

            if v == 2:
                ans.append(k)

        return ans

# solution 2 - (greedy,array) - (0ms) - (2025.10.31)
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        ans = []
        visited = set()
        for num in nums:
            if num in visited:
                ans.append(num)
            else:
                visited.add(num)

        return ans