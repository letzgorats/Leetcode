# solution 1 - (dynamic programming,greedy,math) - (98ms) - (2025.07.17)
from functools import lru_cache
from typing import List
class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        # 짝수 + 짝수 = 짝수
        # 홀수 + 홀수 = 짝수

        # 홀수 + 짝수 = 홀수
        # 짝수 + 홀수 = 홀수

        # same parity
        # -> all even numbers
        # -> all odd numbers

        # alternating parity
        # -> even, odd, even, odd
        # -> odd, even, odd, even

        # 1. Count all even and odd numbers
        # -> this gives the max_len for same parity
        count_even = 0
        count_odd = 0
        for num in nums:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

        # 2. Use greedy like(dp tracking) for alternating parity
        # -> even_dp : max alternating sequence ending in even
        # -> odd_dp : max alternating sequence ending in odd
        # traverse the arrary
        # -> if it's even, update even_dp = max(even_dp,odd_dp+1)
        # -> if it's odd, update odd_dp = max(odd_dp,even_dp+1)

        even_dp = 0
        odd_dp = 0
        for num in nums:
            if num % 2 == 0:
                # "앞에 홀수 있었으면 내가 이어갈게!"
                even_dp = max(even_dp, odd_dp + 1)
            else:
                # "앞에 짝수 있었으면 내가 이어갈게!"
                odd_dp = max(odd_dp, even_dp + 1)

        return max(count_even, count_odd, even_dp, odd_dp)


'''

짝수를 넣으려면? 바로 앞에 홀수가 있어야 "홀짝 번갈아"가 되겠다.
-> 그래서 odd_dp + 1  이 가능한 것이다!
-> even_dp = max(even_dp,odd_dp+1)

홀수를 넣으려면? 바로 앞에 짝수가 있어야 "짝홀 번갈아"가 되므로
-> even_dp + 1 이 가능한 것이다.
-> odd_dp = max(odd_dp,even_dp+1)

'''