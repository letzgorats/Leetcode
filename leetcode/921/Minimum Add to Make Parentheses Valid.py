# solution 1 - stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []

        for c in s:

            if stack and c == ")":
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)

        return len(stack)

# solution 2 - stack(clean code)
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []

        for c in s:

            if stack and c == ")" and stack[-1] == '(':
                    stack.pop()
            else:
                stack.append(c)

        return len(stack)