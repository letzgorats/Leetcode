class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        cnt = 0
        g = sorted(g,reverse=True)
        s = sorted(s,reverse=True)

        if len(s) == 0:
            return 0
        i = 0 
        j = 0
        while i < len(s) and j < len(g):
            if s[i] >= g[j] :
                cnt += 1
                i += 1
            j += 1

        return cnt
