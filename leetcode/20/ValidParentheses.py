class Solution(object):
    def isValid(self, s):
      
        stack = []

        pair =  {")":"(","}":"{","]":"["}

        for i in s:
            if i in pair.values():
                stack.append(i)
            elif i in pair.keys():
                if stack == [] or stack.pop() != pair[i]:
                    return False

        if len(stack) == 0:
            return True
