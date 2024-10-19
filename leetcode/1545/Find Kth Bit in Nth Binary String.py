class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def flip(s1):
            s2 = list(s1)
            for j in range(len(s2)):
                if s2[j] == '1':
                    s2[j] = '0'
                else:
                    s2[j] = '1'
            return "".join(s2)

        def concatenation(cur, idx):

            if idx == n:
                return cur

            return concatenation(cur + "1" + flip(cur[::-1]), idx + 1)

        sn = concatenation("0", 1)

        return sn[k - 1]