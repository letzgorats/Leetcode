# solution 1 - (math,dp,number theory,combinatorics) - (535ms) - (2025.04.22)
from collections import defaultdict
from math import comb

MOD = 10 ** 9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:

        # 최대 길이는 log2(10000)보다 작기 때문에 14까지만 탐색해도 충분
        max_len = 14  # 핵심 최적화 포인트! n이 커져도 유효 길이는 약 14를 넘지 않음(수학적 성질)

        # dp[val][length] = val에서 시작해서 길이 length를 가지는 배열 개수
        dp = [[0] * (max_len + 1) for _ in range(maxValue + 1)]

        # 초기값: 길이 1은 자기 자신으로 하나만 가능
        for val in range(1, maxValue + 1):
            dp[val][1] = 1

        # dp[val][length] = val에서 시작해서 길이 length로 확장되는 곱셈 경로 수
        # Sieve-like 방식으로 곱셈 그래프 확장
        # 예: val = 2 → 4, 6, 8, 10, ..., 2*k ≤ maxValue
        for val in range(1, maxValue + 1):
            for length in range(1, max_len):
                if dp[val][length] == 0:
                    continue    # 이전에 도달 불가능했던 경로는 무시
                for mult in range(2, (maxValue // val) + 1):
                    nxt = val * mult
                    if nxt > maxValue:
                        break
                    # val로 끝나는 length짜리 배열을 확장하여 nxt로 끝나는 length+1짜리 배열 생성
                    dp[nxt][length + 1] = (dp[nxt][length + 1] + dp[val][length]) % MOD

        # Step 2: 각 (val, length)쌍에 대해
        # 해당 배열을 길이 n으로 확장하는 조합 수를 곱해 최종 결과에 더함
        # 조합 수 = (n - 1) C (length - 1)
        # 예: [2,4] (length=2) → n=4로 확장 → [2,2,2,4], [2,2,4,4], [2,4,4,4] 등 comb(3,1) = 3개
        res = 0
        for val in range(1, maxValue + 1):
            for length in range(1, max_len + 1):
                # length 길이를 n 길이로 확장하는 경우의 수 = comb(n-1, length-1)
                ways = comb(n - 1, length - 1)
                res = (res + dp[val][length] * ways) % MOD

        return res

'''
- max_len = 14 제한  : n 이 커질수록 대부분의 수열은 14단계를 넘지 않음(수학적 성질)
- dp[val][length] : val 에서 시작해서 길이 length의 수열 개수
- comb(n-1,length-1) : 그 수열을 n 길이로 늘리는 방법 수 
- 시간복잡도 : O(maxValue * 14 * log(maxValue)) 이내 -> 매우 빠름
'''


'''
dp[nxt][length + 1] = (dp[nxt][length + 1] + dp[val][length]) % MOD

-> 지금 val 로 끝나는 Length 짜리 배열이 존재한다면, 그 배열 뒤에 nxt 라는 수를 붙여서 (length + 1) 짜리 배열을 만들 수 있다는 뜻

현재는 dp[val][length] 에 저장된 상태다.
즉, 길이가 length 이고, 마지막 값이 val 인 배열이 몇 개인지를 알고 있다.

이제 우리는 val의 배수인 어떤 수 nxt 를 이어 붙여야 한다.
(그래야 조건 arr[i] % arr[i-1] == 0 이 성립하니까)

(ex)
val = 2, length = 2
즉, [2,4] 같은 배열이 존재한다고 해보자 -> 이건 dp[4][2] += dp[2][1] 로 만들어졌겠지?

이제, 배수 확장 시도
nxt = 4 또는 6 또는 8 등
예를 들어 nxt = 8 이면, 기존 [2,4] 에 8을 붙이면 [2,4,8] 이 된다!
-> 이 배열은 길이 3, 마지막 순느 8

그러니까 dp[8][3] += dp[4][2] => 즉, dp[nxt][length+1] = dp[val][length] 이렇게 되는 셈이다.

다시 정리하자면,

현재까지 만든 [val1,val2, ... , val] 같은 length 짜리 배열이 dp[val][length] 개 있다면,
이 배열들 각각의 뒤에 val 의 배수인 nxt 를 붙이면,
새로운 length+1 짜리 배열이 생성되고, 그 개수만큼 dp[nxt][legnth+1] 에 누적해줘야 한다는 뜻이다.

'''