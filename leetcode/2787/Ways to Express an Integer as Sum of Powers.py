# solution 1 - (knapsack algorithm, dynamic programming,bottom up) - (279ms) - (2025.08.12)
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7

        # 1) 후보 항목 만들기 : i^x <=n
        powers = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            powers.append(p)
            i += 1

        # print(powers)

        # 2) 0/1 냅색 카운팅
        # dp[s] = 정수 s 를 만들 수 있는 조합의 수(합이 s가 되는 방법의 수)
        dp = [0] * (n + 1)
        dp[0] = 1  # 아무것도 안 써서 0 을 만드는 방법 1개

        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

            # print(dp)

        return dp[n]


'''
# 냅색 알고리즘-물건 담기로 바꿔보면,

"새로운 물건 p 를 넣는다" = p 를 사용해서 s 를 만드는 경우를 더하는 것.
-> p를 쓰지 않는 경우 : 기존 dp[s] 유지
-> p를 쓴느 경우 : 남은 합 s-p 를 만드는 방법 수만큼 더함 => dp[s-p]

그래서 dp[s] = (dp[s] + dp[s-p]) => dp[s] += dp[s-p]

# 내림차순의 이유
-> 오름차순으로 s 를 돌리면, 같은 라운드에서 갱신된 dp[s] 값이 dp[s-p] 계산에
    재사용돼서 같은 물건 p를 여러번 쓰는 효과가 발생한다.
-> 그래서 0/1 냅색 알고리즘에서는 s 를 내림차순으로 순회해서 한 라운드에 
    동일 물건이 중복 사용되지 않도록 막는다.

# 정리
“0/1 냅색에서 최적값 대신 경우의 수를 세고, 물건의 무게를 제곱수로 바꾸면 된다.
내림차순 업데이트로 같은 제곱수를 여러 번 쓰는 걸 막는다.”
'''