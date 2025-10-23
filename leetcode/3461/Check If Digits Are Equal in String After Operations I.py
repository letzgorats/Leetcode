# solution 1 - (math,string,simulation) - (43ms) - (2025.10.23)
class Solution:
    def hasSameDigits(self, s: str) -> bool:

        n = len(s)
        tmp = list(s)
        while len(tmp) > 2:

            tmp2 = []
            for i in range(n - 1):
                tmp2.append((int(tmp[i]) + int(tmp[i + 1])) % 10)
            tmp = tmp2[:]
            n -= 1

        # return eq(*tmp) # 이렇게 해도 된다.
        return len(set(tmp)) == 1