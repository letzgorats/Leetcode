# solution 1 - (defaultdict,hash table,math) - (75ms) - (2025.12.02)
import math
from typing import List
from collections import defaultdict
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:

        y_group = defaultdict(int)
        MOD = 10 ** 9 + 7

        for x, y in points:
            y_group[y] += 1

        # print(y_group)

        candi = []
        for y_cnt in y_group.values():
            if y_cnt >= 2:
                candi.append(y_cnt * (y_cnt - 1) // 2)

        # print(candi)
        if len(candi) < 2:
            return 0

        total_sum = sum(candi) % MOD
        sum_of_squares = sum((x * x) % MOD for x in candi) % MOD
        ans = (total_sum * total_sum - sum_of_squares + MOD) * pow(2, MOD - 2, MOD) % MOD

        return ans % MOD


'''
기존 목표는 candi 리스트에 있는 모든 요소 쌍(candi[i],candi[j]) 의 곱을
구해서 합치는 것이었다.
예를 들어, candi = [a,b,c] 가 있다고 가정해본다면, 우리가 구하고자 하는 값
ans 는 아래와 같다.
ans = (a x b) + (a x c) + (b x c)
이중 반복문은 위 식을 순차적으로 계산했다.

최적화 아이디어 : 곱셈 공식 활용
-> 완전 제곱식을 떠올려본다면, 합의 제곱은 각 항의 제곱과 모든 쌍의 곱의 합으로 이루어져있다.
(a+b+c)^2 = (a^2+b^2+c^2) + 2 x (a x b + a x c + b x c)

우리가 구하고 싶은 부분이 바로 괄호 안의 "모든 쌍의 곱의 합" 부분이다!

이 공식을 우리가 원하는 ans 에 대해 다시 정리해본다면,
ans x 2 = (a+b+c)^2-(a^2+b^2+c^2)
ans = (a+b+c)^2 - (a^2+b^2+c^2) // 2 이다.

total_sum = sum(candi) -> (a+b+c)

sum_of_squares = sum((x*x) for x in candi) -> (a^2+b^2+c^2)

ans = ((total_sum)^2- (sum_of_squares)) // 2
(단, pow(2,MOD-2,MOD) 부분이 '2로 나누는 것과 같은 효과를 주는 수'(즉,2의 모듈러 역원)를 
계산해준다. 페르마의 소정리(Fermat's Little Theorem)를 이용한 방식이다. 
'+ MOD' 는 뺄셈 과정에서 결과가 음수가 되는 것을 방지하기 위한 안전장치이다.)
* pow(a,b,c) 와 같이 세 번째 인자는 modular 연산이다. == (a^b)%c
'''