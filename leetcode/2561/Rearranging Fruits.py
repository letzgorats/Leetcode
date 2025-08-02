# solution 1 - (array,hash table,frequency,sort) - (135ms) - (2025.08.02)
from collections import Counter
from typing import List
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        basket1_freq = Counter(basket1)
        basket2_freq = Counter(basket2)

        total = Counter(basket1 + basket2)

        # 총 개수가 짝수개여야 한다.
        if any(v % 2 == 1 for v in total.values()):
            return -1

        target = {k: v // 2 for k, v in (basket1_freq + basket2_freq).items()}

        # basket1 에서 과하게 있는 값들(옮겨야 할 값들)
        extra1 = []
        # basket2 에서 과하게 있는 값들(옮겨야 할 값들)
        extra2 = []

        for k in total:
            diff1 = basket1_freq[k] - target[k]
            diff2 = basket2_freq[k] - target[k]
            if diff1 > 0:
                extra1.extend([k] * diff1)
            if diff2 > 0:
                extra2.extend([k] * diff2)

        extra1.sort()
        extra2.sort(reverse=True)  # 큰 값부터 매칭시키기 위해 내림차순
        # print(extra1)
        # print(extra2)
        # 한쪽만 보면 됨 : 두 바구니가 동일한 길이의 초과 항목을 가짐
        swaps = len(extra1)
        min_elem = min(total.keys())

        cost = 0
        for i in range(swaps):
            a = extra1[i]
            b = extra2[i]
            # a,b를 직접 swap 하는 비용 (min(a,b)) vs 간접 swap 비용(2*min_elem)
            cost += min(min(a, b), 2 * min_elem)

        return cost


'''
각 바구니에서 현재보다 많이 가진 과일들을 빼내어 상대 바구니로 보내야 함.
swap 대상은 정확히 과잉 요소의 개수를 기준으로 해야 함

이때 최소 비용을 위해:
    - 직접 swap
    - or 가장 작은 과일과 2번 swap (2 * min(all_elements))

test cases

[1,2,2,2,4,4,5,5,5,5]
[1,1,1,2,3,3,5,5,5,5]
[1,1,2,2,2,4,4,4,4,3,3,3,3,4,4,4]
[1,1,1,1,2,2,3,3,3,4,4,5,5,6,6,7]
[10,10,20,20,20,30,40,40,40,50,50,60,60,70]
[10,10,20,20,20,30,30,30,40,50,50,60,60,70]
[1,1,2,2,2,2,3,4,4,4,5,5,5,5,5,5]
[1,1,1,1,2,2,3,3,3,3,3,4,5,5,5,5]
[7,7,7,8,8,8,8,9,9,9,9]
[7,7,7,7,7,8,8,9,9,9,9]
[100,100,200,200,200,200,300,400,400,400,400,400]
[100,100,100,100,200,200,300,300,300,400,400,400]
[1,1,1,2,2,3,4,4,4,5,5,5,5]
[1,1,1,1,1,2,2,2,2,3,3,3,4]
[3,3,3,4,4,4,5]
[3,3,3,5,5,5,4]

For the test case
[84,80,43,8,80,88,43,14,100,88]
[32,32,42,68,68,100,42,84,14,8]

extra1 = [43, 80, 88]
extra2 = [68, 42, 32]

We can do it like this: 
 - min(80, 8) = 8;
 - min(8, 32) = 8;
 - min(88, 8) = 8;
 - min(8, 42) = 8;
 - min(43, 8) = 8;
 - min(8, 68) = 8.

Here, the total cost is 6 × 8 = 48. 
By repeatedly using the smallest number from both sides, we can achieve this.



'''
