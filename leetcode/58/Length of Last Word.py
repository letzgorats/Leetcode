# first try 
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        last = s.strip(" ").split(" ")[-1]
        return len(last)


# second try solution
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        

        return len(list(s.split())[-1])
