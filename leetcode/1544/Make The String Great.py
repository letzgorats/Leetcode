class Solution(object):
    def makeGood(self, s):

        idx = 0
        while idx < len(s)-1:
      
            if ord(s[idx])-32 == ord(s[idx+1]) or ord(s[idx])+32 == ord(s[idx+1]):
                s = s[:idx] + s[idx+2:]
                idx = 0
            else:
                idx += 1
    

        return s


class Solution(object):
    def makeGood(self, s):

        stack = []

        for st in s:
            if stack and (stack[-1].swapcase() == st):
                stack.pop()
            else:
                stack.append(st)

        return "".join(stack)
