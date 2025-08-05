# solution1 - (two pointers,brute force) - (22ms) - (2025.08.05)
from typing import List
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        n = len(fruits)
        visited = set()

        for i in range(n):
            for j in range(n):
                if j not in visited and fruits[i] <= baskets[j]:
                    visited.add(j)
                    break
        # print(visited)

        return n - len(visited)



