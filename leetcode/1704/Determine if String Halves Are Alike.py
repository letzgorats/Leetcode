class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        a = s[:len(s)//2]
        b = s[len(s)//2:]

        standard = 0
        
        for i in a:
            if i in vowels:
                standard += 1
        for j in b:
            if j in vowels:
                standard -= 1

        return standard == 0
