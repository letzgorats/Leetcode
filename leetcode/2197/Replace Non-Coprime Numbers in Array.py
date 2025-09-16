# solution 1 - (coprime,number,math) - (97ms) - (2025.09.16)
from typing import List
import math
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        ans = []

        for num in nums:
            while ans:
                g = math.gcd(ans[-1], num)
                if g == 1:
                    break  # co-prime
                num = (ans.pop() * num) // g
            ans.append(num)

            # print(ans)
        return ans

