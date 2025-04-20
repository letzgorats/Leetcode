# solution 1 - (math, ceil, count) - (0ms) - (2025.04.20)
from math import ceil
from collections import Counter
from math import ceil


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers_count = Counter(answers)  # color(index) -> nums of rabbits
        rabbits = 0

        for num, freq in answers_count.items():
            group_size = num + 1
            group_count = ceil(freq / group_size)
            rabbits += group_size * group_count
        return rabbits


'''
각 토끼는 자신의 색깔을 가진 토끼가 자기 외에 num 명 더 있다고 대답했다.
->  즉, 이 토끼는 총 (num+1) 마리짜리 그룹에 속한다.
(ex) 토끼가 2라고 대답했다면?
"나 외에도 어딘가에 나랑 같은 색을 가진 토끼가 2마리 더 있다"
= 총 2(다른애들) + 1(나 자신) = 3마리의 토끼가 같은 색이라는 것을 알 수 있다.
그래서, 우리는 이 토끼가 속한 그룹이 "3마리짜리 그룹"이라는 것을 알 수 있다.

(ex) 왜 ceil(freq/(num+1)) 이냐면,
한 그룹에는 최대 num+1 마리만 있을 수 있는데, 어떤 num 값에 대해 count(그렇게 말한 토끼 수)가 
num+1 보다 크다면?
(ex) [2,2,2,2,2] -> "나랑 같은 색 토끼가 2명 더 있어" 라고 말한 토끼가 5명이나 있으니까
=> 하나의 그룹(3)으로는 부족하니까 2개의 그룹(6)이 필요하다.
즉, 그룹카운트는 ceil(freq/group_size) 로 해줘야 수용가능하다.

그리고, rabbit 에 group_size * group_count 를 더해주면 된다.
'''
