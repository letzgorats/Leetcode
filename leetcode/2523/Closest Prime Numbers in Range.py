# TLE - greedy,help function - (2025.03.07)
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def is_prime(number):
            for i in range(2, int(sqrt(number)) + 1):
                if number % i == 0:
                    return False
            return True

        prime_candi = []

        for num in range(left, right + 1):

            if is_prime(num):
                prime_candi.append(num)

        if len(prime_candi) == 1:
            return [-1, -1]

        answer = [-1, -1]
        min_gap = prime_candi[-1] - prime_candi[0]
        for i in range(len(prime_candi) - 1):
            g = prime_candi[i + 1] - prime_candi[i]
            if g < min_gap:
                min_gap = g
                answer[0], answer[1] = prime_candi[i], prime_candi[i + 1]

        return answer

# solution 1 - Sieve of Eratosthenes, Number theory - (1626ms) - (2025.03.07)
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        is_prime = [True] * (right + 1)
        is_prime[0], is_prime[1] = False, False  # 0 과 1은 소수가 아님

        # 매번 is_prime 함수 호출하는 건 O(M√N)
        # 여기선 O(N log log N) - 한 번에 소수를 찾고 범위를 체크
        # 소거법 느낌으로 이미 is_prime[i] 가 아니면 체크 할 필요 없게 하는 장치
        for i in range(2, int(sqrt(right)) + 1):
            if is_prime[i]:
                for j in range(i * i, right + 1, i):
                    is_prime[j] = False

        # 2. left ~ right 범위에서 소수 리스트 만들기
        prime_candi = [num for num in range(left, right + 1) if is_prime[num]]

        if len(prime_candi) == 1:
            return [-1, -1]

        answer = [-1, -1]
        min_gap = float('inf')
        for i in range(len(prime_candi) - 1):
            g = prime_candi[i + 1] - prime_candi[i]
            if g < min_gap:
                min_gap = g
                answer[0], answer[1] = prime_candi[i], prime_candi[i + 1]

        return answer

'''
(TLE) 
is_prime 을 매번 호출 하는 연산
left = 10^6, right = 10^7 이라면, 약 900만개 숫자범위
-> 각 숫자마다 O(M√N) 연산 수행
-> 900만 x O(√10^7) => 900만 x 3162 => 28 * 10^9 => 약 280억회 연산 -> 너무 비효율적

(에라토스테네스의 체) 
O(Nlog logN) 이므로 O(10^7loglog10^7)
-> 10^7 X 3 => 3 * 10^7 => 약 3000만회 연산 -> 훨씬 빠름
'''