# solution 1 - (set,greedy,hash table) - (0ms) - (2025.07.25)
from typing import List
class Solution:
    def maxSum(self, nums: List[int]) -> int:

        elements = set()
        answer = 0
        top = -100
        positive = False
        for num in nums:
            if num not in elements and num > 0:
                elements.add(num)
                answer += num
                positive = True
            elif num <= 0 and top < num:
                top = num

        if not positive:
            return top

        return answer
