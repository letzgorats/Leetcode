# solution 1 - (backtracking,permutations,counter) - (7ms) - (2025.08.10)
from typing import List
from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        answer = []
        counter = Counter(nums)

        def backtracking(cur):

            if len(cur) == len(nums):
                answer.append(cur)
                return

            for k in counter:
                if counter[k]:
                    counter[k] -= 1
                    backtracking(cur + [k])
                    counter[k] += 1

        backtracking([])

        return answer

'''
counter 를 backtracking() 의 인자로 주지 않아도 각 호출 시점에서 당시의 값을 "기억"한다.
그 이유는 파이썬의 클로저(closure)+가변 객체 참조 때문이다.

1. 왜 counter 를 인자로 안 줘도 되는가?
- counter 는 permuteUnique() 함수 안에서 한 번 생성되고,
  backtracking() 함수는 이 변수를 자신이 속한 스코프(외부 함수의 로컬 변수)에서 참조한다.
- 이런 변수를 자유변수(free variable)라고 하며, 파이썬은 이를 클로저로 캡처한다.
- 즉, backtracking() 이 호출될 때마다 같은 counter 객체를 참조한다.

2. 그렇다면, counter가 어떻게 변하는가?
- Counter 는 mutable(가번)객체이기 떄문에, 한 호출에서 counter[k]-=1 로 수정하면, 그 모든 변경이 모든 호출 스택에 공유된다.
- 그래서 재귀 호출 전에 counter[k] 를 줄였다가, 재귀가 끝난 후 원상복구(counter[k] += 1) 를 해줘야 한다.
- 이 원상복구 과정이 없으면 다른 분기(branch)에서도 변경된 상태가 누적되어 잘못된 결과가 나온다.

'''