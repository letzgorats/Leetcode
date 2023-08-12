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


how to solve -> (https://letzgorats.tistory.com/entry/%EB%A6%AC%ED%8A%B8%EC%BD%94%EB%93%9Cleetcodepython-647-Palindromic-Substrings)
