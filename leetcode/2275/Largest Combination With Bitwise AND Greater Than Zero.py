# solution 1 - zfill
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        maxn = max(candidates)
        binn = bin(maxn)[2:]
        n = len(binn)
        a = [0] * n

        for candidate in candidates:
            s = bin(candidate)[2:].zfill(n)

            for j in range(n):
                if s[j] == '1':
                    a[j] += 1

        maxi = max(a)
        return maxi

# solution 2 - bit manipulation
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        bit_counts = [0] * 24

        for number in candidates:
            for i in range(24):
                if number & (1 << i):
                    bit_counts[i] += 1

        return max(bit_counts)


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:

        res = 0
        for i in range(32):
            cnt = 0

            for n in candidates:
                cnt += 1 if (1 << i) & n else 0
            res = max(res, cnt)

        return res