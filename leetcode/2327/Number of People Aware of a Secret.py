# solution 1 - (sliding window,dp) - (320ms) - (2025.09.09)
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  # 1일차에 1명이 비밀을 알게 됨

        for day in range(1, n + 1):
            for shareDay in range(day + delay, min(day + forget, n + 1)):
                dp[shareDay] += dp[day]
                dp[shareDay] %= MOD
        # print(dp)
        res = 0
        for i in range(n - forget + 1, n + 1):
            res += dp[i]
            res %= MOD

        return res


'''
day : 비밀을 처음 알게 된 날
shareDay : day에 비밀을 알게 된 사람이, 다른 사람에게 비밀을 전파할 수 있는 날짜
    -> day+delay 부터 공유시작
    -> day+forget-1 까지 공유가능
    -> min(....,n) 은 전체 일수 n을 넘어가지 않도록 제한
즉, 그날 비밀을 안 사람들이 이후 일정 기간 동안 신규 인원을 만들어내는 과정


n-forget+1 일부터 N 일까지 확인하는 이유는?
 -> forget 일이 지나면, 비밀을 잊어버리므로, 마지막 날(n) 기준으로 아직 기억하는 사람들만
    카운트해야 함.
-> 따라서, dp[day] 중에서 아직 비밀을 기억 중인 사람들만 더해서 결과를 구하는 과정이 두 번째 for문!   
'''
