class Solution:
    def findComplement(self, num: int) -> int:

        n = len(bin(num)[2:])
        s = (1 << n) - 1  # n 비트 수가 모두 1인 정수

        return s ^ num