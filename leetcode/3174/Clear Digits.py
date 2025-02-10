# solution 1 - string function
class Solution:
    def clearDigits(self, s: str) -> str:

        if len(s) == 2:
            if not s.isalpha():
                return ""

        while not s.isalpha():

            for idx, num in enumerate(s):

                if num.isdigit():
                    s = s[:idx - 1] + s[idx + 1:]
                    break

            if len(s) == 2:
                if not s.isalpha():
                    return ""

        return s

# solution 2 - stack
class Solution:
    def clearDigits(self, s: str) -> str:

        answer = []

        for ch in s:

            if ch.isalpha():
                answer.append(ch)
            else:
                answer.pop()

        return "".join(answer)
