class Solution(object):
    def minRemoveToMakeValid(self, s):


        s = list(s)
        stack = []

        for i, st in enumerate(s):
            if st == "(":
                stack.append(i)
            elif st == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ''


        while stack:
            s[stack.pop()] = ''
        
        return "".join(s)
