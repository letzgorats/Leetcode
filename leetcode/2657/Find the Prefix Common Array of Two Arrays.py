class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        n = len(A)
        C = [0] * n
        if A[0] == B[0]:
            C[0] = 1
        for i in range(1, n):
            C[i] = len(set(A[:i + 1]) & set(B[:i + 1]))

        return C