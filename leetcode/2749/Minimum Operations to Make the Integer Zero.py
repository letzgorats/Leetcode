# solution 1 - (math,bitwise) - (0ms) - (2025.09.05)
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        if num1 == 0:
            return 0

        # k -> 1...60 까지 확인(최솟값 찾는 순서)
        for k in range(1, 61):

            # S 의 의미 : 우리가 연산을 k번 했다면,
            # S는 k개의 2^i(2의 거듭제곱)합으로 표현돼야 한다.
            S = num1 - k * num2

            if S < 0:
                # 더 이상 k 를 늘리면 S 가 더 작아져서 불가능
                # num2 가 음수일 수 있으므로, '바로'탈출하진 않고 조건으로만 거른다.
                continue

            # 이진수의 1의 개수
            ones = S.bit_count()

            # 조건 체크 : 최소 항 개수 <= k <= 최대 항 개수
            # ones : 최소항의 개수
            # S : S 를 전부다 1로 쪼갠다고 생각하면, S가 쵀대항의 개수
            # 즉, 필요한 최소 항 개수보다는 많아야 하고, S보다는 많을 수 없음.
            # 이 바운더리 안에 들어오면 그게 답
            if ones <= k <= S:
                return k

        # 어떤 k 도 조건을 만족하지 못하면 -1
        return -1

"""
연산: 한 번에 num1 -= (2^i + num2),  i ∈ [0, 60]
k번 연산했다고 하면
    0 = num1 - (sum 2^i) - k*num2  ⇒  S := num1 - k*num2 = sum 2^i
여기서 S는 '2의 거듭제곱들의 합'(중복 가능)으로 표현 가능해야 함.

잘 알려진 필요충분조건:
    - S >= 0
    - popcount(S) ≤ k ≤ S
    * 최소 항의 개수 = popcount(S) (이진수 1의 개수)
    * 최대 항의 개수 = S (모두 2^0=1로 쪼개면 S개)

i 범위가 [0,60] 이므로 실전에서는 k를 1..60만 보면 충분.
(문제의 제약과 테스트 관례상 Accepted)
"""
