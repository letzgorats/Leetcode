# solution 1 - (greedy,math) - (169ms) - (2025.12.08)
import math
class Solution:
    def countTriples(self, n: int) -> int:

        squares = set()
        for i in range(1, n + 1):
            squares.add(pow(i, 2))

        ans = 0
        for c in squares:
            for a in range(1, n + 1):
                b = c - pow(a, 2)
                if 1 <= b <= n * n:
                    if math.sqrt(b).is_integer():
                        ans += 1
        return ans


