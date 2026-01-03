# solution 1 - (dp,math) - (7ms) - (2026.01.03)
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        A, B = 6, 6
        '''
        pattern ABA : 121,131,212,232,313,323 -> 6 개
        pattern ABC : 123,132,213,231,312,321 -> 6 개

        ABA(121) 였으면, 다음행 : 212,213,232,312,313 -> 3*ABA, 2*ABC
        ABC(123) 였으면, 다음행 : 212,231,312,232 -> 2*ABA, 2*ABC
        '''

        for _ in range(n - 1):
            A, B = (2 * A + 2 * B) % mod, (2 * A + 3 * B) % mod

        return (A + B) % mod