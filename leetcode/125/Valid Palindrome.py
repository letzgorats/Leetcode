class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # ss = "".join(filter(str.isalnum,str(s)))

        s = filter(str.isalnum,str(s)).lower()

        n = len(s)
        answer = True
        for i in range(n):

            if s[i] != s[n-1-i]:
                answer = False
                break

        return answer
