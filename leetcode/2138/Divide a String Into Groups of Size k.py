# solution 1 - (string,split) - (0ms) - (2025.06.22)
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        answer = []
        for i in range(0, len(s), k):
            tmp = s[i:i + k]
            answer.append(tmp)

        if len(answer[-1]) != k:
            answer[-1] = answer[-1] + (k - len(answer[-1])) * fill

        return answer