# solution 1 - (bit,greedy) - (0ms) - (2025.10.29)
class Solution:
    def smallestNumber(self, n: int) -> int:

        bits = ['1', '11', '111', '1111', '11111', '111111', '1111111',
                '11111111', '11111111', '111111111', '1111111111']

        for b in bits:
            if int(b, 2) >= n:
                return int(b, 2)

# solution 2 - (iteration) - (0ms) - (2025.10.29)
class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = (x * 2 + 1)

        return x