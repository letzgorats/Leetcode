# solution 1 - deque, monotonic stack - O(n)
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        answer = ""
        spaces = deque(spaces)
        for idx, ch in enumerate(s):

            while spaces and idx == spaces[0]:
                spaces.popleft()
                answer += " "

            answer += ch

        return answer

# solution 2
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        j = 0
        for i in range(len(spaces)):
            res += s[j:spaces[i]]
            res += " "
            j = spaces[i]

        res += s[j:]

        return res