# solution 1 - (dfs,dp) - (422ms) - (2025.10.13)
MOD = 10 ** 9 + 7
from functools import lru_cache
import math
from typing import List

class Solution:
    def magicalSum(self, total_count: int, target_odd: int, numbers: List[int]) -> int:

        @lru_cache(None)
        def dfs(remaining, odd_needed, index, carry):
            if remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed:
                return 0
            if remaining == 0:
                return 1 if odd_needed == carry.bit_count() else 0
            if index >= len(numbers):
                return 0

            ans = 0
            for take in range(remaining + 1):
                ways = math.comb(remaining, take) * pow(numbers[index], take, MOD) % MOD
                new_carry = carry + take
                ans += ways * dfs(remaining - take, odd_needed - (new_carry % 2), index + 1, new_carry // 2)
                ans %= MOD
            return ans

        return dfs(total_count, target_odd, 0, 0)

"""
아이디어 요약 (Digit DP + 조합수):
- 목표: numbers의 각 위치(=비트 자리라고 생각)에서 total_count개의 동일 아이템을 분배해가며, 
        전체 합을 2진수로 봤을 때 홀수 비트(=1의 개수) 가 정확히 
        target_odd가 되도록 하는 경우의 수를 구한다. 
        각 위치 j에서 take개를 배정하면 그 위치의 기여도는 numbers[j]^take이며, 
        동일 아이템을 분배하는 경우의 수는 C(remaining, take)가 된다.
- 핵심은 이진 덧셈의 자리올림(carry) 을 명시적으로 추적하는 Digit DP:
    - 현재 자리에서의 “합”의 홀짝은 (carry + take) % 2 로 결정되고,
    - 다음 자리로 넘어갈 새 캐리는 floor((carry + take)/2) 이다.
    - 결국 “전체 홀수 비트의 개수”는 각 자리에서의 (carry + take) % 2 들의 합 + 마지막에 남은 캐리의 비트수(carry.bit_count())와 같다.

dfs(remaining, odd_needed, index, carry)

    - remaining: 앞으로 분배해야 할 아이템 수

    - odd_needed: 앞으로 만들어야 할 “홀수 비트(1)의 개수” (남은 자리 포함)

    - index: 현재 처리 중인 자리(=numbers의 인덱스)

    - carry: 지금 자리로 들어온 캐리(정수). 이진수로 여러 비트가 켜져 있을 수 있음


구현 포인트:
    - 조합수 C(n,k) 와 거듭제곱은 매 번 모듈러로 계산.
    - 동일 상태 재방문을 위해 lru_cache로 메모이제이션.
    - 시간 복잡도는 상태공간 O(total_count * target_odd * len(numbers) * 평균 carry 범위) 에서, 프루닝과 캐시로 실제는 훨씬 줄어든다.

직관:
    - 각 index는 “이진 덧셈의 한 자리”로 본다.
    - 이 자리에서 take를 선택하면, “이 자리의 1 여부(홀짝)”가 정해지고, 그 영향은 캐리를 통해 다음 자리로 전파된다.
    - 남은 모든 자리의 1의 총합이 정확히 target_odd가 되도록 분배/선택의 조합을 전부 더한 값이 정답.
    
"""