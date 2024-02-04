
# most optimal solution
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while need[s[i]] < 0: need[s[i]] += 1; i += 1
                if not J or j - i <= J - I: I, J = i, j
                need[s[i]] += 1; i += 1; missing += 1       # SPEEEEEEEED UP!
        return s[I : J]


# more optimal solution
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]




# should be optimal solution
from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)

        s_count, t_count = Counter(), Counter(t)
        if n > m :
            return ""
        
        l = 0
        candi = ""
        
        for r in range(m):
            s_count[s[r]] += 1
            # print(r, s_count)
            while (s_count & t_count == t_count):
                if len(s[l:r+1]) < len(candi) or candi == "":
                    candi = s[l:r+1]
                s_count[s[l]] -= 1
                l += 1
        

        return candi


            
