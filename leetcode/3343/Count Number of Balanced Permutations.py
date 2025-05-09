# TLE
from itertools import permutations


class Solution:
    def countBalancedPermutations(self, num: str) -> int:

        mod = 10 ** 9 + 7
        candi = []
        n = len(num)
        answer = 0

        def backtracking(cur, idx, even_sum, odd_sum):
            nonlocal answer

            if len(cur) == n:
                if even_sum == odd_sum:
                    answer = (answer + 1) % mod
                return

            for num in counter:
                if counter[num] > 0:
                    counter[num] -= 1
                    if idx % 2 == 0:
                        backtracking(cur + num, idx + 1, even_sum + int(num), odd_sum)
                    else:
                        backtracking(cur + num, idx + 1, even_sum, odd_sum + int(num))
                    counter[num] += 1

        counter = Counter(num)
        backtracking("", 0, 0, 0)

        return answer % mod

# solution  - (dp,dfs) - (1179ms) - (2025.05.09)
from math import comb
from collections import Counter

class Solution:
    def countBalancedPermutations(self, num: str) -> int:

        # 각 숫자의 등장 개수를 카운트
        cnt = Counter(int(ch) for ch in num)

        # 모든 숫자의 총합
        total = sum(int(ch) for ch in num)

        # 캐싱을 위한 dfs 탐색 함수
        @cache
        def dfs(i, odd, even, balance):
            '''
            :param i: 현재 탐색 중인 숫자 (0 ~ 9)
            :param odd: 홀수 인덱스에 남아있는 자리 수
            :param even: 짝수 인덱스에 남아있는 자리 수
            :param balance: 짝수 자리 합 - 홀수 자리 합
            :return: 가능한 경우의 수
            '''

            # 모든 숫자를 다 채웠고, 합이 맞으면 1 반환
            if odd == 0 and even == 0 and balance == 0:
                return 1

            # 조건이 맞지 않으면 0 반환
            if i < 0 or odd < 0 or even < 0 or balance < 0:
                return 0

            # 가능한 모든 조합 탐색
            res = 0
            for j in range(0, cnt[i] + 1):
                """
                - j개는 홀수 인덱스에 배치
                - 나머지 (cnt[i] - j)는 짝수 인덱스에 배치
                - comb(odd, j) → 홀수 인덱스에 j개를 배치하는 경우의 수
                - comb(even, cnt[i] - j) → 짝수 인덱스에 남은 개수 배치
                """
                res += (
                        comb(odd, j) *  # 홀수에 배치 가능한 경우의 수
                        comb(even, cnt[i] - j) *  # 짝수에 배치 가능한 경우의 수
                        dfs(i - 1,  # 다음 숫자로 이동
                            odd - j,  # 홀수에 배치된 개수 빼기
                            even - cnt[i] + j,  # 짝수에 배치된 개수 빼기
                            balance - i * j  # balance 업데이트
                            )
                )

            return res % 1000000007

        # 총합이 홀수면 불가능 -> 0 반환
        # 총합이 짝수면 dfs 탐색 시작
        return 0 if total % 2 else dfs(9, len(num) - len(num) // 2, len(num) // 2, total // 2)

'''
|               | `math.comb`              | `itertools.combinations`      |
| ------------- | ------------------------ | ------------------------------|
| 설명           | 조합의 개수를 계산합니다.(int)  | 조합을 실제로 생성합니다.(tuple)    |
| 리턴 값         | 정수 (조합의 개수)           | 조합의 실제 리스트 (Iterator)      |
| 메모리 사용      | 매우 적음 (정수만 반환)       | 리스트 생성 → 메모리 사용           |
| 시간 복잡도      | O(k)                     | O(nCk)                        |
| Python 버전    | Python 3.8 이상           | Python 2.x 이상                |

from math import comb
from itertools import combinations

# comb는 개수만 알려줌
print("comb(5, 2):", comb(5, 2))  # Output: 10

# combinations는 실제 조합을 생성해줌
print("combinations([1, 2, 3, 4, 5], 2):", list(combinations([1, 2, 3, 4, 5], 2)))

comb(5, 2): 10
combinations([1, 2, 3, 4, 5], 2): 
[(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]


'''