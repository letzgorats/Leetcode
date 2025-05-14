# solution 1 - (dp,transform,frequency,hash_table,counting) - (4902ms) - (2025.05.14)
from typing import List
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:

        MOD = 10 ** 9 + 7

        # 1️⃣ 변환 규칙 행렬 생성
        # a -> b , b -> c, c ->d, .... , x->y, y->z, z->a
        transform_rules = [[0] * 26 for _ in range(26)]
        for i in range(26):
            steps = nums[i]
            for j in range(steps):
                next_char = (i + j + 1) % 26
                transform_rules[i][next_char] += 1

        # print(transform_rules)

        # 2️⃣ 빠르게 t번 거듭제곱 계산

        # 행렬곱셈을 구현한 함수
        def matrix_multiply(A, B, mod):
            '''
            A = [[1, 2],
                [3, 4]]

            B = [[5, 6],
                [7, 8]]

            1*5 + 2*7    1*6 + 2*8
            3*5 + 4*7    3*6 + 4*8

            A*B = [[19,22],
                   [43,50]]
            '''
            size = len(A)
            result = [[0] * size for _ in range(size)]
            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        # A[i][k] * B[k][j] -> A의 i 번째 행과 B의 j번쨰 열을 곱함
                        # 그 결과를 result[i][j]에 더해줌.
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD

            return result

        # power 거듭제곱 행렬 계산
        def matrix_pow(matrix, power, mod):
            '''
            주어진 행렬(matrix)을 power 만큼 거듭제곱한다.
            최종 결과는 mod로 나눈 값을 유지한다.
            '''
            size = len(matrix)
            # 단위 행렬을 생성한다. (I*A=A)
            # 1 0 0 ...
            # 0 1 0 ...
            # 0 0 1 ...
            result = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

            # 분할 정복을 시작한다.
            while power > 0:
                # 만약 power가 홀수이면, 지금까지의 결과에 한 번 곱해준다.
                #
                if power % 2 == 1:
                    result = matrix_multiply(result, matrix, mod)

                # matrix를 제곱해준다.(2배로 키운다)
                matrix = matrix_multiply(matrix, matrix, mod)

                # power를 절반으로 줄인다.(2로 나눈다)
                power //= 2

            return result

        # 3️⃣ t번 반복한 transform_rules 계산
        final_matrix = matrix_pow(transform_rules, t, MOD)

        # 4️⃣ 초기 카운트 벡터 생성
        count = [0] * 26
        for idx, alpha in enumerate(s):
            count[ord(alpha) - 97] += 1

        # print(count)

        # 5️⃣ 최종 결과 계산 - 행렬곱셈x 벡터곱셈o
        final_count = [0] * 26
        for i in range(26): # 도착지
            for j in range(26): # 출발지
                final_count[i] = (final_count[i] + final_matrix[j][i] * count[j]) % MOD
        '''
        final_matrix[i][j]는 알파벳 i가 알파벳 j로 변환된 개수를 의미(x)
        i를 기준으로 업데이트 → k에서 l로 변환된 뒤에,
        l에서 m, n으로 확장된 부분을 반영하지 못한다.

        final_matrix[j][i]로 해야한다.
        j를 기준으로 final_matrix의 열(i)에 값을 누적해야 한다.
        각 j에서 i로 변환된 개수를 더해주는 구조가 되야 한다.
        j를 기준으로 업데이트 → k가 l로 변환되고,
        l이 m, n으로 확장된 것이 final_matrix[j][i]에 반영되어 누적된다.

        출발지가 j, 도착지가 i 여야 한다!!!!
        '''

        # 6️⃣ 최종 길이 반환
        return sum(final_count) % MOD


'''
transform_rules^13 을 계산해야 하는데,
13 = 2^3 + 2^2 + 2^0 이므로,
transform_rules^13 = transform_rules^(8) * transform_rules^(4) * transform_rules^(1)
이다.

power % 2 == 1일 때는 2진수로 표현했을 때 1인 자리이기 때문에 실제 연산이 필요함.
예를 들어, 13의 2진수는 1101인데, 8, 4, 1의 자리에 1이 있다.
그래서 그 순간에만 result에 곱하는 것이다.

짝수일 때는 2배씩 제곱해주면서 반복 횟수를 빠르게 줄인다.
예를 들어, t = 8 이라면, 
transform_rules^8 을 일일이 다 곱하는 것이 아니라,
transform_rules^2를 한 번 구해놓으면,
또다시 그걸 곱하면 transform_rules^4
또다시 곱하면 transform_rules^8
즉, 3번만에 8번의 반복을 처리할 수 있는 셈이다.

정리하면,
power가 짝수면 그냥 제곱만 하고,
power가 홀수면 지금까지 계산한 값을 result에 추가한다.

power가 짝수라면, power %2 == 0 이니까 그냥 넘기고,
matrix는 자기자신을 제곱하게 된다.
반대로, power가 홀수라면, result에 곱해주고, 그 다음에 matrix가 또 제곱된다.

여기서 중요한 점은, 짝수일 때는 matrix만 제곱하고, result 는 변경하지 않는다는 점이다.
그 이유는, 그 제곱된 결과가 다음 반복에서 필요하기 때문이다.

예를 들어, power = 6 라고 하면,
6 -> 3 -> 1 -> 0 순서로 power 가 줄어든다.
순서대로 보면,
power가 6일 때: 짝수 → matrix = matrix * matrix
power가 3일 때: 홀수 → result = result * matrix
power가 3일 때: 짝수 → matrix = matrix * matrix
power가 1일 때: 홀수 → result = result * matrix

짝수일 때는 행렬만 제곱해두고, 나중에 홀수일 때 그 제곱된 값을 사용한다.
그래서 else가 필요 없다.
짝수인 경우는 그 자체로 미리 준비된 거듭제곱 결과이기 때문이다.


왜 i(행)이 아니라 j(열)기준으로 행렬의 곱셈결과가 누적되어야 하는가? 
행렬 곱셈은 이렇게 진행된다.

final_matrix = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
count = [2, 0, 0, 1]

라고 하면,

final_count의 0번째 인덱스를 구하기 위해서는:
final_count[0] = final_matrix[0][0] * count[0] 
                + final_matrix[1][0] * count[1] 
                + final_matrix[2][0] * count[2] 
                + final_matrix[3][0] * count[3]

-> 0 * 2 + 0 * 0 + 0 * 0 + 1 * 1 = 1
즉, 출발한 알바펫들이 도착한 곳이 몇개가 되었는지를 누적하는 과정이다.
우리가 구하고 싶은 것은, 각 알파벳이 최종적으로 몇 개로 변했는가?
final_matrix를 보면, "열" 단위로 값을 누적해야 → 최종적으로 해당 알파벳에 몇 개가 도착했는지 알 수 있다!!


'''


'''
# 요약

transform_rules → 각 알파벳이 변환될 규칙을 정의한 26x26 행렬

matrix_pow → transform_rules를 t번 거듭제곱하여, 최종 변환 규칙을 계산

count → 초기 문자열의 알파벳 개수 (1x26 벡터)

final_matrix → 최종 변환 규칙이 담긴 26x26 행렬

final_count → final_matrix와 count를 행렬 곱하여, 최종 변환된 알파벳 개수를 구함

sum(final_count) → 모든 알파벳 개수를 합친 최종 길이
'''
