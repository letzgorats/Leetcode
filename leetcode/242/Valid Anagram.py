class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        anagram1 = dict()
        anagram2 = dict()

        if len(s)!= len(t):
            return False

        for i in range(len(s)):

            if s[i] not in anagram1:
                anagram1[s[i]] = s.count(s[i])
            if t[i] not in anagram2:
                anagram2[t[i]] = t.count(t[i])

        return anagram1 == anagram2
