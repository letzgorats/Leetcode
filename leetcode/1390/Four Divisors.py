from collections import defaultdict
from typing import List
import math

# solution 1 - (array,math,sqrt) - (166ms) - (2026.01.04)

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        four_divisors = defaultdict(int)
        answer = 0
        for num in nums:
            if num in four_divisors:
                answer += four_divisors[num]
                continue
            counts = []
            for i in range(1, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    counts.append(i)
                    if i ** 2 != num:
                        counts.append(num // i)

                if len(counts) > 4:
                    break

            if len(counts) == 4:
                four_divisors[num] = sum(counts)
                answer += four_divisors[num]

        return answer
