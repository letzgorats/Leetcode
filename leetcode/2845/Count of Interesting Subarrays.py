# solution 1 - (prefix,hash table) - (163ms) - (2025.04.25)
from collections import defaultdict
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        interesting_or_not = [0] * len(nums)

        for i, num in enumerate(nums):
            if num % modulo == k:
                interesting_or_not[i] = 1

        answer = 0
        prefix_sum = 0
        hash_table = defaultdict(int)  # 지금까지 나온 누적합의 나머지
        hash_table[0] = 1  # prefix_sum = 0 도 하나의 상태로 인정

        for r, num in enumerate(interesting_or_not):
            prefix_sum += num
            target = (prefix_sum - k) % modulo
            answer += hash_table[target]
            hash_table[prefix_sum % modulo] += 1

        return answer

    '''
    우리는 아래 조건을 만족하는 left 의 개수를 알고 싶은 것이다.(=target)
    prefix_sum[r] - prefix_sum[l-1] ≡ k (mod modulo)

    이걸 다시 정리하면, 
    prefix_sum[r] - k ≡ prefix_sum[l-1] (mod modulo)

    지금의 prefix_sum[r] 이 있을 때,
    이전에 prefix_sum[l-1] % modulo == (prefix_sum[r]-k) % modulo 였던 구간의 수만큼
    -> 조건을 만족한느 subarray 가 있다는 뜻

    hash_table[prefix_sum % modulo]의 key: 지금까지 나온 나머지 상태

    hash_table[prefix_sum % modulo]의 value: 그 나머지가 나온 횟수

    매 순간 target = (prefix_sum - k) % modulo를 계산해서,

    이 상태가 과거에 몇 번 있었는가를 기반으로 정답을 누적해줌
    '''



