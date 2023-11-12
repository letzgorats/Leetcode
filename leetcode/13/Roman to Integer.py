class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}

        answer = 0
        n = len(s)
        finish = False
        idx = 0

        while idx < n-1:

            if roman[s[idx]] < roman[s[idx+1]]:

                answer += (roman[s[idx+1]]-roman[s[idx]])
                idx += 2
                if idx == n-1:
                    finish = False
                else:
                    finish = True

            else:

                answer += roman[s[idx]]
                idx += 1
                if idx == n-1:
                    finish = False

            # print(answer)

        if not finish:
            answer += roman[s[-1]]

        return answer
