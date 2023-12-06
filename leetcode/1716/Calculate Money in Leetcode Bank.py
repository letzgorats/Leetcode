# sol 1)
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

  # sol2)
  class Solution(object):
    def totalMoney(self, n):

        total = 0

        for day in range(n):

            total += (day // 7 + 1) + (day % 7)
            

        return total
