class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []
        current = list(s)

        for i in range(len(s)):

            if s[i] == ")":
                idx = stack.pop()
                current[idx + 1:i] = current[idx + 1:i][::-1]

            elif s[i] == "(":
                stack.append(i)

        return "".join(c for c in current if c not in '()')