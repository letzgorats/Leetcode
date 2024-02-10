class Solution(object):
    def countSubstrings(self, s):
        answer = 0
        
        for i in range(len(s)):
            left = i
            right = i

            # odd length
            while left >=0 and right < len(s) and s[left]==s[right]:
                answer += 1
                left -= 1
                right += 1


            # even length
            left = i
            right = i + 1
            while left >=0 and right < len(s) and  s[left]==s[right]:
                answer += 1
                left -= 1
                right += 1

        return answer


# simplication
class Solution(object):

    def countSubstrings(self, s):
        
        answer = 0 
        for i in range(len(s)):
            # odd length
            answer += self.countPalindrom(i,i,s)
            # even length
            answer += self.countPalindrom(i,i+1,s)

    
        return answer

    def countPalindrom(self,left,right,s):
    
    	answer = 0
    	while left >=0 and right < len(s) and s[left]==s[right]:
            answer += 1
            left -= 1
            right += 1

        return answer


# second solution - less effective - 553ms
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)
        dp = [1] * n
        cnt = 0
        left = 0
        right = 0

        while left <= n-1:
            right = left
            while right < n+1:
                tmp = s[left:right] 
                if tmp and tmp == tmp[::-1]:
                    cnt += 1
                right += 1

            left += 1
        
        return cnt

how to solve -> (https://letzgorats.tistory.com/entry/%EB%A6%AC%ED%8A%B8%EC%BD%94%EB%93%9Cleetcodepython-647-Palindromic-Substrings)
