# solution 1 - (hash_table,dict) - (22ms) - (2025.06.30)
from collections import defaultdict, Counter
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:

        answer = 0
        hash_table = Counter(nums)

        for k, v in hash_table.items():

            if k - 1 in hash_table:
                answer = max(answer, v + hash_table[k - 1])

        return answer
