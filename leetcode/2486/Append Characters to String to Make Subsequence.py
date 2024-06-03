class Solution(object):
    def appendCharacters(self, s, t):
        
        if t in s:
            return 0
        
        s_idx, t_idx = 0,0
        current = ""

        while s_idx < len(s) and t_idx < len(t):

            if s[s_idx] == t[t_idx]:
                current += s[s_idx]
                s_idx += 1 
                t_idx += 1
            
            else:
                s_idx += 1
            
        return len(t) - len(current)
