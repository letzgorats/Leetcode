# solution 3 - (simulation,greedy) - (0ms) - (2025.10.25)
class Solution:
    def totalMoney(self, n: int) -> int:

        window = [1, 2, 3, 4, 5, 6, 7]

        if n // 7 == 0:
            return sum(window[:n % 7])
        else:
            ans = 0
            week = n // 7
            ans += (28 * week)  # 한주 계산
            # 주간 누적값 계산(월요일마다 증가
            for i in range(1, week):
                ans += 7 * i
            # 마지막 주간 누적값 + 계산
            ans += (n % 7) * week
            ans += sum(window[:n % 7])

        return ans



# sol 1) - 21ms - (2023.12.06)
class Solution(object):
    def totalMoney(self, n):

        s = 0
        answer = 0
        m = n

        while m != 0:

            m = n // 7
            n %= 7

            for i in range(m):
                s += 1
                for j in range(s,s+7):
                    answer += j

        s += 1
        for k in range(s,s+n):
            answer += k
        
        return answer

  # sol2) - 21ms - (2023.12.06)
  class Solution(object):
    def totalMoney(self, n):

        total = 0

        for day in range(n):

            total += (day // 7 + 1) + (day % 7)
            

        return total
