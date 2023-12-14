class Solution(object):
    def wordPattern(self, pattern, s):
        
        pair = dict()
        s = list(map(str,s.split()))

        if len(s) != len(pattern):
            return False

        for idx,p in enumerate(pattern):

            if p not in pair:
                if s[idx] in pair.values():
                    return False
                pair[p] = s[idx]
            elif pair[p] != s[idx]:
                return False
        
        return True
