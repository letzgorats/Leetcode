# solution 1 - deque
from collections import deque
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        if len(s) != len(goal):
            return False

        a = deque(list(s))
        b = deque(list(goal))

        idx = 0
        while a != b and idx < len(s):
            a.rotate(-1)
            idx += 1

        if a == b:
            return True
        return False

# solution 2 - concatenation
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return s in goal + goal

# solution 3 - slicing
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True
        return False