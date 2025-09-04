# solution 1 - (math,greedy) - (0ms) - (2025.09.04)
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        if abs(x - z) > abs(y - z):
            return 2
        elif abs(x - z) == abs(y - z):
            return 0
        else:
            return 1

