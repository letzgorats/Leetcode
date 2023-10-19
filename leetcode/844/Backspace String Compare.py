class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        tmp1 = []
        for alpha in s:
            if alpha == "#" and len(tmp1)!=0:
                tmp1.pop()
            elif alpha != '#':
                tmp1.append(alpha)
        
        tmp2 = []
        for alpha in t:
            if alpha == "#" and len(tmp2)!=0:
                tmp2.pop()
            elif alpha != "#":
                tmp2.append(alpha)

        # print(tmp1)
        # print(tmp2)
        return tmp1 == tmp2
