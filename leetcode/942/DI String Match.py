class Solution:
    def diStringMatch(self, s: str) -> List[int]:

        answer = [0] * (len(s) + 1)
        dec = len(s)
        inc = 0

        for idx, ch in enumerate(s):

            if ch == "I":
                answer[idx] = inc
                inc += 1
            elif ch == "D":
                answer[idx] = dec
                dec -= 1

        if s[-1] == "D":
            answer[-1] = dec
        else:
            answer[-1] = inc

        return answer