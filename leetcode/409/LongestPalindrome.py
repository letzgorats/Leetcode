# solution 1
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        answer = 0
        alpha = {}
        for c in s:
            if c not in alpha:
                alpha[c] = 1
            else:
                alpha[c] += 1

        odd_exist = False
        max_odd = 0
        for value in  alpha.values():
            if value % 2 == 0:
                answer += value
            else:
                max_odd = max(max_odd,value)
                odd_exist = True
                answer += ( value -1 )
        if odd_exist:
            answer += 1
        return answer



# second solution - 2024-06-04

class Solution(object):
    def longestPalindrome(self, s):

        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i],0)+1

        if len(count) == 1:
            for k,v in count.items():
                return v

        answer = 0
        check = False
        for k,v in count.items():

            if v % 2 == 0:
                answer += v
            elif v % 2 == 1:
                answer += (v-1)
                check = True
        
        if check:
            answer += 1

        return answer
