# solution 1 - (greedy,simulation) - (44ms) - (2025.102.07)
class Solution:
    def countOdds(self, low: int, high: int) -> int:

        # 짝홀
        if low % 2 == 0 and high % 2 == 1:
            return (high - low) // 2 + 1
        # 짝짝
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
        # 홀홀
        if low % 2 == 1 and high % 2 == 1:
            return (high - low) // 2 + 1
        # 홀짝
        if low % 2 == 1 and high % 2 == 0:
            return (high - low) // 2 + 1