# first try
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        answer = False

        if len(s) != len(t):
            return answer
        
        else:
            s_check = []
            t_check = []
            for i in s:
                s_check.append(s.index(i))

            for j in t:
                t_check.append(t.index(j))

            if s_check == t_check:
                answer = True
            
            return answer


# second solution
from collections import defaultdict
class Solution(object):
    def isIsomorphic(self, s, t):

        counts = defaultdict(list)
        countt = defaultdict(list)

        for idx,st in enumerate(s):

            counts[st].append(idx)
        
        for idx,tt in enumerate(t):

            countt[tt].append(idx)

        for k,v in counts.items():

            if v not in countt.values():
                return False
        
        return True


# others solution
class Solution(object):
    def isIsomorphic(self, s, t):

        return len(set(zip(s,t))) == len(set(s)) == len(set(t))


            

        
        
