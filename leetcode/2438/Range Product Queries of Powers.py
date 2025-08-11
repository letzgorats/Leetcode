# Wrong answer
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        answer = []
        powers = []
        max_range = 32
        while n > 0:
            for i in range(max_range):
                if 2 ** i > n:
                    powers.append(2 ** (i - 1))
                    n -= (2 ** (i - 1))
                    max_range = i
                    break
                elif 2 ** i == n:
                    powers.append(2 ** i)
                    n -= 2 ** i
                    max_range = i
                    break
            # print(n)

        powers.sort()

        # print(powers)

        mod = 10 ** 9 + 7
        for a, b in queries:
            ans = 1
            for j in range(a, b + 1):
                ans *= (powers[j] % mod)
            answer.append(ans)

        # print(answer)
        return answer

# solution 1 - (bit manipulation, bitwise,brute force) - (232ms) - (2025.08.11)
from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        answer = []
        powers = []
        max_range = 32
        while n > 0:
            for i in range(max_range):
                if 2 ** i > n:
                    powers.append(2 ** (i - 1))
                    n -= (2 ** (i - 1))
                    max_range = i
                    break
                elif 2 ** i == n:
                    powers.append(2 ** i)
                    n -= 2 ** i
                    max_range = i
                    break
            # print(n)

        powers.sort()

        # print(powers)

        mod = 10 ** 9 + 7
        for a, b in queries:
            ans = 1
            for j in range(a, b + 1):
                ans = (ans * powers[j]) % mod
            ans %= mod          # '''이 부분만 수정함'''
            answer.append(ans)

        # print(answer)
        return answer

'''
ans *= (power[j] % mod) 에서 ans = (ans*power[j]) % mod
최종적으로 또 ans % mod 를 하니까 통과가 됐다.

이유?
-> 이미 루프 안에서 ans = (ans * powers[j]) % mod 로 매 스텝 모듈러를 적용했으니, ans는 항상 0...mod-1 범위에 있어서,
    마지막에도 한 번 더 %mod 를 씌워도 값은 그대로라 결과가 바뀌지 않아야 해.
    
    그런데, 이전 코드가 ans *= (powers[j] % mod) 처럼 "피연산자 하나만 mod" 를 하고 ans 에는 mod 를 안 걸었다면, ans 가
    점점 엄청 큰 정수로 불어나고(파이썬은 big int라 오버플로우는 없지만 느려질 수 있다.), 케이스에 따라 TLE/런타임 변동이 생겨날 수 있어.
    이번에 바꾼 핵심은 사실 "곱셈 후에 mod"를 걸게 된 것(ans = (ans % powers[j]) * mod) 이고, 마지막 ans %= mod 는 확인사살로 그냥
    안전벨트같은 중복처리였을 가능성이 높다. 즉, 통과의 진짜 이유는 곱셈-직후 모듈러이고, 마지막 모듈러는 본질적 영향이 없긴하다.
'''


# solution 2 - (bit manipulation) - (236ms) - (2025.08.11)
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        answer = []
        powers = []

        for i in range(n.bit_length()):
            if (n >> i) & 1:
                powers.append(1 << i)  # 2**i 와 같은 의미

        # print(powers)

        mod = 10 ** 9 + 7
        for a, b in queries:
            ans = 1
            for j in range(a, b + 1):
                ans = (ans * powers[j]) % mod
            # ans %= mod
            answer.append(ans)

        # print(answer)
        return answer


'''
비트로 powers 를 만들면 훨씬 깔끔하다.
n 을 2의 거듭제곱 합으로 분해할 때는 비트가 깔끔한데, 파이썬 내장함수인 "bit_length()"를 활용하면, 해당 정수(n)의 
이진수 비트가 몇 자리인지 알 수 있다.(이진수 길이 알 수 있는 내장함수)

2**i 대신, 1<<i 를 활용해서, powers.sort() 가 애초에 불필요하게 할 수 있다!

if (n>>i) & 1 은 무슨 뜻일까?
먼저 (n>>i)
    -> ">>" 는 오른쪽 시프트 연산자 로 "n>>i" 는 "n 을 이진수로 i 칸 오른쪽으로 민다"는 뜻이다.
    오른쪽으로 민다는 것은, i번째 비트가 맨 오른쪽(0번째 자리)로 내려온다는 뜻이다. (나누기 2 느낌)
    & 1
    -> & 는 비트연산자 AND 로, 어떤 수 x 에 x&1 을 하면 맨 오른쪽 비트(LSB:Least Significant Bit)만 남기고 나머지는 다 0 이 된다.
    -> 결과는 0 또는 1이 될 터인데, 맨 오른쪽 비트가 1이면 결과는 1, 맨 오른쪽 비트가 0 이면 결과는 0 이 되는 셈이다.

즉, (n>>i) & 1 의 진짜 의미는
    -> n 을 오른쪽으로 i 번 이동시켜 i 번째 비트를 맨 오른쪽으로 가져오고,
    -> 그 후 &1 로 그 비트가 1인지(켜져 있는지) 확인한다.
    -> 결과가 1이면 i 번째 비트가 켜져 있다는 뜻이고, 0 이면 꺼져 있다는 뜻이 된다.

(ex) n = 46 # 101110(2진수)
i = 3
(n >> i) -> 00 101 (2진수 5)
(n >> i) & 1 -> 101 & 001 = 001 -> 결과 1

즉, n의 3번째 비트(0부터 세었을 때) 가 1이므로, 조건문은 True가 된다. 
    
'''

# solution 3 - (prefix sum) - (83ms) - (2025.08.11)
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        answer = []
        exps = []  # 지수 배열

        for i in range(n.bit_length()):
            if (n >> i) & 1:
                exps.append(i)  # 지수 저장

        # print(exps)

        # 추후 쿼리 게산을 위해 누적합 - prefix sum
        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)
            # print(pref)

        MOD = 10 ** 9 + 7
        answer = []
        for a, b in queries:
            e = pref[b + 1] - pref[a]  # 구간 지수 합
            # print(e)
            answer.append(pow(2, e, MOD))

        return answer

'''
지수 합으로 O(1) 쿼리

모든 항이 2의 거듭제곱이므로, powers[j] = 2^(exp[j]) 이고, 구간 곱 = 2 ^(sum(exp[a..b]))
즉, 지수(prefix sum) 로 바꾸면 쿼리마다 한 번의 pow 로 끝이다.

'''


