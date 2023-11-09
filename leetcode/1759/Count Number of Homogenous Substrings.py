class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """

        def calculate(n):
            return (n * (1+n)) // 2


        answer = 0
        cnt = 1
        INF = 10 ** 9 + 7

        for i in range(len(s)-1):
            temp = s[i]
            if (s[i+1] == temp):
                cnt += 1
            else:
                answer += calculate(cnt)
                cnt = 1
                temp = s[i+1]

        answer += calculate(cnt)

        return answer % (INF)

