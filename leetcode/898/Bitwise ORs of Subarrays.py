# solution 1 - (subarray, bitwise) - (443ms) - (2025.07.31)
from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # 전체에서 등장한 모든 or 결과를 누적한 집합
        answer = set()
        # 현재 위치에서 끝나는 모든 연속된 subarray의 or 결과 집합
        curr = set()

        for num in arr:
            curr = {num | x for x in curr} | {num}
            answer |= (curr)

            # print(answer)
        return len(answer)


'''
직전까지 만들었던 연속 subarray들의 or 결과(curr)에 현재 숫자 num 을 
붙이면, 여전히 subarray 이다.

그래서, 모든 x in curr 에 대해 x | num 을 계산하고, 
num 하나만 있는 subarray도 포함한다.

answer 에 현재 curr 을 누적한다.
즉, 지금까지 나온 모든 or 값을 집합에 저장한다.
집합 | 집합 = 합집합
'''

'''
겉으로 보기엔 curr = {num | x for x in curr} | {num}
때문에 이중 루프처럼 보여 O(N^2)인 것처럼 느껴질 수 있다.

하지만, 실제로 curr 의 크기는 O(30) 이하로 유지된다. 
arr[i] 는 최대 10억(2^30) -> 최대 30비트
bitwise OR 는 계속 값이 커지기만 하고, 중복되는 결과도 많다.
즉, 하나의 num 에서 파생 가능한 OR 값은 매우 제한적이다.
-> 실제로 대부분의 경우 curr 의 크기는 10~40 이하로 유지된다.
-> 최악의 시간복잡도는 O(N*Window)(Window = unique OR values in a window~=30~40) 
즉, 각 단계마다 curr 집합은 OR 연산의 성질로 인해 크게 증가하지 않는다.

아래와 같이 진짜 이중 포문은 절대 통과를 못하긴 한다.
for i in range(n):
    or_val = 0
    for j in range(i,n):
        or_val |= arr[j]
        res.add(or_val)
-> 이건 진짜로 O(N^2) 이고, 절대 통과 안 된다!
'''