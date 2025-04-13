# solution 1 - good integer, math, binary exponentiation, pow - (3ms) - (2025.04.13)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7

        # even 자리에는 -> 짝수 [0,2,4,6,8] : 총 5가지
        # odd 자리에는 -> 소수 [2,3,5,7] : 총 4가지
        odd = n // 2
        even = n - odd

        # 전체 경우의 수 -> 5^(n/2) * 4^(n/2)
        result = (5 ** (even % mod) * 4 ** (odd % mod)) % mod
        return result

    '''
    문자열 길이가 n 이면, 각 자리에 숫자를 하나씩 골라야 한다.

    각 자리의 선택지는 독립적이다.
    0 번 자리에 5가지 선택
    1 번 자리에 4가지 선택
    2번 자리에 5가지 선택 
    3번 자리에 4가지 선택
    4번 자리에 5가지 선택

    -> 이렇게 되면 전체 경우의 수는 : "각 자리의 경우 수를 모두 곱한 것"이 된다!

    (ex) n = 4
    0(짝수) : 짝수만, 가능한 숫자 수 -> 5가지
    1(홀수) : 소수만, 가능한 숫자 수 -> 4가지
    2(짝수) : 짝수만, 가능한 숫자 수 -> 5가지
    3(홀수) : 소수만, 가능한 숫자 수 -> 4가지
    => 5^2 * 4^2

    즉, 길이 n 일 때, 
    짝수 인덱스 자리수는 n/2 : even 
    홀수 인덱스 자리수는 n/2 : odd
    총 경우의 수는 => 5^even * 4 ^odd
    '''

# solution 2 - recursive - (3ms) - (2025.04.13)
class Solution:
    def countGoodNumbers(self, n: int) -> int:

        MOD = 10 ** 9 + 7

        def expo(x, num):
            if num == 0:
                return 1
            elif num % 2 == 0:
                return expo(x ** 2 % MOD, num // 2)
            return x * expo(x, num - 1) % MOD

        # even 자리에는 -> 짝수 [0,2,4,6,8] : 총 5가지
        # odd 자리에는 -> 소수 [2,3,5,7] : 총 4가지

        # n 이 짝수일 때 -> 5^0 * 20^(n//2) = 20^(n//2)
        # n 이 홀수일 때 -> 5^1 * 20^(n//2) = 5 * 20^(n//2)
        return 5 ** (n % 2) * expo(20, n // 2) % MOD

'''
각 짝수-홀수 인덱스 쌍(2자리) 는 

짝수 인덱스(5가지) * 홀수 인덱스(4가지) => 총 5*4 = 20 가지 조합
(ex) n = 4 이면, 인덱스 0(짝수) x 1(홀수) x 2(짝수) x 3(홀수)
=> 두 쌍이 각각 20가지 => 총 20^2 = 400

(ex) n = 3 이면, 인덱스 0(짝수) x 1(홀수) x 2(짝수)
=> 짝수 x 홀수 한 쌍이 20가지 => 20^1 = 20, 
=> (나머지 한 자리는 짝수자리이므로 5만 곱해주면 됨) 짝수 5가지  = 5 x 20 = 100

expo 함수는 binary exponentiation(이진 거듭제곱법)을 재귀로 구현한 버전
-> 정확히 pow(x,num,MOD)를 직접 구현한 함수, 재귀 구조라 x^num을 빠르게 구하면서 MOD를 중간중간에 적용하는 구조
'''

# solution 3 - pow,mod - (0ms) - (2025.04.13)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        # even 자리에는 -> 짝수 [0,2,4,6,8] : 총 5가지
        # odd 자리에는 -> 소수 [2,3,5,7] : 총 4가지

        return (pow(5, n % 2, MOD) * pow(20, n // 2, MOD)) % MOD
