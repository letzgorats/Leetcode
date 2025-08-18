# solution 1 - (backtracking,math) - (113ms) - (2025.08.18)
from fractions import Fraction
from typing import List
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        nums = [Fraction(x, 1) for x in cards]

        def backtracking(arr):

            if len(arr) == 1:
                return arr[0] == 24

            # 두 수를 순서있게 고르고 (빼기/나눗셈은 순서 중요)
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):

                    a, b = arr[i], arr[j]

                    # i+1 을 통해 (i,j) 쌍만 고름 -> 중복 절반 감소( (j,1)는 따로 고르지 않음)
                    # rest 는 이번에 쓰지 않은 나머지 숫자들
                    rest = [arr[k] for k in range(len(arr)) if k not in (i, j)]

                    candidates = [
                        a + b,
                        a - b,
                        b - a,
                        a * b,
                    ]
                    if b != 0:
                        candidates.append(a / b)
                    if a != 0:
                        candidates.append(b / a)

                    for val in candidates:
                        if backtracking(rest + [val]):
                            return True
            return False

        return backtracking(nums)


'''
- 숫자 4개를 매 단계마다 두 개 골라 연산해서 하나로 줄이는 과정을 반복하면, 모든 괄호 배치(수식의 연산 순서)를 자연스럽게
  전부 탐색할 수 있다.
    (예시)  ((a◦b)◦c)◦d, (a◦(b◦c))◦d, a◦((b◦c)◦d) … 같은 모든 괄호 구조가, 
        “두 개 고르고 → 결과를 넣고 → 다시 두 개 고르고 …”를 재귀로 반복하면 다 나온다.

- Fraction은 유리수(분자/분모)로 딱 떨어지는 정확한 연산을 제공한다. (0 나누기만 조심하면 된다.)

- backtracking(arr):
    기저 조건 : len(arr) == 1 이면 arr[0] = 24 여부 반환
    재귀 전개 :
            - 모든 서로 다른 두 인덱스(i,j)를 선택(i<j 로 중복 절반 제거)
            - 선택한 두 수 a=arr[i],b=arr[j]를 연산 후보들로 결합
                - a+b, a-b, b-a, a*b, 그리고 a/b(b!=0), b/a(a!=0)
                - 덧셈/곱셈은 교환법칙이 있으니까, a+b만 만들어도 충분(이미 i<j 로 쌍을 한 번만 뽑음)
                - 뺼셈/나눗셈은 "순서가 다르면 결과가 달라질 수 있기 때문"에 둘 다 시도.
            - 위 후보들 각각을 rest+[val] 로 붙여 넣고 재귀 호출
            - 하나라도 True 면 즉시 True 반환(조기 종료)


'''